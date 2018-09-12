
# -*- coding:utf-8 -*-
#encoding=utf8
import pymysql
# PY_MYSQL_CONN_DICT = {
#     "host": '127.0.0.1',
#     "port": 3306,
#     "user": 'root',
#     "passwd": '123456',
#     "db": 'test',
#     "charset": 'utf8'
# }
# conn = pymysql.connect(**PY_MYSQL_CONN_DICT)   #连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='test', charset='utf8')
cursor = conn.cursor()                         #创建游标

#对数据库的操作
sql = "show databases"
cursor.execute(sql)    #执行sql
a=cursor.fetchall()      #通过执行sql，获取所有返回的信息
#cursor.fetchone()     #通过执行sql，获取返回信息中的一条

conn.commit()    #如果只是查询操作，这个命令可以不用加
print(a)
cursor.close()
conn.close()