# -*- coding:utf-8 -*-
from time import sleep

import Function.Base
from utils.config import Config
import utils.config
import logging


class Overview:

    def __init__(self, driver, branch, node, case_no):

        self.branch = branch
        self.node = node
        self.case_no = case_no
        self.driver = driver

    def select_display(self):
        # Function.Base.wait_element(self.driver, "xpath", "/html/body/section/main")
        # Function.Base.click(self.driver, "xpath", "/html/body/section/main")
        # sleep(1)
        # win32api.keybd_event(0x11, 0, 0, 0)  # Ctrl
        # win32api.keybd_event(0x23, 0, 0, 0)  # End
        # win32api.keybd_event(0x23, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放
        # win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放
        # sleep(1)
        # print("结束")


        select_date = Config(utils.config.CONFIG_DATA).get(self.case_no)
        # 点击检索
        Function.Base.wait_element(self.driver, "xpath",
                                   "/html/body/section/main/div/section/main/div[1]/div/div[1]/div/div[1]/div")
        Function.Base.clickT(self.driver, "xpath", "/html/body/section/main/div/section/main/div[1]/div/div[1]/div/div[1]/div")
        # 选中证券号输入框
        path = Config(utils.config.CONFIG_DISPLAY_PATH).get(self.branch)[self.node]["証券番号"]
        Function.Base.wait_element(self.driver, "xpath", path)
        Function.Base.clickT(self.driver, "xpath", path)
        # 输入证券号
        elem_select_date = self.driver.driver.find_element_by_xpath(path)
        elem_select_date.send_keys(select_date)

        # 点击检索按钮
        path = Config(utils.config.CONFIG_DISPLAY_PATH).get(self.branch)[self.node]["検索"]
        Function.Base.wait_element(self.driver, "xpath", path)
        # print("------------debug info--------------Display.py", self.branch, self.node, ",検索 path is", path)
        logging.debug('branch=' + self.branch + 'flow=' + self.node + 'path=' + path)
        Function.Base.clickT(self.driver, "xpath", path)
        sleep(3)


    def have_data_check(self):
        flag = 1
        try:
            if "データなし" == self.driver.driver.find_element_by_xpath(
                    "/html/body/section/main/div/section/main/div[2]/div[3]/div/span").text:
                print("------------debug info--------------" + self.branch + " " + self.node + "---没有找到数据")
                logging.warning('branch=' + self.branch + 'flow=' + self.node + '没有找到数据')
                flag = 0
        except:
            pass
        finally:
            logging.debug('branch=' + self.branch + 'flow=' + self.node + '------结束-----')
            return flag






if __name__ == "__main__":
    overview = Overview(111, 222)
    overview.select_display()
