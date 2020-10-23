# -*- coding:utf-8 -*-
from time import sleep

import win32con
import Function.Base
import win32api
# import win32con
from utils.config import Config
import utils.config
import logging


def select_display(self, branch, flow, case_no):
    select_date = Config(utils.config.CONFIG_DATA).get(case_no)
    # 点击检索
    Function.Base.wait_element(self, "xpath",
                               "/html/body/section/main/div/section/main/div[1]/div/div[1]/div/div[1]/div")
    Function.Base.clickT(self, "xpath", "/html/body/section/main/div/section/main/div[1]/div/div[1]/div/div[1]/div")
    # 选中证券号输入框
    path = Config(utils.config.CONFIG_DISPLAY_PATH).get(branch)[flow]["証券番号"]
    Function.Base.wait_element(self, "xpath", path)
    Function.Base.clickT(self, "xpath", path)
    # 输入证券号
    elem_select_date = self.driver.find_element_by_xpath(path)
    elem_select_date.send_keys(select_date)

    # 点击检索按钮
    path = Config(utils.config.CONFIG_DISPLAY_PATH).get(branch)[flow]["検索"]
    Function.Base.wait_element(self, "xpath", path)
    # print("------------debug info--------------Display.py",branch,flow,",検索 path is",path)
    logging.debug('branch=' + branch + 'flow=' + flow + 'path=' + path)
    Function.Base.clickT(self, "xpath", path)
    sleep(5)


def handle(self, branch, flow, caseNo):
    # 点击处理
    path = Config(utils.config.CONFIG_DISPLAY_PATH).get(branch)[flow]["処理"]
    Function.Base.wait_element(self, "xpath", path)
    sleep(2)
    # print("------------debug info--------------Display.py", branch, flow, ",処理 path is",path)
    logging.debug('branch=' + branch + 'flow=' + flow + 'path=' + path)
    Function.Base.clickT(self, "xpath", path)

    # 处理数据 数据格式因为多一个空格而无效
    try:
        Function.Base.wait_element(self, "xpath", "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[1]/td/div/div/div[2]/div/table/tbody/tr[2]/td/div/div/input")
        if ("無効なフォーマット" == self.driver.find_element_by_xpath("/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[1]/td/div/div/div[2]/div/table/tbody/tr[2]/td/div/small").text):
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


