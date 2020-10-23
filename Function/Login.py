import sys
from time import sleep

from Function import *
import utils
from utils.config import Config
from config.global_setting import *
# from Function.Logout import *
# import Function.Logout
from Function import Logout


def login_action(self, role):
	sleep(5)
	if "ログイン" == self.driver.find_element_by_xpath("//*[@id='bs-example-navbar-collapse-1']/ul[2]/li[3]/a").text:
		login_daido(self, role)
	else:
		Logout.logout(self)
		login_daido(self, role)


def login_daido(self, role):
	Base.clickT(self, "xpath", '//*[@id="bs-example-navbar-collapse-1"]/ul[2]/li[3]/a')
	sleep(3)
	user = Config(utils.config.CONFIG_LOGIN).get('user')[role]
	password = Config(utils.config.CONFIG_LOGIN).get('password')[role]

	elem_user = self.driver.find_element_by_xpath('//*[@id="username"]')
	elem_user.send_keys(user)
	elem_pwd = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[2]/div/input')
	elem_pwd.send_keys(password)

	Base.result_action(self, sys._getframe().f_code.co_name[:], result_setting)

	# self.driver.driver.find_element_by_xpath("//*[text()='ログイン']").click()
	sleep(5)
	Base.clickT(self, "xpath", "//*[@id='loginForm']/div[7]/div/button")
	Base.wait_element(self, "xpath", '//*[@id="bs-example-navbar-collapse-1"]/ul[2]/li[3]/a')
	print("------------debug info-------Login信息", "user", user, "password", password, "login成功")
