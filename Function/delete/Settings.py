from time import sleep
import Function.Base


def fire_spot_check1(self):
    # 个别设置
    Function.Base.wait_element(self, "xpath",
                        "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[6]/td/div/div/label[2]/span[1]/span")
    # 未集计
    Function.Base.clickT(self, "xpath",
                        "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[6]/td/div/div/label[2]/span[1]/span")
    sleep(2)
    # リビングアシスト
    Function.Base.clickT(self, "xpath",
                        "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[8]/td/div/div/label[1]/span[1]/span")
    # 口振连携选中要
    Function.Base.clickT(self, "xpath",
                        "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[13]/td/div/div/label[2]/span[1]/span")

    # 返金・解約「要」を選択
    Function.Base.clickT(self, "xpath",
                        "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[18]/td/div/div/label[1]/span[1]/span")
    # 至急返金
    # Function.common.Click(self, "xpath",
    #                      "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[19]/td/div/div/label[2]/span[1]/span")
    # 点検2回目
    Function.Base.clickT(self, "xpath",
                        "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[23]/td/div/div/label[2]/span[1]/span")


def fire_spot_check2(self):
    # 个别设置
    Function.Base.wait_element(self, "xpath",
                        "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[6]/td/div/div/label[2]/span[1]/span")
    # 未集计
    Function.Base.clickT(self, "xpath",
                        "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[6]/td/div/div/label[2]/span[1]/span")
    sleep(2)
    # リビングアシスト
    Function.Base.clickT(self, "xpath",
                        "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[8]/td/div/div/label[3]/span[1]/span")
    Function.Base.clickT(self, "xpath",
                        "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[13]/td/div/div/label[1]/span[1]/span")
    # 返金・解約「要」を選択
    Function.Base.clickT(self, "xpath",
                        "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[18]/td/div/div/label[1]/span[1]/span")
    # 至急返金
    # Function.common.Click(self, "xpath",
    #                      "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[19]/td/div/div/label[2]/span[1]/span")
    # 点検2回目
    Function.Base.clickT(self, "xpath", "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[23]/td/div/div/label[1]/span[1]/span")


def business_check1(self):
    Function.Base.wait_element(self, "xpath",
                        "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[7]/td/div/div/label[2]/span[2]")
    sleep(2)
    Function.Base.clickT(self, "xpath",
                        "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[7]/td/div/div/label[2]/span[2]")
    Function.Base.clickT(self, "xpath",
                        "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[7]/td/div/div/label[2]/span[2]")
    sleep(5)


def bank_business_check(self):
    # バッチ計上送付帳票選択=要
    Function.Base.wait_element(self, "xpath",
                                   "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[2]/td/div/div/div[2]/div/div/div[2]/div[1]/table/tbody/tr[6]/td/div/div/label/span[1]/span")
    Function.Base.clickT(self, "xpath",
                              "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[2]/td/div/div/div[2]/div/div/div[2]/div[1]/table/tbody/tr[6]/td/div/div/label/span[1]/span")

    sleep(1)
    # 計上方式 = バッチ計上（事務センターコーディング）
    Function.Base.clickT(self, "xpath",
                            "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[30]/td/div/div/label[4]/span[2]")
    # 保険種目 =？
    Function.Base.clickT(self, "xpath",
                            "/html/body/section/main/section/main/div/div/div[1]/main/aside[2]/div/form/div/table/tbody/tr[32]/td/div/div/div/input")
    sleep(1)
    Function.Base.clickT(self, "xpath", "/html/body/div/div[1]/div[1]/ul/li[1]/span")
    sleep(3)
