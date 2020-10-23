from selenium import webdriver
from PIL import Image
from aip import AipOcr

browser = webdriver.Chrome()  # 实例化对象
url = 'http://daido.sitetest1.com/login'
browser.get(url)

# user = "daido2"
# password = "daido002"
# elem_user = browser.find_element_by_xpath('//*[@id="username"]')
# elem_user.send_keys(user)
# elem_user = browser.find_element_by_xpath('//*[@id="loginForm"]/div[2]/div/input')
# elem_user.send_keys(password)
# browser.find_element_by_xpath('//*[@id="loginForm"]/div[7]/div/button').click()

# Function.Login.login_ra(browser,"role")
png = browser.find_element_by_id('img_seccode')  # 查找验证码元素
png.screenshot('test.png')

img = Image.open('piture/test.png')
img = img.convert('L')  # P模式转换为L模式(灰度模式默认阈值127)
count = 127  # 设定阈值
table = []
for i in range(256):
    if i < count:
        table.append(0)
    else:
        table.append(1)

img = img.point(table, '1')
img.save('captcha.png')  # 保存处理后的验证码

# 识别码
APP_ID = '21647273'
API_KEY = 'qk3p1gELsLrjMFI4E9ZKWGi3'
SECRET_KEY = 'WQVPU7F4HIHc4s15fmx3QjqeoGGGktyA'
# 初始化对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
# 读取图片


def get_file_content(file_path):
    with open(file_path, 'rb') as f:
        return f.read()


image = get_file_content('piture/captcha.png')
# 定义参数变量
options = {'language_type': 'CHN_ENG', }  # 识别语言类型，默认为'CHN_ENG'中英文混合
#  调用通用文字识别
result = client.basicGeneral(image, options)  # 高精度接口 basicAccurate
# result = client.general(image)
print(result)
try:
    code = result['words_result'][0]['words']
except:
    code = '验证码匹配失败'
    print(code)
# for item in result['words_result']:
#     print(item['words'])


# import re  # 用于正则
# from PIL import Image  # 用于打开图片和对图片处理
# import pytesseract  # 用于图片转文字
# from selenium import webdriver  # 用于打开网站
# import time  # 代码运行停顿
#
#
# class VerificationCode:
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#
#     def get_pictures(self):
#         self.driver.get('http://daido.sitetest1.com/login')  # 打开登陆页面
#         self.driver.save_screenshot('pictures.png')  # 全屏截图
#         page_snap_obj = Image.open('pictures.png')
#         img = self.find_element('img_seccode')  # 验证码元素位置
#         time.sleep(1)
#         location = img.location
#         size = img.size  # 获取验证码的大小参数
#         left = location['x']
#         top = location['y']
#         right = left + size['width']
#         bottom = top + size['height']
#         image_obj = page_snap_obj.crop((left, top, right, bottom))  # 按照验证码的长宽，切割验证码
#         image_obj.show()  # 打开切割后的完整验证码
#         self.driver.close()  # 处理完验证码后关闭浏览器
#         return image_obj
#
#     def processing_image(self):
#         image_obj = self.get_pictures()  # 获取验证码
#         img = image_obj.convert("L")  # 转灰度
#         pixdata = img.load()
#         w, h = img.size
#         threshold = 160
#         # 遍历所有像素，大于阈值的为黑色
#         for y in range(h):
#             for x in range(w):
#                 if pixdata[x, y] < threshold:
#                     pixdata[x, y] = 0
#                 else:
#                     pixdata[x, y] = 255
#         return img
#
#     def delete_spot(self):
#         images = self.processing_image()
#         data = images.getdata()
#         w, h = images.size
#         black_point = 0
#         for x in range(1, w - 1):
#             for y in range(1, h - 1):
#                 mid_pixel = data[w * y + x]  # 中央像素点像素值
#                 if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
#                     top_pixel = data[w * (y - 1) + x]
#                     left_pixel = data[w * y + (x - 1)]
#                     down_pixel = data[w * (y + 1) + x]
#                     right_pixel = data[w * y + (x + 1)]
#                     # 判断上下左右的黑色像素点总个数
#                     if top_pixel < 10:
#                         black_point += 1
#                     if left_pixel < 10:
#                         black_point += 1
#                     if down_pixel < 10:
#                         black_point += 1
#                     if right_pixel < 10:
#                         black_point += 1
#                     if black_point < 1:
#                         images.putpixel((x, y), 255)
#                     black_point = 0
#         # images.show()
#         return images
#
#     def image_str(self):
#         image = self.delete_spot()
#         pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # 设置pyteseract路径
#         result = pytesseract.image_to_string(image)  # 图片转文字
#         resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", result)  # 去除识别出来的特殊字符
#         result_four = resultj[0:4]  # 只获取前4个字符
#         # print(resultj)  # 打印识别的验证码
#         return result_four
#
#
# if __name__ == '__main__':
#     a = VerificationCode()
#     a.image_str()

###############################################3
# from aip import AipOcr
#
#  # 你的 APPID AK SK
# APP_ID = '你的APPID'
# API_KEY = '你的AK'
# SECRET_KEY = '你的SK'
#
# client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
#
# # 读取图片
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()
# # 测试文件也可以写路径
# image = get_file_content('test.jpg')
#
# #  调用通用文字识别, 图片参数为本地图片
# result = client.basicGeneral(image)
#
# # 定义参数变量
# options = {
#     # 定义图像方向
#         'detect_direction' : 'true',
#     # 识别语言类型，默认为'CHN_ENG'中英文混合
#         'language_type' : 'CHN_ENG',
# }
#
# # 调用通用文字识别接口
# results = client.basicGeneral(image,options)
# print(results)
# # 遍历取出图片解析的内容
# # for word in result['words_result']:
# #     print(word['words'])
# try:
#     code = results['words_result'][0]['words']
# except:
#     code = '验证码匹配失败'
#
# print(code)
