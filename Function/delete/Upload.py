import logging
from time import sleep
import win32api
import win32con
import Function.Base


def upload(self):
    # 点击+
    Function.Base.wait_element(self, "xpath", "/html/body/section/main/section/main/div/div/div[1]/main/aside[1]/div/div[7]/div/div/div[1]/span/i")
    Function.Base.clickT(self, "xpath", "/html/body/section/main/section/main/div/div/div[1]/main/aside[1]/div/div[7]/div/div/div[1]/span/i")
    # 点击文件名
    Function.Base.wait_element(self, "xpath", "/html/body/section/main/section/main/div/div/div[1]/main/aside[1]/div/div[3]/div/div[2]/div[3]/div")
    Function.Base.clickT(self, "xpath", "/html/body/section/main/section/main/div/div/div[1]/main/aside[1]/div/div[3]/div/div[2]/div[3]/div")
    sleep(1)
    Function.Base.clickT(self, "xpath", "/html/body/div[2]/div[1]/div[1]/ul/li[24]/span")

    # 选择主副
    Function.Base.clickT(self, "xpath",
                        "/html/body/section/main/section/main/div/div/div[1]/main/aside[1]/div/div[3]/div/div[2]/div[4]/div")
    sleep(1)
    Function.Base.clickT(self, "xpath", "/html/body/div[3]/div[1]/div[1]/ul/li[2]")

    # 上传文件
    Function.Base.clickT(self, "xpath",
                        "/html/body/section/main/section/main/div/div/div[1]/main/aside[1]/div/div[3]/div/div[2]/div[1]/div/button/span")

    sleep(2)
    win32api.keybd_event(0x31, 0, 0, 0)  # 1
    win32api.keybd_event(0x31, 0, win32con.KEYEVENTF_KEYUP, 0) # 释放
    sleep(1)
    win32api.keybd_event(0xBE, 0, 0, 0)  # .
    win32api.keybd_event(0xBE, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放
    sleep(1)
    win32api.keybd_event(0x50, 0, 0, 0)  # p
    win32api.keybd_event(0x50, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放
    sleep(1)
    win32api.keybd_event(0x4E, 0, 0, 0)  # n
    win32api.keybd_event(0x4E, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放
    sleep(1)
    win32api.keybd_event(0x47, 0, 0, 0)  # g
    win32api.keybd_event(0x47, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放
    sleep(1)

    win32api.keybd_event(0x0D, 0, 0, 0)  # enter
    win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放
    sleep(1)
    win32api.keybd_event(0x0D, 0, 0, 0)  # enter
    win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放
    sleep(2)
    # 点击OK
    Function.Base.clickT(self, "xpath", "/html/body/section/main/section/main/div/div/div[1]/main/aside[1]/div/div[3]/div/div[3]/span/button[2]")

    # screenShotName = sys._getframe().f_code.co_name[:]
    # Function.Base.Save_screenshot(self, screenShotName, "case1")
    print("------------debug info--------------上传文件成功")
    logging.debug('上传文件成功')
    sleep(12)
