# hyjGOAT
# 2022/11/9 15:16
import sys

from PyQt5.QtWidgets import QApplication
from PySide2.QtGui import QIcon, QFont, QTextCursor
from PySide2.QtWidgets import QMainWindow, QPushButton, QLabel, QSpinBox, QTextEdit, QMessageBox, QProgressBar
import requests
import parsel
import csv
import psycopg2
import pandas as pd
from globalVar import gloVar
from showintable import ShowInMainWindow


class CityFile:
    page_num = 0
    data = []
    city_name = ' '

    def __init__(self):
        self.window = QMainWindow()
        self.window.setFixedSize(1800, 800)
        self.window.setWindowTitle(gloVar.hanziname + "二手房信息")
        self.window.move(60, 60)
        self.window.setWindowIcon(QIcon("v2_version3\image\icon2.jpg"))

        self.tw = ShowInMainWindow()

        self.label = QLabel(self.window)
        self.label.setPixmap("v2_version3\image\\bg3.jpg")
        self.label.setFixedSize(1800, 800)
        # self.window.setStyleSheet('''QWidget{background-color:#00CC33;}''')



        self.progressbar = QProgressBar(self.window)
        self.progressbar.move(550, 20)
        self.progressbar.resize(400, 50)
        # self.progressbar.setStyleSheet(
        #     "QProgressBar { border: 2px solid grey; border-radius: 5px; background-color: \
        #     #FFFFFF; text-align: center;}QProgressBar::chunk {background:\
        #     QLinearGradient(x1:0,y1:0,x2:2,y2:0,stop:0 #666699,stop:1  #DB7093); }")
        self.progressbar.setStyleSheet("QProgressBar {   border: 2px solid #2196F3;\n"
                                       "border-radius: 5px;   background-color: #FFFFFF;}QProgressBar::chunk \
                                       {   background-color: #2196F3;\n"
                                       "width: 10px;margin: 0.5px;}")
        font = QFont()
        font.setBold(True)
        font.setWeight(30)
        self.progressbar.setFont(font)
        # 设置一个值表示进度条的当前进度
        self.pv = 0
        # 设置进度条的范围
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)
        self.progressbar.setValue(self.pv)
        ## 设置进度条文字格式
        self.progressbar.setFormat(' ')

        self.label = QLabel(self.window)
        self.label.move(50, 30)
        self.label.resize(300, 25)
        self.label.setText("请输入您想爬取的页面总数：")

        self.spinbox = QSpinBox(self.window)
        self.spinbox.resize(100, 27)
        self.spinbox.setRange(1, 100)
        self.spinbox.move(310, 30)

        self.button = QPushButton('开始爬取', self.window)
        self.button.move(430, 30)
        self.button.clicked.connect(self.collect_data)

        self.textEdit = QTextEdit(self.window)
        self.textEdit.move(25, 90)
        self.textEdit.resize(1100, 280)

        self.textEdit2 = QTextEdit(self.window)
        self.textEdit2.move(25, 480)
        self.textEdit2.resize(1100, 280)

        self.label2 = QLabel(self.window)
        self.label2.move(50, 380)
        self.label2.resize(350, 50)
        self.label2.setText("如果想将数据存入数据库请点击确定")

        self.label3 = QLabel(self.window)
        self.label3.move(50, 420)
        self.label3.resize(350, 50)
        self.label3.setText("如果想展示数据库中的数据请点击展示")

        self.button2 = QPushButton('确定', self.window)
        self.button2.move(420, 390)
        self.button2.clicked.connect(self.store_to_list)
        self.button2.clicked.connect(self.show_messagebox)

        self.button3 = QPushButton('展示', self.window)
        self.button3.move(420, 430)
        self.button3.clicked.connect(self.get_data_from_database)

        # self.button4 = QPushButton('返回', self.window)
        # self.button4.move(1600, 700)
        # self.button4.clicked.connect(self.back_to_mainscene)



    def get_spinbox_num(self):
        gloVar.page_num = self.spinbox.value() + 1

    # def back_to_mainscene(self):
    #     self.window.hide()
    #     self.mainscene.window.show()

    def show_messagebox(self):
        messagebox = QMessageBox()
        messagebox.setWindowTitle('成功')
        messagebox.setText('成功写入数据库')
        messagebox.exec_()

    def collect_data(self):
        print("正在爬取。。。")
        header_list = ['标题', '开发商', '房子信息', '户型', '面积', '朝向', '装修', '楼层', '建造时间', '结构', '发布周期', '售价/万', '单价']
        with open("v2_version3\\" + gloVar.hanziname+"二手房信息.csv", mode="w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, header_list)
            writer.writeheader()
            self.get_spinbox_num()
            for page in range(1, gloVar.page_num):
                url = "https://{0}.lianjia.com/ershoufang/pg{1}".format(gloVar.name, page)
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.3161 SLBChan/25"
                }
                response = requests.get(url=url, headers=headers)
                selector = parsel.Selector(response.text)
                lis = selector.css('.sellListContent li')
                dit = {}
                for li in lis:
                    title = li.css('.title a::text').get()
                    dit['标题'] = title
                    positionInfo = li.css('.positionInfo a::text').getall()
                    info = '-'.join(positionInfo)
                    dit['开发商'] = info
                    houseInfo = li.css('.houseInfo::text').get()
                    dit['房子信息'] = houseInfo
                    housrInfoSplit = houseInfo.split('|')
                    # print("1111111111111111111111111111111111111")
                    # print(housrInfoSplit)
                    # print("1111111111111111111111111111111111111")
                    if len(housrInfoSplit) == 7:
                        dit['户型'] = housrInfoSplit[0]
                        dit['面积'] = housrInfoSplit[1]
                        dit['朝向'] = housrInfoSplit[2]
                        dit['装修'] = housrInfoSplit[3]
                        dit['楼层'] = housrInfoSplit[4]
                        dit['建造时间'] = housrInfoSplit[5]
                        dit['结构'] = housrInfoSplit[6]
                    else:
                        dit['户型'] = housrInfoSplit[0]
                        dit['面积'] = housrInfoSplit[1]
                        dit['朝向'] = housrInfoSplit[2]
                        dit['装修'] = housrInfoSplit[3]
                        dit['楼层'] = housrInfoSplit[4]
                        dit['建造时间'] = "不详"
                        dit['结构'] = housrInfoSplit[5]
                    followInfo = li.css('.followInfo::text').get()
                    dit['发布周期'] = followInfo
                    Price = li.css('.totalPrice span::text').get()
                    dit['售价/万'] = Price
                    unitPrice = li.css('.unitPrice span::text').get()
                    dit['单价'] = unitPrice
                    # print(dit)
                    writer.writerow(dit)
                self.textEdit.append("已经获取第%d页的内容，该页网址是：%s" % (page, "https://{0}.lianjia.com/ershoufang/pg{1}".format(gloVar.name, page)))
                self.changepgbvalue()
        print("爬取完毕。。。")
        self.progressbar.setValue(100)

    def changepgbvalue(self):
        self.pv += int(100/ gloVar.page_num)
        self.progressbar.setValue(self.pv)

    def insert_table(self, data):
        ## 连接到一个给定的数据库
        con = psycopg2.connect(database="v2", user="postgres", password="12345", \
                               host='localhost', port="5432")
        ## 建立游标，用来执行数据库操作
        cur = con.cursor()
        ## 执行SQL命令
        cur.execute("""CREATE TABLE if not exists """ + gloVar.hanziname + """(
                        "标题" varchar(100) PRIMARY KEY   NOT NULL,
                        "开发商" varchar(100) NOT NULL, 
                        "房子信息" varchar(100) ,
                        "户型" varchar(100) ,
                        "面积" varchar(100) ,
                        "朝向" varchar(100) ,
                        "装修" varchar(100) ,
                        "楼层" varchar(100) ,
                        "建造时间" varchar(100) ,
                        "结构" varchar(100) ,
                        "发布周期" varchar(100),
                        "售价" varchar(10),
                        "单价" varchar(10));""")
        # do nothing是在主键冲突时防止SQL报错，若主键冲突则什么也不做
        insert_sql = "INSERT INTO " + gloVar.hanziname + " values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) \
                      on conflict on constraint " + gloVar.hanziname + "_pkey\
                      do nothing;"
        cur.executemany(insert_sql, data)
        # cur.execute("SELECT * FROM public.北京")
        # rows = cur.fetchall()  # 这里返回查询的所有数据集
        ## 提交SQL命令
        con.commit()
        ## 关闭游标
        cur.close()
        ## 关闭数据库连接
        con.close()

    def store_to_list(self):
        data = []
        with open("v2_version3\\" + gloVar.hanziname + "二手房信息.csv", "r", encoding='UTF-8') as f:
            reader = csv.reader(f)
            next(reader)
            for line in reader:
                data.append(line)
            self.insert_table(data)
            print("成功写入数据库！")

    def get_data_from_database(self):
        # 连接参数设置
        database = 'v2'  # 指定数据库名
        username = 'postgres'  # 指定用户名
        password = '12345'
        host = "localhost"
        port = "5432"  # 指定数据库端口号
        gongsi_conn = psycopg2.connect(database=database, user=username,
                                       password=password, host=host, port=port)
        # 获取数据
        data1 = pd.read_sql("select * from public." + gloVar.hanziname, con=gongsi_conn)
        self.textEdit2.insertPlainText(str(data1))
        # print(data1)
        gongsi_conn.close()  # 关闭数据库连接

        self.tw.show()
        self.tw.change_attributes(gloVar.hanziname)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = CityFile()
    myWin.window.show()
    # test = mainwindow.Test()
    sys.exit(app.exec_())


