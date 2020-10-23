import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class mainPage(QDialog):

    def __init__(self):
        super().__init__()

        self.init_ui()  # 界面绘制交给InitUi方法

    def init_ui(self):
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 600, 300)
        # 设置窗口的标题
        self.setWindowTitle('测试平台')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('icon_control.png'))

        self.frame = QFrame(self)
        self.verticalLayout = QVBoxLayout(self.frame)

        self.lineEdit_account = QLineEdit()
        self.lineEdit_account.setPlaceholderText("请输入账号")
        self.verticalLayout.addWidget(self.lineEdit_account)

        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainPage()
    sys.exit(app.exec_())