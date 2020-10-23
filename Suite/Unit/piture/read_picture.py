
# from PIL import Image
# import pytesseract
# #上面都是导包，只需要下面这一行就能实现图片文字识别
# text = pytesseract.image_to_string(Image.open('picture1.png'), lang='chi_sim')
# print(text)

import re  # 用于正则
from PIL import Image  # 用于打开图片和对图片处理
import pytesseract  # 用于图片转文字
from selenium import webdriver  # 用于打开网站
import time  # 代码运行停顿


class VerificationCode:
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.find_element = self.driver.find_element_by_id(self)

    def get_pictures(self):
        self.driver.get('http://daido.sitetest1.com/login')  # 打开登陆页面
        self.driver.save_screenshot('pictures.png')  # 全屏截图
        page_snap_obj = Image.open('pictures.png')
        # img = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/a')  # 查找验证码元素
        # #img = self.find_element(self, 'img_seccode')  # 验证码元素位置
        # time.sleep(3)
        # location = img.location
        # print("location=",location)
        # size = img.size  # 获取验证码的大小参数
        # print("size=", size)
        # left = location['x']
        # top = location['y']
        # right = left + size['width']
        # bottom = top + size['height']
        # print("left=",left)
        # print("top=",top)
        # print("right=",right)
        # print("bottom=",bottom)
        #image_obj = page_snap_obj.crop((left, top, right, bottom))  # 按照验证码的长宽，切割验证码
        image_obj = page_snap_obj.crop((15, 0, 215, 60))  # 按照验证码的长宽，切割验证码
        image_obj.show()  # 打开切割后的完整验证码
        self.driver.close()  # 处理完验证码后关闭浏览器
        return image_obj

    def processing_image(self):
        image_obj = self.get_pictures()  # 获取验证码
        img = image_obj.convert("L")  # 转灰度
        pixdata = img.load()
        w, h = img.size
        threshold = 160
        # 遍历所有像素，大于阈值的为黑色
        for y in range(h):
            for x in range(w):
                if pixdata[x, y] < threshold:
                    pixdata[x, y] = 0
                else:
                    pixdata[x, y] = 255
        # img.show()  # 打开切割后的完整验证码
        return img

    def delete_spot(self):
        images = self.processing_image()
        data = images.getdata()
        w, h = images.size
        black_point = 0
        for x in range(1, w - 1):
            for y in range(1, h - 1):
                mid_pixel = data[w * y + x]  # 中央像素点像素值
                if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
                    top_pixel = data[w * (y - 1) + x]
                    left_pixel = data[w * y + (x - 1)]
                    down_pixel = data[w * (y + 1) + x]
                    right_pixel = data[w * y + (x + 1)]
                    # 判断上下左右的黑色像素点总个数
                    if top_pixel < 10:
                        black_point += 1
                    if left_pixel < 10:
                        black_point += 1
                    if down_pixel < 10:
                        black_point += 1
                    if right_pixel < 10:
                        black_point += 1
                    if black_point < 1:
                        images.putpixel((x, y), 255)
                    black_point = 0
        # images.show()
        return images

    def image_str(self):
        image = self.delete_spot()
        # pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # 设置pyteseract路径
        # result = pytesseract.image_to_string(image)  # 图片转文字
        # resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", result)  # 去除识别出来的特殊字符
        # result_four = resultj[0:4]  # 只获取前4个字符
        # # print(resultj)  # 打印识别的验证码
        # return result_four
        # image.show()
        return image


if __name__ == '__main__':
    a = VerificationCode()
    a.image_str()
    # a.image_str()
