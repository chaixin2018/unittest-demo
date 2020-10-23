# coding=utf-8
import logging
import time
from selenium import webdriver
print("123")
driver = webdriver.Chrome()
logging.info("123")
print("123")
time.sleep(1)
driver.maximize_window()
driver.get("https://www.baidu.com")
time.sleep(1)


driver.get_screenshot_as_file("C:\\Users\\chaixin\\Desktop\\baidu.png")
driver.quit()