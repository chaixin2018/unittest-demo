import os
import sys
from HTMLTestRunner import HTMLTestRunner

import selenium
from selenium import webdriver
import unittest

from Function import *
from Case import *
import time
from config.global_setting import *


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        # 有代理的情况，且代理需要密码
        # proxy = 'test001:123qwe.com@172.16.0.5:3128'
        # cls.driver = Function.Getproxy.get_driver(proxy)
        # cls.driver.get("http://platform1.comitbpm.com/")
        # cls.driver.implicitly_wait(10)  # 隐式等待10秒

        # 无代理情况
        #cls.driver = selenium.webdriver.Chrome()
        cls.driver = selenium.webdriver.Firefox()
        #cls.driver = selenium.webdriver.Ie()
        cls.driver.get("http://daido.sitetest1.com/")
        cls.driver.maximize_window()

        # 有代理，代理无密码
        # chromeOptions = webdriver.ChromeOptions()  # 设置代理
        # chromeOptions.add_argument("--proxy-server=http://192.168.116.141:808")
        # # cls.driver=webdriver.Chrome(chrome_options=chromeOptions)
        # cls.driver = webdriver.Chrome()  #不适用代理
        # cls.driver.maximize_window()
        # cls.driver.get("http://platform1.comitbpm.com/")  # rakuten

    def test_login_daido1(self):
        Base.set_func_name(sys._getframe().f_code.co_name[:])
        Base.set_suite_name("login_suite")
        LoginCase.login_daido1(self)


    def test_login_daido2(self):
        Base.set_func_name(sys._getframe().f_code.co_name[:])
        Base.set_suite_name("login_suite")
        LoginCase.login_daido2(self)

    def test_login_daido3(self):
        Base.set_func_name(sys._getframe().f_code.co_name[:])
        Base.set_suite_name("login_suite")
        LoginCase.login_daido3(self)
        try:
            Base.close_file("XLMAIN", "Microsoft Excel - test_evidence.xlsx")
        except:
            pass

    def test_service_recommend1(self):
        Base.set_func_name(sys._getframe().f_code.co_name[:])
        Base.set_suite_name("service_recommend_suite")
        LoginCase.login_admin(self)
        service_recommend.service_select(self)
        # service_recommend.service_result(self)
        try:
            Base.close_file("XLMAIN", "Microsoft Excel - test_evidence.xlsx")
        except:
            pass

    def test_needs_recommend1(self):
        Base.set_func_name(sys._getframe().f_code.co_name[:])
        Base.set_suite_name("needs_recommend_suite")
        LoginCase.login_admin(self)
        needs_recommend.needs_select(self)
        needs_recommend.needs_result(self)

    def tearDown(self):
        # try:
        #     Base.close_file("XLMAIN", "Microsoft Excel - test_evidence.xlsx")
        # except:
        #     pass
        pass
        # sleep(1)
        # Logout.logout(self)

    @classmethod
    # 全部套件执行完
    def tearDownClass(cls):
        cls.driver.quit()
        # 关闭操作的保存evidence的文件夹
        try:
            Base.close_file("XLMAIN", "Microsoft Excel - test_evidence.xlsx")
        except:
            print("沒有需要关闭的文件")


if __name__ == '__main__':
    Base.create_report()
    unittest.main()

#     suite = unittest.TestSuite()
#     login_suite = [Test('login_daido1'), Test('login_daido2'), Test('login_daido3')]
#     service_recommend_suite = [Test('service_recommend1')]
#     needs_recommend_suite = [Test('needs_recommend1')]
#     suite.addTests(login_suite)
#
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     login_suite = [Test('login_daido1'), Test('login_daido2'), Test('login_daido3')]
#     service_recommend_suite = [Test('service_recommend1')]
#     needs_recommend_suite = [Test('needs_recommend1')]
#     # tests = login_suite + service_recommend_suite + needs_recommend_suite
#     # tests = service_recommend_suite
#     # tests = [Test('test001')]
#     # suite.addTests(tests)
#
#     # 创建suite文件夹
#     Base.create_report()
#     # time = time.strftime("%Y%m%d-%H%M", time.localtime())
#     # file = 'TestReport' + time
#     # Base.set_report_name(file)
#     # path = Base.get_base_path() + '\\Report\\'
#     # os.makedirs(path + file)
#     # os.chdir(path + file)
#
#     # suite.addTests(login_suite)
#     suite.addTests(service_recommend_suite)
#     # suite.addTests(needs_recommend_suite)
#
#
#     filename = 'TestReport' + time.strftime("%Y%m%d-%H%M", time.localtime()) + '.html'
#     fr = open(filename, 'wb')  # 无文件时创建
#
#     # runner = unittest.TextTestRunner()
#     # BeautifulReport(suite).report(filename=filename, description='接口测试')
#     # runner.run(suite)
#
#     report = HTMLTestRunner(stream=fr, title='TestReport', description='')
#     report.run(suite)
#
#     fr.close()
#
#
