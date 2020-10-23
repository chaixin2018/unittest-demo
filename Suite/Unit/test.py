from selenium import webdriver
import unittest
from time import sleep
import Function.Base
import Function.Login
import Function.Logout

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        #cls.driver.get("http://20.20.89.165/front/")   # sony
        cls.driver.get("https://rakuten-sonpo-stg.comitx.co.jp/jimu/front/home")  # rakuten

    def test001(self):
        Function.Login.login_action(self, "admin")

    # def test002(self):
    #     Case.fire1.step(self)
    # def test003(self):
    #     Case.fire1.step(self)

    def tearDown(self):
        sleep(10)

        Function.Logout.logout(self)
        # Function.common.Click(self, "xpath", "/html/body/section/header/div/div[5]/div/span/i")
        # #Function.common.Click(self, "xpath", "//*[@id='dropdown-menu-4822']/li[3]")
        #
        # Function.common.wait_element(self, "xpath", "//body/ul/li[3]")
        # sleep(1)
        # Function.common.Click(self, "xpath", "//body/ul/li[3]")


    @classmethod
    # 全部套件执行完
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()


# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     tests=[Test('test001')]
#     suite.addTests(tests)
#
#     path = os.path.abspath('') + '\Report'
#     #print(path)
#     os.chdir(path)
#     time = (time.strftime("%m%d-%H%M", time.localtime()))
#     filename = 'TestReport' + time + '.html'
#
#     fr = open(filename, 'wb')  # 无文件时创建
#     report = HTMLTestRunner.HTMLTestRunner(stream=fr, title='TestReport', description='')
#     report.run(suite)
#     fr.close()
#
#
