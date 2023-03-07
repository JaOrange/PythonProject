# hyjGOAT
# 2022/11/12 22:14
import sys

from PyQt5.QtGui import QIcon, QPainter, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from login import Ui_Form  # 导入你写的界面类


class LogMainWindow(QWidget, Ui_Form):  # 这里也要记得改
    def __init__(self):
        super(LogMainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("登录")
        self.setWindowIcon(QIcon("v2_version3\image\login.png"))
        self.label.setText("用户名")
        self.label_2.setText("密码")
        self.pushButton.setText("登录")
        self.pushButton_2.setText("注册")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = LogMainWindow()
    myWin.show()
    sys.exit(app.exec_())