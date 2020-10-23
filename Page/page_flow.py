# -*- coding:utf-8 -*-
import sys
from time import sleep

import Function.Base
from utils.config import Config
import utils.config
import logging


class Flow:

    def __init__(self, driver, role, branch, node):

        self.role = role
        self.branch = branch
        self.node = node
        self.driver = driver

    def select_branch(self):
        # 寻找Branch
        Function.Base.wait_element(self.driver, "xpath", "/html/body/section/main/section/main/div[1]/div/div/span/span/i")
        Function.Base.clickT(self.driver, "xpath", "/html/body/section/main/section/main/div[1]/div/div/span/span/i")
        sleep(2)
        path = Config(utils.config.CONFIG_BRANCH_PATH).get(self.role)[self.branch]

        Function.Base.clickT(self.driver, "xpath", path)
        logging.debug('role='+self.role+'branch='+self.branch+'path='+path)
        Function.Base.clickT(self.driver, "xpath", path)

    def select_flow(self):
        # 寻找Flow
        sleep(5)
        screen_shot_name = sys._getframe().f_code.co_name[:]
        Function.Base.save_screenshot(self.driver, screen_shot_name)
        path = Config(utils.config.CONFIG_FLOW_PATH).get(self.branch)[self.node]
        # print('branch=' + self.branch + 'flow=' + self.node + 'path=' + path)
        sleep(2)
        Function.Base.clickT(self.driver, "xpath", path)
        sleep(2)


if __name__ == "__main__":
    flow = Flow(111, 222)
    flow.select_branch()
