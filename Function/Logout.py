import sys
from time import sleep
from Function import *
from config.global_setting import *


def logout(self):
    # 如果已经在登出界面，则直接pass
    sleep(3)
    # Base.wait_element(self, "xpath", '//*[@id="bs-example-navbar-collapse-1"]/ul[2]/li[3]/a')
    Base.clickT(self, "xpath", '//*[@id="bs-example-navbar-collapse-1"]/ul[2]/li[3]/a')
    # try:
    #     Function.Base.wait_element(self, "xpath", '//*[@id="bs-example-navbar-collapse-1"]/ul[2]/li[3]/a')
    #     Function.Base.click(self, "xpath", '//*[@id="bs-example-navbar-collapse-1"]/ul[2]/li[3]/a')
    # except:
    #     # Function.Base.wait_element(self, "xpath","/html/body/section/main/section/main/div/div/div[2]/"
    #     #                                          "div/div[2]/table/tbody/tr[3]/td[2]/div[1]/div/button")
    #     # Function.Base.click(self, "xpath","/html/body/section/main/section/main/div/"
    #     #                                   "div/div[2]/div/div[2]/table/tbody/tr[3]/td[2]/div[1]/div/button")
    #     # sleep(2)
    #     pass

    print("------------debug info-------用户登出-------")
