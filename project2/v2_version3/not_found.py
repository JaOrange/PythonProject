# hyjGOAT
# 2022/11/10 11:43

from PySide2.QtWidgets import QMainWindow, QLabel
from PySide2.QtGui import QIcon
from globalVar import gloVar


class NF:
    def __init__(self):
        self.window = QMainWindow()
        self.window.setFixedSize(1800, 800)
        self.window.setWindowTitle(gloVar.hanziname + "二手房信息")
        self.window.move(60, 60)
        self.window.setWindowIcon(QIcon("v2_version3\image\icon2.jpg"))

        self.label = QLabel(self.window)
        self.label.setPixmap("v2_version3\image\\nf2.jpg")

        self.label.move(500, 0)
        self.label.resize(800,500)
