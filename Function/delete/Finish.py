import sys
from time import sleep

import Function.Base


def finish(self):
    # 点击处理完了
    Function.Base.wait_element(self, "xpath", "/html/body/section/main/section/main/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[2]/div[1]/div/button")
    Function.Base.clickT(self, "xpath", "/html/body/section/main/section/main/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[2]/div[1]/div/button")
    sleep(2)
    screen_shot_name = sys._getframe().f_code.co_name[:]
    Function.Base.save_screenshot(self, screen_shot_name)
    # 点击ok
    Function.Base.clickT(self, "xpath", "//*[@id='printTest1']/div/div/div[2]/div/div[5]/div/div[2]/div/button[2]")
    # 选择処理待ち
    sleep(8)
    Function.Base.wait_element(self, "xpath", "/html/body/section/header/div/div[4]/ul/li[1]")
    Function.Base.clickT(self, "xpath", "/html/body/section/header/div/div[4]/ul/li[1]")
    sleep(2)
