from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QIcon
from gui import *
# from GUI.gui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import django


icon_logo = 'E://chaixin//02_working//04_automation//03_daido-demo//demo1_0722//GUI//icon//logo.png'
icon_comitX = 'E://chaixin//02_working//04_automation//03_daido-demo//demo1_0722//GUI//icon//ComitX.png'

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 200)
        MainWindow.setWindowIcon(QIcon(icon_logo))
        # MainWindow.setStyleSheet("background-image:url(Background.jpg)")
        MainWindow.setStyleSheet("#MainWindow{background-color: white}")

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        # 显示一张图片
        self.l1 = QtWidgets.QLabel(self.centralWidget)
        self.l1.setGeometry(QtCore.QRect(0, 25, 1000, 100))
        # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        png = QtGui.QPixmap(icon_comitX)
        # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        self.l1.setPixmap(png)
        # 调整l1和l2的位置
        # self.l1.move(100, 100)

        # 添加用户名的文本框
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 20, 100, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        # 添加密码的文本框
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 50, 100, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        # 添加用户名的标签
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(200, 24, 24, 12))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        # 添加密码的标签
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(200, 54, 24, 12))
        self.label_2.setObjectName("label_2")
        # 添加确定按钮
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")
        # 添加取消按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 120, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        # 复选框 记住密码
        self.pushButton_3 = QtWidgets.QCheckBox(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 74, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        # self.pushButton_3.setCheckable(True)

        MainWindow.setCentralWidget(self.centralWidget)

        self.pushButton.clicked.connect(self.word_get)
        self.pushButton_2.clicked.connect(self.btn_close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入帐号"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.label.setText(_translate("MainWindow", "帐号"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton_2.setText(_translate("MainWindow", "取消"))
        self.pushButton_3.setText(_translate("MainWindow", "    记住密码"))

    def word_get(self):
        login_user = self.lineEdit.text()
        login_password = self.lineEdit_2.text()
        if login_user == 'admin' and login_password == '123456':
            ui_hello.show()
            MainWindow.close()

        else:
            QMessageBox.warning(self,
                    "警告",
                    "用户名或密码错误！",
                    QMessageBox.Yes)
            self.lineEdit.setFocus()


    def btn_close(self):
        # qApp.quit()
        Ui_MainWindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui_hello = homePage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
