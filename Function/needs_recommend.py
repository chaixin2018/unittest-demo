import sys
from time import sleep
from Function import *
from config.global_setting import *


def needs_select(self):
    # 选择needs—recommend
    # Base.wait_element(self, "xpath", "/html/body/div[4]/div[4]/div[3]")
    Base.clickT(self, "xpath", "/html/body/div[4]/div[4]/div[3]")

    # 各个项目选择
    # Base.wait_element(self, "xpath", "//*[@id='businesstype']/option[2]")
    Base.clickT(self, "xpath", "//*[@id='businesstype']/option[4]")
    Base.clickT(self, "xpath", "/html/body/div[4]/div/form/div[2]/div/select/option[2]")
    Base.clickT(self, "xpath", "/html/body/div[4]/div/form/div[3]/div/select/option[2]")
    Base.clickT(self, "xpath", "/html/body/div[4]/div/form/div[4]/div/select/option[2]")
    Base.clickT(self, "xpath", "/html/body/div[4]/div/form/div[5]/div/select/option[2]")
    Base.clickT(self, "xpath", "/html/body/div[4]/div/form/div[6]/div/select/option[2]")
    Base.result_action(self, sys._getframe().f_code.co_name[:], result_setting)
    # 点击登录按钮
    Base.clickT(self, "xpath", "/html/body/div[4]/div/form/div[7]/div/button")

def needs_result(self):
    # 会社を見る
    # Base.wait_element(self, "xpath", "/html/body/div[4]/div/ul/li[1]/div[2]/div[2]/h4/a")
    Base.clickT(self, "xpath", "/html/body/div[4]/div/ul/li[1]/div[2]/div[2]/h4/a")
    Base.result_action(self, sys._getframe().f_code.co_name[:], result_setting)