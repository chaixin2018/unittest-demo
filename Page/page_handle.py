# -*- coding:utf-8 -*-
import sys
from time import sleep

import win32api
import win32con
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import Function.Base
from utils.config import Config
import utils.config
import logging
import Function.delete.Settings


class Handle:

    def __init__(self, driver, branch, node, case_no):

        self.branch = branch
        self.node = node
        self.case_no = case_no
        self.driver = driver

    def begin(self):
        # 点击处理
        path = Config(utils.config.CONFIG_DISPLAY_PATH).get(self.branch)[self.node]["処理"]
        Function.Base.wait_element(self.driver, "xpath", path)
        sleep(2)
        # print("------------debug info--------------Display.py", self.branch, self.node, ",処理 path is", path)
        logging.debug('branch=' + self.branch + 'flow=' + self.node + 'path=' + path)
        Function.Base.clickT(self.driver, "xpath", path)

        # 处理数据 数据格式因为多一个空格而无效
        try:
            Function.Base.wait_element(self.driver, "xpath",
                                       "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[1]/td/div/div/div[2]/div/table/tbody/tr[2]/td/div/div/input")
            if ("無効なフォーマット" == self.driver.find_element_by_xpath(
                    "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[1]/td/div/div/div[2]/div/table/tbody/tr[2]/td/div/small").text):
                sleep(2)
                # self.driver.find_element_by_xpath("/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[1]/td/div/div/div[2]/div/table/tbody/tr[2]/td/div/div/input").click()
                win32api.keybd_event(0x08, 0, 0, 0)  # DEL
                win32api.keybd_event(0x08, 0, win32con.KEYEVENTF_KEYUP, 0)
                # elemTradeNo = self.driver.find_element_by_xpath("/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[1]/td/div/div/div[2]/div/table/tbody/tr[2]/td/div/div/input")
                # elemTradeNo.send_keys(select_date)
            else:
                pass
        except:
            pass

    def finish(self):
        # 点击处理完了
        # 滚轮移动到最下方
        Function.Base.wait_element(self.driver, "xpath", "/html/body/section/main")
        Function.Base.clickT(self.driver, "xpath", "/html/body/section/main")
        # js = "var q=document.documentElement.scrollTop=100000"
        # sleep(1)
        # self.driver.driver.execute_script(js)
        # sleep(5)
        # self.driver.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        # sleep(5)
        #
        for i in range(20):
            self.driver.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            ActionChains(self.driver.driver).key_down(Keys.DOWN).perform()
            sleep(5)
        # Function.Base.wait_element(self.driver, "xpath", "/html/body/section/main")
        # Function.Base.click(self.driver, "xpath", "/html/body/section/main")
        # win32api.keybd_event(0x11, 0, 0, 0)  # Ctrl
        # sleep(1)
        # win32api.keybd_event(0x23, 0, 0, 0)  # End
        # sleep(1)
        # win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)  # Ctrl释放
        # win32api.keybd_event(0x23, 0, win32con.KEYEVENTF_KEYUP, 0)  # End释放
        # sleep(1)

        Function.Base.wait_element(self.driver, "xpath",
                                   "/html/body/section/main/section/main/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[2]/div[1]/div/button")
        Function.Base.clickT(self.driver, "xpath",
                            "/html/body/section/main/section/main/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[2]/div[1]/div/button")
        sleep(2)



        screen_shot_name = sys._getframe().f_code.co_name[:]
        Function.Base.save_screenshot(self.driver, screen_shot_name)
        # 点击ok
        Function.Base.clickT(self.driver, "xpath", "//*[@id='printTest1']/div/div/div[2]/div/div[5]/div/div[2]/div/button[2]")
        # 选择処理待ち
        sleep(8)
        Function.Base.wait_element(self.driver, "xpath", "/html/body/section/header/div/div[4]/ul/li[1]")
        Function.Base.clickT(self.driver, "xpath", "/html/body/section/header/div/div[4]/ul/li[1]")
        sleep(2)

    def upload(self):
        # 点击+
        Function.Base.wait_element(self.driver, "xpath",
                                   "/html/body/section/main/section/main/div/div/div[1]/main/aside[1]/div/div[7]/div/div/div[1]/span/i")
        Function.Base.clickT(self.driver, "xpath",
                            "/html/body/section/main/section/main/div/div/div[1]/main/aside[1]/div/div[7]/div/div/div[1]/span/i")
        # 点击文件名
        Function.Base.wait_element(self.driver, "xpath",
                                   "/html/body/section/main/section/main/div/div/div[1]/main/aside[1]/div/div[3]/div/div[2]/div[3]/div")
        Function.Base.clickT(self.driver, "xpath",
                            "/html/body/section/main/section/main/div/div/div[1]/main/aside[1]/div/div[3]/div/div[2]/div[3]/div")
        sleep(1)
        Function.Base.clickT(self.driver, "xpath", "/html/body/div[2]/div[1]/div[1]/ul/li[24]/span")

        # 选择主副
        Function.Base.clickT(self.driver, "xpath",
                            "/html/body/section/main/section/main/div/div/div[1]/main/aside[1]/div/div[3]/div/div[2]/div[4]/div")
        sleep(1)
        Function.Base.clickT(self.driver, "xpath", "/html/body/div[3]/div[1]/div[1]/ul/li[2]")

        # 上传文件
        Function.Base.clickT(self.driver, "xpath",
                            "/html/body/section/main/section/main/div/div/div[1]/main/aside[1]/div/div[3]/div/div[2]/div[1]/div/button/span")

        sleep(2)
        win32api.keybd_event(0x31, 0, 0, 0)  # 1
        win32api.keybd_event(0x31, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放
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
        Function.Base.clickT(self.driver, "xpath",
                            "/html/body/section/main/section/main/div/div/div[1]/main/aside[1]/div/div[3]/div/div[3]/span/button[2]")

        # screenShotName = sys._getframe().f_code.co_name[:]
        # Function.Base.Save_screenshot(self, screenShotName, "case1")
        print("------------debug info--------------上传文件成功")
        logging.debug('上传文件成功')
        sleep(12)

    def select_set(self):
        # 以下部分，会因为进入的分支不同而操作不同
        if self.branch == "営業点検" and self.node == "営業点検":
            Function.delete.Settings.business_check1(self.driver)
        elif self.branch == "火災" and self.node == "点検1回目":
            Function.delete.Settings.fire_spot_check1(self.driver)
        elif self.branch == "bank" and self.node == "営業点検":
            Function.delete.Settings.bank_business_check(self.driver)
