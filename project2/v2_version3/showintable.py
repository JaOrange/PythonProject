import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from tablewidget import Ui_Form  # 导入你写的界面类
import csv


class ShowInMainWindow(QWidget, Ui_Form):  # 这里也要记得改
    def __init__(self):
        super(ShowInMainWindow, self).__init__()
        self.setupUi(self)
        self.resize(1000, 600)

    def change_attributes(self, city_name):
        self.setWindowTitle(city_name + "二手房信息")
        self.setWindowIcon(QIcon(".\image\\icon2.jpg"))
        self.tableWidget.setColumnCount(13)
        header_list = ['标题', '开发商', '房子信息', '户型', '面积', '朝向', '装修',\
                       '楼层', '建造时间', '结构', '发布周期', '售价/万', '单价']
        self.tableWidget.setHorizontalHeaderLabels(header_list)
        content = []
        with open("v2_version3\\" + city_name + "二手房信息.csv", "r", encoding='UTF-8') as f:
            reader = csv.reader(f)
            next(reader)
            for line in reader:
                content.append(line)
        # print(content)
        for i in range(len(content)):
            self.tableWidget.insertRow(i)
            for j in range(len(content[i])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(content[i][j])))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tw = ShowInMainWindow()
    tw.show()
    tw.change_attributes("北京")
    sys.exit(app.exec_())
