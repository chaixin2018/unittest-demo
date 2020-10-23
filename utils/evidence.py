import time
import pyautogui
import pyperclip
import win32api
import win32con
import win32gui


# 1	找到excel的句柄，就可以操作这个excel文件
# 2	不能直接粘贴板复制粘贴图片 但可以通过插入图片实现
# 3	插入图片的快捷键是 ALT+L + P+F
# 4	可以截屏图片保存这个图片的文件名 在插入图片的位置直接找到这个图片即可
# 5	每次插入图片后，可以滚动excel条，然后通过鼠标的位置坐标，点击后插入图片
import xlwt


a = 3


def Fuc():
    global a
    print(a)
    a = a+1
    print(a)

Fuc()
print(a)

# workbook = xlwt.Workbook(encoding='utf-8')  # 新建工作簿
# sheet1 = workbook.add_sheet("测试表格")
# # name = "E:\chaixin\\02_working\\04_automation\project\demo4_0602_changeJapaneseName\Report\TestReport20200608-1536" + "\\test.xlsx"
# # print(name)
# workbook.save(r"E:\chaixin\\test.xls")  # 保存
# win32api.ShellExecute(0, 'open', r"E:\chaixin\\test.xls", '', '', 1)

#
# # x, y = pyautogui.position()
# # print(x, y)
#
# # pyautogui.alert('stop')
#
# # image = pyautogui.screenshot(region=(0, 0, 300, 400))
# image = pyautogui.screenshot()
# image.save(r"E:\chaixin\02_working\01_Sony\screenshot.png")
#
# img = pyautogui.screenshot(r"E:\chaixin\02_working\01_Sony\screenshot.png")
#
# # 获得excel临时文件的句柄
# handle = win32gui.FindWindow("XLMAIN", "Microsoft Excel - 工作簿1.xlsx")
# # 激活并显示窗口。
# win32gui.ShowWindow(handle, win32con.SW_MAXIMIZE)
# win32gui.EnableWindow(handle, True)
# win32gui.SetForegroundWindow(handle)
# x, y = 35, 186
# pyautogui.moveTo(x, y)
# pyautogui.click()
# time.sleep(1)
# # 鼠标移动到屏幕中央并点击
# # 上一块我们激活了窗口，这一块鼠标点击excel，目的还是确认操作excel，也可以不加这一块
# # screenWidth, screenHeight = pyautogui.size()
# # pyautogui.moveTo(screenWidth/2, screenHeight/2)
# # pyautogui.click()
# # pyautogui.doubleClick()
# # img = pyautogui.screenshot(r"E:\chaixin\02_working\01_Sony\screenshot.png")
#
# # pyperclip.copy('str1')
# # pyautogui.hotkey('ctrl', 'v')
# time.sleep(1)
# pyautogui.keyDown('Alt')
# pyautogui.keyDown("I")
# pyautogui.keyUp('Alt')
# pyautogui.keyUp("I")
# pyautogui.press('P')
# pyautogui.press('F')
#
# time.sleep(2)
# pyautogui.moveTo(279, 46, 1)
# pyautogui.click()
# time.sleep(1)
# name = r"E:\chaixin\02_working\01_Sony"
# pyautogui.typewrite(name)
# time.sleep(1)
# pyautogui.press('enter')
# pyautogui.press('enter')
#
# pyautogui.moveTo(348, 413, 1)
# pyautogui.click()
# time.sleep(1)
# name = r"screenshot.png"
# pyautogui.typewrite(name)
# time.sleep(1)
# pyautogui.press('enter')
# pyautogui.press('enter')
#
# time.sleep(3)
# pyautogui.press('enter')
#
# pyautogui.moveTo(x, y)
# pyautogui.moveRel(0, 570)
# time.sleep(2)
# pyautogui.click()
#

# 点击另存为的快捷键
# pyautogui.press('f12')
# # 清空初始文件名
# pyautogui.press('backspace')
# # 输入文件名，注意press是一个键一个键的按，所以要把文件名拆成一个一个字母的
# # file_name = list("2020-03-06.xlsx")
# # pyautogui.press(file_name)
# pyperclip.copy('str1')
# pyautogui.hotkey('ctrl', 'v')
# # 回车，实现保存
# pyautogui.press('enter')
# # 关闭excel文件
# pyautogui.hotkey('ctrl', 'w')


if __name__ == '__main__':
    pass
