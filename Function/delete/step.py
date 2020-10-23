import Function.Base
import Function.Login
import Function.Logout
import Function.delete.Branch
import Function.delete.Flow
import Function.delete.Display
import Function.delete.Upload
import Function.delete.Finish
import Function.delete.Settings
import logging


class Step:
    """操作excel"""

    def __init__(self, role=None, branch=None, flow=None, case_no=None):
        pass

    def step(self, role, branch, flow, case_no):
        logging.debug(branch+flow)
        print("------------debug info--------------"+branch+" "+flow+"---开始")
        logging.debug('branch=' + branch + 'flow=' + flow + '-----开始-----')
        Function.Login.login_action(self, role)
        if role == "admin":
            Function.delete.Branch.selectBranch(self, role, branch)  # 选择分支
        Function.delete.Flow.select_flow(self, branch, flow)  # 选择流程 前处理1
        Function.delete.Display.select_display(self, branch, flow, case_no)
        try:
            if "データなし" == self.driver.find_element_by_xpath(
                    "/html/body/section/main/div/section/main/div[2]/div[3]/div/span").text:
                Function.Logout.logout(self)
                print("------------debug info--------------"+branch+" "+flow+"---没有找到数据")
                logging.warning('branch=' + branch + 'flow=' + flow + '没有找到数据')
        except:
            Function.delete.Display.handle(self, branch, flow, case_no)
            # 以下部分，会因为进入的分支不同而操作不同
            if branch == "営業点検" and flow == "営業点検":
                Function.delete.Settings.business_check1(self)
            elif branch == "火災" and flow == "点検1回目":
                Function.delete.Upload.upload(self)
                Function.delete.Settings.fire_spot_check1(self)
                Function.delete.Upload.upload(self)
            elif branch == "bank" and flow == "営業点検":
                Function.delete.Settings.bank_business_check(self)

            # 无论什么分支，最后都执行退出流程
            Function.delete.Finish.finish(self)  # 处理完成
            Function.Logout.logout(self)
            print("------------debug info--------------"+branch+" "+flow+"---结束")
            logging.debug('branch=' + branch + 'flow=' + flow + '------结束-----')
        finally:
            pass


