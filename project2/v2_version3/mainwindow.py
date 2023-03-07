# hyjGOAT
# 2022/11/9 14:32

from PySide2 import QtGui
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QFont, QCursor
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QLineEdit, QComboBox, QLabel
from PyQt5.QtWidgets import QMessageBox
import cityinfo
import re
from pypinyin import lazy_pinyin, Style
import not_found
import database
from globalVar import gloVar
from call_login import LogMainWindow
from call_signin import SignMainWindow
from VerificationCode import VerificationCode
from my_Log import Log


class Test:
    str1 = ''
    res = []

    def __init__(self):
        self.window = QMainWindow()
        self.window.setFixedSize(1800, 795)
        self.window.setWindowTitle("二手房信息")
        self.window.move(60, 60)
        self.window.setWindowIcon(QIcon("v2_version3\image\icon2.jpg"))
        self.choose_city = cityinfo.CityFile()
        self.nf = not_found.NF()
        self.mylog = LogMainWindow()
        self.db = database.DB()
        self.mySign = SignMainWindow()
        self.vc = VerificationCode()
        self.log = Log()

        self.textEdit = QTextEdit(self.window)
        self.textEdit.move(1000, 25)
        self.textEdit.resize(100, 100)

        self.label = QLabel(self.window)
        self.label.setPixmap("v2_version3\image\\background.jpg")
        self.label.setFixedSize(1800, 800)

        # self.change_bgimage_button = QPushButton(self.window)
        # self.change_bgimage_button.move(1700, 250)
        # self.change_bgimage_button.resize(100, 300)
        # self.change_bgimage_button.setCursor(QCursor(Qt.PointingHandCursor))
        # self.change_bgimage_button.setStyleSheet(
        #     "QPushButton{background:transparent;}")
        # icon = QIcon(".\image\\right.png")
        # self.change_bgimage_button.setIcon(icon)
        # self.change_bgimage_button.clicked.connect(self.changebg)

        self.loginButton = QPushButton('未登录', self.window)
        self.loginButton.move(1550, 0)
        self.loginButton.resize(100, 80)
        self.loginButton.setStyleSheet("QPushButton{font-family:'微软雅黑';font-size:20px;border:none;color:white;background:transparent;}")
        self.loginButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon("v2_version3\image\\unlog.png")
        self.loginButton.setIcon(icon)
        self.loginButton.clicked.connect(self.open_login_scene)

        self.mylog.pushButton.clicked.connect(self.pushButtonLogin_click)
        self.mylog.pushButton_2.clicked.connect(self.pushButtonSignin_click)
        self.mySign.pushButton_2.clicked.connect(self.from_signin_to_mainscene)

        self.mylog.pushButton_3.clicked.connect(self.change_verificationcode)
        self.mySign.pushButton_3.clicked.connect(self.change_verificationcode2)
        code1 = self.vc.generate_verification_code()
        code2 = self.vc.generate_verification_code()
        self.mylog.pushButton_3.setText(code1)
        self.mySign.pushButton_3.setText(code2)

        self.signinButton = QPushButton('立即注册', self.window)
        self.signinButton.move(1670, 0)
        self.signinButton.resize(100, 80)
        self.signinButton.setStyleSheet("QPushButton{font-family:'微软雅黑';font-size:20px;border:none;color:white;background:transparent;}")
        self.signinButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.signinButton.clicked.connect(self.open_signin_scene)

        self.lineEdit = QLineEdit(self.window)
        self.lineEdit.setPlaceholderText("您现在是游客模式，请登录后找房")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setFont(QFont("微软雅黑", 20))
        self.lineEdit.move(367, 435)
        self.lineEdit.resize(971, 85)
        self.lineEdit.returnPressed.connect(self.fuzzysearch)

        # self.lineEdit2 = QLineEdit(self.window)
        # self.lineEdit2.setPlaceholderText("请输入您想搜索的城市的编号：")
        # self.lineEdit2.move(500, 100)
        # self.lineEdit2.resize(300, 50)

        self.button = QPushButton('开始找房', self.window)
        self.button.setCursor(QCursor(Qt.PointingHandCursor))
        self.button.move(1337, 435)
        self.button.resize(200, 84)
        self.font = QtGui.QFont()
        self.font.setFamily('微软雅黑')
        self.font.setBold(True)
        self.font.setPointSize(16)
        self.font.setWeight(50)
        self.button.setFont(self.font)
        self.button.setStyleSheet(
            '''QPushButton{color: white; background: green; border-radius: 5px;}\
               QPushButton:hover{color: black; background: #F7D674;}''')
        self.button.clicked.connect(self.choose_city_num)
        self.button.clicked.connect(self.change_to_city_scene)

        # self.button3 = QPushButton('开始找房', self.window)
        # self.button3.move(1337, 519)
        # self.button3.resize(200, 42)
        # self.button3.clicked.connect(self.choose_city_num)
        # self.button3.clicked.connect(self.change_to_city_scene)

        # self.button2 = QPushButton('北京', self.window)
        # self.button2.move(100, 300)
        # self.button2.clicked.connect(self.change_to_city_scene)
        self.comboBox = QComboBox(self.window)
        self.comboBox.resize(0, 0)

    def change_verificationcode(self):
        cod = self.vc.generate_verification_code()
        self.mylog.pushButton_3.setText(cod)

    def change_verificationcode2(self):
        cod = self.vc.generate_verification_code()
        self.mySign.pushButton_3.setText(cod)

    def from_signin_to_mainscene(self):  # 注册账户并写入数据库
        user = self.mySign.lineEdit.text()
        password1 = self.mySign.lineEdit_2.text()
        password2 = self.mySign.lineEdit_3.text()
        print(user, password1)
        if password1 == password2:
            content = self.mySign.lineEdit_4.text()
            if content != self.mySign.pushButton_3.text():
                QMessageBox.warning(self.mySign,
                                    "警告",
                                    "验证码输入错误",
                                    QMessageBox.Yes)
            else:
                self.db.CreatTable()
                if self.db.insert_db(user, password1):
                    QMessageBox.critical(self.mySign,
                                        "失败",
                                        "用户名已存在！",
                                        QMessageBox.Yes)
                else:
                    QMessageBox.information(self.mySign,
                                        "成功",
                                        "成功注册用户！",
                                        QMessageBox.Yes)

                    self.mySign.close()
        else:
            QMessageBox.warning(self.mySign,
                                "警告",
                                "两次密码输入不一致！",
                                QMessageBox.Yes)


    def pushButtonSignin_click(self):
        self.mySign.show()
        self.mylog.close()

    def change_Icon(self):
        self.loginButton.setText("已登录")
        icon = QIcon("v2_version3\image\log.png")
        self.loginButton.setIcon(icon)
        self.lineEdit.setPlaceholderText("请输入您想搜索的城市信息：")
        self.lineEdit.setEnabled(True)

    def pushButtonLogin_click(self):
        # 判断用户名密码
        user = self.mylog.lineEdit.text()
        password = self.mylog.lineEdit_2.text()
        if len(user) and len(password):
            """这里是输入账号密码，接下来要去数据库中匹配密码是否正确，如果正确就执行main_window.close()"""
            if self.db.has_user(user, password) == "a":
                content = self.mylog.lineEdit_3.text()
                if content == self.mylog.pushButton_3.text():
                    self.mylog.close()
                    QMessageBox.information(self.mylog,
                                        "成功",
                                        "正在进入。。。",
                                        QMessageBox.Yes)
                    self.change_Icon()
                    self.window.show()
                else:
                    QMessageBox.warning(self.mylog,
                                        "警告",
                                        "验证码输入错误",
                                        QMessageBox.Yes)
            elif self.db.has_user(user, password) == "b":
                QMessageBox.warning(self.mylog,
                                    "警告",
                                    "密码输入错误！",
                                    QMessageBox.Yes)
            else:
                QMessageBox.warning(self.mylog,
                                    "警告",
                                    "账户不存在！",
                                    QMessageBox.Yes)
        else:
            QMessageBox.warning(self.mylog,
                                "警告",
                                "用户名或密码没有输入！",
                                QMessageBox.Yes)

    def open_login_scene(self):
        self.mylog.show()

    def open_signin_scene(self):
        self.mySign.show()

    def change_to_city_scene(self):
        self.window.hide()
        if gloVar.hanziname in ["哈尔滨", "拉萨", "澳门", "台北", "银川", "西宁"]:
            self.nf.window.show()
        else:
            self.choose_city.window.show()

    def is_chinese(self):
        for ch in self.str1:
            if '\u4e00' <= ch <= '\u9fff':
                return True
        return False

    def fuzzysearch(self):
        self.str1 = self.lineEdit.text()
        self.log.info("输入了城市名称，正在检测输入格式是否正确")
        with open("v2_version3\\" + "provincial capital.txt", "r", encoding='UTF-8') as f:
            for content in f:
                if re.search(self.str1, content) is not None:
                    self.res.append(content.replace('\n', ''))
            if len(self.res) == 0:
                print("没找到啊。。。")
                self.lineEdit.setText("oops! 没找到呀。。。")
                self.log.error("没有找到城市信息!")
            else:
                self.comboBox.move(367, 520)
                self.comboBox.resize(971, 85)
                self.comboBox.setFont(QFont("Timers", 20))
                self.log.info("输入了正确的城市名称，正在进行模糊搜索")
                for i in self.res:
                    print(self.res.index(i), i)
                    self.textEdit.insertPlainText(str(self.res.index(i)))
                    self.comboBox.addItem(str(self.res.index(i))+" "+i)
                    self.textEdit.insertPlainText(" "+i)
                    self.textEdit.insertPlainText("\n")

    def get_first_letter(self, str2):
        ans = ''.join(lazy_pinyin(str2, style=Style.FIRST_LETTER))
        gloVar.name = ans
        print(gloVar.name)
        return ans

    def choose_city_num(self):
        num = self.comboBox.currentIndex()
        sep = ""
        item = self.res[num]
        gloVar.hanziname = sep.join(item)
        print("所选城市为：" + sep.join(item))
        initial_letter = self.get_first_letter(sep.join(item))
        print("搜索结果为：%s，所对应的文件路径为：%s" % (sep.join(item) + "->" + initial_letter, \
                                         "D:\python_demo\\v1_version2\city\\" + sep.join(item) + ".txt"))
        self.log.info("搜索成功")

if __name__ == "__main__":
    a = QApplication([])
    test = Test()
    choose_city = cityinfo.CityFile()
    nf = not_found.NF()
    test.window.show()
    a.exec_()