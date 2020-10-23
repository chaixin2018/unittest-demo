# -*- coding:utf-8 -*-
from time import sleep

import Function.Base
from utils.config import Config
import utils.config
import logging


def select_branch(self, role, branch):
    # 点击下拉框
    # 寻找Branch
    Function.Base.wait_element(self, "xpath", "/html/body/section/main/section/main/div[1]/div/div/span/span/i")
    Function.Base.clickT(self, "xpath", "/html/body/section/main/section/main/div[1]/div/div/span/span/i")
    sleep(2)
    path = Config(utils.config.CONFIG_BRANCH_PATH).get(role)[branch]
    Function.Base.clickT(self, "xpath", path)
    # print("------------debug info--------------branch.py", role, branch, ",branch path is", path)
    logging.debug('role='+role+'branch='+branch+'path='+path)
    Function.Base.clickT(self, "xpath", path)