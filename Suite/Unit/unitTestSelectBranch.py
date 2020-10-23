from selenium import webdriver
import unittest
from time import sleep
import Function.Base
import Function.Login
import Function.Logout
import Function.delete.Branch

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://rakuten-sonpo-stg.comitx.co.jp/jimu/front/home")  # rakuten

    def test001(self):
        Function.Login.login_action(self, "火災ユーザー")
        Function.delete.Branch.select_branch(self, "火災ユーザー", "火災")
        Function.Logout.logout(self)

        Function.Login.login_action(self, "admin")
        Function.delete.Branch.select_branch(self, "admin", "hurt")
        Function.Logout.logout(self)

        Function.Login.login_action(self, "日本代行ユーザー1")
        Function.delete.Branch.select_branch(self, "日本代行ユーザー1", "日本代行")

    def tearDown(self):
        sleep(5)
        Function.Logout.logout(self)


    @classmethod
    # 全部套件执行完
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()