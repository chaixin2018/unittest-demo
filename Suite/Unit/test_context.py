from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")  # rakuten
sleep(10)

# if ("抗击肺炎111" in driver.page_source):
#     print("------------debug info--------------前处理1---没有检索到数据")
driver.quit()