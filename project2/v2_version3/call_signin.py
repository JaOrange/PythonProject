# hyjGOAT
# 2022/11/12 23:00

# hyjGOAT
# 2022/11/12 22:14
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel
from signin import Ui_Form  # 导入你写的界面类


class SignMainWindow(QWidget, Ui_Form):  # 这里也要记得改
    def __init__(self):
        super(SignMainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("注册")
        self.setWindowIcon(QIcon("v2_version3\image\signin.png"))
        self.label.setText("用户名")
        self.label_2.setText("密码")
        self.label_3.setText("确认密码")
        self.pushButton_2.setText("注册")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = SignMainWindow()
    myWin.show()
    sys.exit(app.exec_())
