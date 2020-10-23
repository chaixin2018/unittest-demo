import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject, pyqtSignal


icon_control = 'E://chaixin//02_working//04_automation//03_daido-demo//demo1_0722//GUI//icon//icon_control.png'
icon_exit = 'E://chaixin//02_working//04_automation//03_daido-demo//demo1_0722//GUI//icon//exit.png'

class CasePage(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()  # 界面绘制交给InitUi方法

    def init_ui(self):


        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 300, 220)
        # 设置窗口的标题
        self.setWindowTitle('测试平台')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon(icon_control))

        # 显示窗口
        self.show()

class homePage(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QAction(QIcon(icon_exit), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        helpAction = QAction(QIcon('help.png'), '&使用帮助', self)
        # self.pushButton_enter.clicked.connect(self.on_pushButton_enter_clicked)
        versionAction = QAction(QIcon('version.png'), '&版本信息', self)


        # 创建一个菜单栏
        menubar = self.menuBar()
        # 添加菜单
        fileMenu1 = menubar.addMenu('&用例')
        fileMenu2 = menubar.addMenu('&配置')
        fileMenu3 = menubar.addMenu('&执行')
        fileMenu4 = menubar.addMenu('&帮助')
        # 添加事件
        fileMenu1.addAction(exitAction)
        fileMenu2.addAction(exitAction)
        fileMenu3.addAction(exitAction)

        fileMenu4.addAction(helpAction)
        fileMenu4.addAction(versionAction)

        # 主界面设置，位置大小名称
        self.setGeometry(0,0,1200, 600)
        self.setWindowTitle('测试平台')

        # 状态栏设置
        self.statusBar().showMessage('Ready')

        # 配置使用帮助信息
        # self.helpAction.clicked.connect(self.word_get)

class LoginPage(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        textName = QTextEdit()
        textPassword = QTextEdit()


        # 主界面设置，位置大小名称
        self.setGeometry(0,0,1200, 600)
        self.setWindowTitle('测试平台')

        # 状态栏设置
        self.statusBar().showMessage('Ready')

        self.show()

# 多行文本框
class TextEdit(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("test")
        self.resize(300,300)
        self.textEdit = QTextEdit()
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        self.setLayout(layout)



# 按钮QPushButton
class pushButton1(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.setWindowTitle("test")
        self.resize(300, 300)

        button1 = QPushButton("button1")
        button1.setCheckable(False)

        button2 = QPushButton("button2")
        button2.setEnabled(False)

        layout.addWidget(button1)
        layout.addWidget(button2)
        self.setLayout(layout)


# 复选框
class CheckBox(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.setWindowTitle("test")
        self.resize(300, 300)

        self.box1 = QCheckBox("&checkbox1")
        self.box1.setChecked(True)

        # layout.addWidget(box)
        layout.addWidget(self.box1)
        self.setLayout(layout)


# 按钮RationButton
class rationButton1(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.setWindowTitle("test")
        self.resize(300, 300)

        ration1 = QRadioButton("ration1")
        ration1.setCheckable(True)

        ration2 = QRadioButton("ration2")
        ration2.setEnabled(False)

        layout.addWidget(ration1)
        layout.addWidget(ration2)
        self.setLayout(layout)

# 网格布局
class gridlayout(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 1
        layout = QGridLayout()
        self.setLayout(layout)

        # 2
        names = ['cls', 'back', '', 'close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        # 3
        positions = [(i, j) for i in range(5) for j in range(4)]

        # 4
        for positions, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            layout.addWidget(button, *positions)

        self.setWindowTitle("test")
        self.resize(300, 300)
        self.move(300, 100)

# 表单布局
class formLayout(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        fromlayout = QFormLayout()
        self.setLayout(fromlayout)

        self.setWindowTitle("test")
        self.resize(300, 300)

        label1 = QLabel("标签1")
        lineEdit1 = QLineEdit()
        label2 = QLabel("标签2")
        lineEdit2 = QLineEdit()
        label3 = QLabel("标签3")
        lineEdit3 = QLineEdit()

        fromlayout.addRow(label1, lineEdit1)
        fromlayout.addRow(label2, lineEdit2)
        fromlayout.addRow(label3, lineEdit3)


class exlayout(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 1 添加布局
        # 全局布局
        wlayout = QHBoxLayout()
        # 局部局部
        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()
        glayout = QGridLayout()
        formlayout = QFormLayout()

        # 2 准备四个控件
        hwg = QWidget()
        vwg = QWidget()
        gwg = QWidget()
        fwg = QWidget()

        # 3 使用四个控件设置局部布局
        hwg.setLayout(hlayout)
        vwg.setLayout(vlayout)
        gwg.setLayout(glayout)
        fwg.setLayout(formlayout)

        # 4 将四个控件添加到全局布局中
        wlayout.addWidget(hwg)
        wlayout.addWidget(vwg)
        wlayout.addWidget(gwg)
        wlayout.addWidget(fwg)

        # 5 将窗口设置为全局布局
        self.setLayout(wlayout)

        # 6 为局部布局添加控件
        hlayout.addWidget(QPushButton("1"))
        hlayout.addWidget(QPushButton("2"))

        vlayout.addWidget(QPushButton("3"))
        vlayout.addWidget(QPushButton("4"))

        # glayout.addWidget(QPushButton("5"), 0, 0)
        # glayout.addWidget(QPushButton("6"), 0, 1)
        # glayout.addWidget(QPushButton("7"), 1, 0)
        # glayout.addWidget(QPushButton("8"), 1, 1)

        formlayout.addWidget(QPushButton("9"))
        formlayout.addWidget(QPushButton("10"))
        formlayout.addWidget(QPushButton("11"))
        formlayout.addWidget(QPushButton("12"))

        names = ['cls', 'back', '', 'close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for positions, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            glayout.addWidget(button, *positions)
        self.setWindowTitle("test")
        self.resize(300, 300)
        self.move(300, 100)


class QTypeSingnal(QObject):
    # 定义一个信号
    sendmsg = pyqtSignal(object)

    def __init__(self):
        super(QTypeSingnal, self).__init__()

    def run(self):
        # 发射信号
        self.sendmsg.emit("hello pyqt5")


class QTypeSlot(QObject):
    def __init__(self):
        super(QTypeSlot, self).__init__()

    # 槽对象中的槽函数
    def get(self, msg):
        print("QSlot get msg =>" + msg)


class Winform(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle('test')
        self.resize(330,100)
        btn = QPushButton("关闭",self)
        btn.clicked.connect(self.close)


class Winform2(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle('test')
        self.resize(330,100)
        btn = QPushButton("关闭",self)
        btn.clicked.connect(self.btn_close)

    def btn_close(self):
        self.close()


class Winform3(QWidget):
    # 自定义信号，不带参数
    button_clicked_signal = pyqtSignal()

    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle('test')
        self.resize(330,100)
        btn = QPushButton("关闭",self)
        # 连接信号与槽函数
        btn.clicked.connect(self.btn_clicked)
        # 接收信号，连接到槽函数
        self.button_clicked_signal.connect(self.close)

    def btn_clicked(self):
        self.button_clicked_signal.emit()


class MyWidget11(QWidget):
    # 无参数的信号
    Signal_NoParameters = pyqtSignal()
    # 带一个参数信号
    Signal_OneParameters = pyqtSignal(int)
    # 带两个个参数信号
    Signal_TwoParameters = pyqtSignal(int, str)

    def setValue_NoParameters(self):
        '''无参数的槽函数'''
        pass

    def setValue_OneParameters(self, intIndex):
        '''无参数的槽函数'''
        pass

    def setValue_TwoParameters(self, xIndex, yIndex):
        '''无参数的槽函数'''
        pass

    # Signal_NoParameters.connect(setValue_NoParameters)
    # Signal_NoParameters.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = homePage()
    ex.show()
    sys.exit(app.exec_())

    # send = QTypeSingnal()
    # slot = QTypeSlot()
    # print("---把信号绑定到槽函数上---")
    # send.sendmsg.connect(slot.get)
    # send.run()
    # print("---把信号与槽函数的连接断开")
    # send.sendmsg.disconnect(slot.get)
