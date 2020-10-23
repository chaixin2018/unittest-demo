import sys
from time import sleep
from Function import *
from config.global_setting import *
from selenium.webdriver.support.ui import Select


def service_select(self):
    # Base.wait_element(self, "xpath", "/html/body/div[4]/div[4]/div[1]")
    Base.clickT(self, "xpath", "/html/body/div[4]/div[4]/div[1]")
    # 业种
    # Base.clickT(self, "xpath", "//*[@id='business_types']")
    s1 = Select(self.driver.find_element_by_xpath("//*[@id='business_types']"))
    s1.select_by_index("1")
    # sleep(5)
    # s1.select_by_visible_text("製造業")
    # sleep(5)
    # s1.select_by_value("IT")
    # sleep(5)

    # 遍历下拉框内容
    # 如果value_text与下拉框所有遍历后内容一致，则返回选项内容校验正确，否则返回选项内容校验正确
    # value_text写法：从第一个依次写，每个选项用， 分割，最后一个后面需要， 举例"製造業, 卸売業, 小売業, IT, "
    Base.option_value_check(self, "//*[@id='business_types']", "option", "製造業, 卸売業, 小売業, IT, ")
    # 验证某一个下拉框内容是否存在并选中
    Base.is_option_value_present(self, "//*[@id='business_types']", "option", "卸売業")

    # Base.clickT(self, "xpath", "//*[@id='business_types']/option[1]")
    # 职位
    Base.clickT(self, "xpath", "//*[@id='position']")
    Base.clickT(self, "xpath", "//*[@id='position']/option[1]")
    # 从业人员
    Base.clickT(self, "xpath", "//*[@id='scale']")
    Base.clickT(self, "xpath", "//*[@id='scale']/option[1]")
    # 问题点
    Base.clickT(self, "xpath", "//*[@id='catalog']")
    Base.clickT(self, "xpath", "//*[@id='catalog']/option[1]")

    # 下五项按钮
    Base.clickT(self, "xpath", "/html/body/div[4]/div[2]/form/div[5]/div/button")

    Base.clickT(self, "xpath", "/html/body/div[4]/div[1]/form/div[2]/div/div[2]/label/span")
    Base.clickT(self, "xpath", "/html/body/div[4]/div[1]/form/div[3]/div/div[3]/label/span")
    Base.clickT(self, "xpath", "/html/body/div[4]/div[1]/form/div[4]/div/div[4]/label/span")
    Base.clickT(self, "xpath", "/html/body/div[4]/div[1]/form/div[5]/div/div[2]/label/span")
    Base.clickT(self, "xpath", "/html/body/div[4]/div[1]/form/div[6]/div/div[3]/label/span")
    Base.result_action(self, sys._getframe().f_code.co_name[:], result_setting)
    Base.clickT(self, "xpath", "/html/body/div[4]/div[1]/form/div[7]/div/button")
    # 下五项按钮


def service_result(self):
    # 详细
    # Base.wait_element(self, "xpath", "/html/body/div[4]/div/ul/li[4]/div[2]/div[2]/h4/a")
    Base.clickT(self, "xpath", "/html/body/div[4]/div/ul/li[4]/div[2]/div[2]/h4/a")
    Base.result_action(self, sys._getframe().f_code.co_name[:], result_setting)
    # Base.wait_element(self, "xpath", "/html/body/div[4]/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/button[2]")
    Base.clickT(self, "xpath", "/html/body/div[4]/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/button[2]")
    sleep(5)
    # 这里需要手动加入延时，因为find_element_by_xpath函数没有等待，界面find不到会报错
    self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/textarea").send_keys("123text")
    Base.result_action(self, sys._getframe().f_code.co_name[:], result_setting)
    Base.clickT(self, "xpath", "/html/body/div[5]/div/div/div[3]/button[2]")