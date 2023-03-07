# hyjGOAT
# 2022/11/10 23:33

import psycopg2
# 连接到一个给定的数据库


class DB:
    def CreatTable(self):
        print("正在建立数据库")
        conn = psycopg2.connect(database="login", user="postgres", password="12345", host="localhost", port="5432")
        # 建立游标，用来执行数据库操作
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE if not exists userInfo(
                                    username varchar(20) PRIMARY KEY     NOT NULL,
                                    password varchar(20) NOT NULL)""")
        print("成功建好数据库")
        # 提交SQL命令
        conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭数据库连接
        conn.close()

    def insert_db(self, user, password):
        print("进入insert_db函数")
        conn = psycopg2.connect(database="login", user="postgres", password="12345", host="localhost", port="5432")
        # 建立游标，用来执行数据库操作
        cursor1 = conn.cursor()
        cursor2 = conn.cursor()
        sql1 = "select * from userInfo where username='%s'" % user
        sql2 = "INSERT INTO userInfo values(%s,%s)\
                        on conflict on constraint userInfo_pkey\
                        do nothing;" % (user, password)
        cursor1.execute(sql1)
        result = cursor1.fetchall()
        if len(result) > 0:
            print("该用户名已被注册！")
            # 提交SQL命令
            conn.commit()
            # 关闭游标
            cursor1.close()
            # 关闭数据库连接
            conn.close()
            return True
        else:
            cursor2.execute(sql2)
            # 提交SQL命令
            conn.commit()
            cursor2.close()
            # 关闭数据库连接
            conn.close()
            return False

    def has_user(self, account, password):
        conn = psycopg2.connect(database="login", user="postgres", password="12345", host="localhost", port="5432")
        cursor = conn.cursor()
        cursor2 = conn.cursor()
        sql = "select * from userInfo where username='%s' and password='%s' " % (account, password)
        sql2 = "select * from userInfo where username='%s'" % account
        print(sql)
        cursor.execute(sql)
        cursor2.execute(sql2)
        result = cursor.fetchall()
        result2 = cursor2.fetchall()
        print(result)
        print(result2)
        # 提交SQL命令
        conn.commit()
        # 关闭游标
        cursor.close()
        cursor2.close()
        # 关闭数据库连接
        conn.close()
        if len(result2) > 0:
            print("该账户信息存在")
            if len(result) > 0:
                print("用户名、密码输入正确")
                return "a"
            else:
                print("密码输入错误！")
                return "b"
        else:
            print("该账户不存在")
            return "c"




