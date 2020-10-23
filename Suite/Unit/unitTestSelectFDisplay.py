from selenium import webdriver
import unittest
from time import sleep
import Function.Base
import Function.Login
import Function.Logout
import Function.delete.Branch
import Function.delete.Flow
import Function.delete.Display

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://rakuten-sonpo-stg.comitx.co.jp/jimu/front/home")  # rakuten

    def test001(self):
        # Function.Login.loginRA(self,"火災ユーザー")
        # Function.Branch.selectBranch(self, "火災ユーザー", "火災")
        # Function.Flow.selectFlow(self,  "火災","spotCheck1")
        # Function.Display.selectDisplay(self,"火災","spotCheck1")
        # Function.Logout.logout(self)

        Function.Login.login_action(self, "businuessRole1")
        Function.delete.Branch.select_branch(self, "businuessRole1", "営業点検")
        Function.delete.Flow.select_flow(self, "営業点検", "問合せ回答")
        Function.delete.Display.select_display(self, "営業点検", "問合せ回答")
        Function.Logout.logout(self)


    def tearDown(self):
        sleep(5)
        Function.Logout.logout(self)


    @classmethod
    # 全部套件执行完
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()