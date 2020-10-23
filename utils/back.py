
import time
import pyautogui
import pyperclip
import win32con
import win32gui


# 1	找到excel的句柄，就可以操作这个excel文件
# 2	不能直接粘贴板复制粘贴图片 但可以通过插入图片实现
# 3	插入图片的快捷键是 ALT+L + P+F
# 4	可以截屏图片保存这个图片的文件名 在插入图片的位置直接找到这个图片即可
# 5	每次插入图片后，可以滚动excel条，然后通过鼠标的位置坐标，点击后插入图片


# x, y = pyautogui.position()
# print(x, y)

# pyautogui.alert('stop')

# image = pyautogui.screenshot(region=(0, 0, 300, 400))
image = pyautogui.screenshot()
image.save(r"E:\chaixin\02_working\01_Sony\screenshot.png")

img = pyautogui.screenshot(r"E:\chaixin\02_working\01_Sony\screenshot.png")

# 获得excel临时文件的句柄
handle = win32gui.FindWindow("XLMAIN", "Microsoft Excel - 工作簿1.xlsx")
# 激活并显示窗口。
win32gui.ShowWindow(handle, win32con.SW_RESTORE)
win32gui.EnableWindow(handle, True)
win32gui.SetForegroundWindow(handle)
time.sleep(1)
# 鼠标移动到屏幕中央并点击
# 上一块我们激活了窗口，这一块鼠标点击excel，目的还是确认操作excel，也可以不加这一块
screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth/2, screenHeight/2)
pyautogui.click()
pyautogui.doubleClick()
# img = pyautogui.screenshot(r"E:\chaixin\02_working\01_Sony\screenshot.png")

pyperclip.copy('str1')
pyautogui.hotkey('ctrl', 'v')

time.sleep(5)
# 点击另存为的快捷键
pyautogui.press('f12')
# 清空初始文件名
pyautogui.press('backspace')
# 输入文件名，注意press是一个键一个键的按，所以要把文件名拆成一个一个字母的
# file_name = list("2020-03-06.xlsx")
# pyautogui.press(file_name)
pyperclip.copy('str1')
pyautogui.hotkey('ctrl', 'v')
# 回车，实现保存
pyautogui.press('enter')
# 关闭excel文件
pyautogui.hotkey('ctrl', 'w')


if __name__ == '__main__':
    pass
