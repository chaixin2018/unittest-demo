import sys
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import Function.Base
import Function.Login
import Function.Logout
import Function.delete.Flow
import Function.delete.Finish
import logging

import utils
from Page.page_flow import Flow
from Page.page_handle import Handle
from Page.page_overview import Overview
from utils.config import Config


class StepBase():
    def __init__(self, driver, role, branch, node, case_no):
        self.branch = branch
        self.node = node
        self.case_no = case_no
        self.driver = driver
        self.role = role

    def step_begin(self):
        # 登录
        print("------------debug info--------------" + self.branch + " " + self.node + "---开始")
        Function.Login.login_action(self.driver, role=self.role)
        # 选择流程节点
        flow = Flow(driver=self.driver, role=self.role, branch=self.branch, node=self.node)
        if self.role == "admin":
            flow.select_branch()
        flow.select_flow()
        # 进入一览界面，输入检索内容
        overview = Overview(driver=self.driver, branch=self.branch, node=self.node, case_no=self.case_no)
        overview.select_display()
        flag = overview.have_data_check()

        # 点击处理，进入处理流程
        if flag:
            handle = Handle(driver=self.driver, branch=self.branch, node=self.node, case_no=self.case_no)
            handle.begin()
            # 无论什么分支，最后都执行退出流程
            handle.finish()  # 处理完成
            Function.Logout.logout(self.driver)
        print("------------debug info--------------" + self.branch + " " + self.node + "---结束")
        logging.debug('branch=' + self.branch + 'flow=' + self.node + '------结束-----')

    def step_begin72(self):
        # 登录
        Function.Login.login_action(self.driver, role=self.role)
        # 选择流程节点
        print("------------debug info--------------" + self.branch + " " + self.node + "---开始")
        flow = Flow(driver=self.driver, role=self.role, branch=self.branch, node=self.node)
        if self.role == "admin":
            flow.select_branch()
        flow.select_flow()

        try:
            # 进入一览界面，输入检索内容
            Function.Base.wait_element(self.driver, "xpath",
                                "/html/body/section/main/div/section/main/div[1]/div/div[1]/div/div[1]/div")
            Function.Base.clickT(self.driver, "xpath", "/html/body/section/main/div/section/main/div[1]/div/div[1]/div/div[1]/div")
            sleep(2)
            # 设置鼠标滚动的开始点
            Function.Base.wait_element(self.driver, "xpath", "/html/body/section/main/div/section/main/div[2]/div[3]/table/tbody/tr[1]/td[3]")
            Function.Base.clickT(self.driver, "xpath", "/html/body/section/main/div/section/main/div[2]/div[3]/table/tbody/tr[1]/td[3]")
            # 设置鼠标滚动的结束点
            for i in range(200):
                self.driver.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                ActionChains(self.driver.driver).key_down(Keys.RIGHT).perform()
            sleep(3)

            screen_shot_name = sys._getframe().f_code.co_name[:]
            Function.Base.save_screenshot(self.driver, screen_shot_name)

            self.driver.assertTrue("備考欄" in self.driver.driver.page_source)

            for i in range(200):
                self.driver.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                ActionChains(self.driver.driver).key_down(Keys.LEFT).perform()
            sleep(3)

        except:
            pass

        overview = Overview(driver=self.driver, branch=self.branch, node=self.node, case_no=self.case_no)
        flag = overview.have_data_check()
        if flag:
            # 按照受付日排序
            path = Config(utils.config.CONFIG_DISPLAY_PATH).get(self.branch)[self.node]["sort"]
            Function.Base.wait_element(self.driver, "xpath", path)
            Function.Base.clickT(self.driver, "xpath", path)
            # 点击处理按钮
            sleep(2)
            path = Config(utils.config.CONFIG_DISPLAY_PATH).get(self.branch)[self.node]["処理"]
            Function.Base.wait_element(self.driver, "xpath", path)
            Function.Base.clickT(self.driver, "xpath", path)
            sleep(2)
            # 滑动到底部，截图
            sleep(2)
            Function.Base.wait_element(self.driver, "xpath", "/html/body/section/main/section/main/div/div/div[1]/div/span/span[3]")
            Function.Base.clickT(self.driver, "xpath", "/html/body/section/main/section/main/div/div/div[1]/div/span/span[3]")
            sleep(1)
            # 滑动到最底部
            Function.Base.wait_element(self.driver, "xpath",
                                       "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody[1]/tr[3]/td")
            Function.Base.clickT(self.driver, "xpath",
                                "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody[1]/tr[3]/td")
            sleep(1)
            for i in range(200):
                self.driver.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                ActionChains(self.driver.driver).key_down(Keys.DOWN).perform()

            # 滑动到处理完了
            Function.Base.wait_element(self.driver, "xpath", "/html/body/section/main/section/main/div/div/div[2]/div[1]/div/div[1]/span")
            Function.Base.clickT(self.driver, "xpath", "/html/body/section/main/section/main/div/div/div[2]/div[1]/div/div[1]/span")
            sleep(1)
            get_elem = self.driver.driver.find_element_by_xpath("/html/body/section/main/section/main/div/div/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[2]/div[1]/div/button")
            self.driver.driver.execute_script("arguments[0].focus();", get_elem)
            for i in range(5):
                self.driver.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                ActionChains(self.driver.driver).key_down(Keys.UP).perform()
            sleep(3)

            screen_shot_name = sys._getframe().f_code.co_name[:]
            Function.Base.save_screenshot(self.driver, screen_shot_name)
            # 增加断言
            try:
                self.driver.assertTrue("備考欄" in self.driver.driver.page_source)
            except:
                pass

            # 点击返回
            self.driver.driver.back()
            # 点击详细按钮
            path = Config(utils.config.CONFIG_DISPLAY_PATH).get(self.branch)[self.node]["詳細"]
            Function.Base.wait_element(self.driver, "xpath", path)
            Function.Base.clickT(self.driver, "xpath", path)
            # 滑动到底部，截图
            sleep(2)
            Function.Base.wait_element(self.driver, "xpath",
                                       "/html/body/section/main/section/main/div/div/div[1]/div/span/span[3]")
            Function.Base.clickT(self.driver, "xpath",
                                "/html/body/section/main/section/main/div/div/div[1]/div/span/span[3]")
            sleep(1)
            Function.Base.wait_element(self.driver, "xpath",
                                       "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody[1]/tr[3]/td")
            Function.Base.clickT(self.driver, "xpath",
                                "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody[1]/tr[3]/td")
            sleep(1)
            for i in range(200):
                self.driver.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                ActionChains(self.driver.driver).key_down(Keys.DOWN).perform()

            screen_shot_name = sys._getframe().f_code.co_name[:]
            Function.Base.save_screenshot(self.driver, screen_shot_name)
            # 增加断言
            self.driver.assertTrue("備考欄" in self.driver.driver.page_source)

            # 点击返回
            self.driver.driver.back()

        print("------------debug info--------------" + self.branch + " " + self.node + "---结束")
        logging.debug('branch=' + self.branch + 'flow=' + self.node + '------结束-----')


class StepFire(StepBase):
    pass


class StepFire2(StepBase):
    pass

