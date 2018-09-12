#encoding=utf8
import pymysql
#1.建立连接
connect = pymysql.connect(
                        '127.0.0.1', #数据库地址
                        'root',      #数据库用户名
                        '123456',    #数据库密码
                        'test',    #数据库名
                         3306,       #数据库端口(默认就是3306，端口不加引号，不然报错)
                        charset='utf8' #设置字符集编码
                        )
#2.实例化游标(是一个内存地址，存放的是python对mysql提交的命名和执行命令之后返回的结果)
cursor = connect.cursor()
#3.定义要执行sql语句(比如现在我们要创建一个teacher表)
sql1 = """create table if not exists student(
    id int primary key auto_increment,
    name char(20) not null,
    age char(3) not null,
    sex char(1) not null,
    email char(50) not null,
    address char(100) not null
    )"""
sql2 = """show tables"""
#4.提交命令
a = cursor.execute(sql1) #通过execute()方法向mysql提交要执行的sql命令
b = cursor.execute(sql2)
#5.提交修改(将python提交给mysql的sql命令在mysql当中执行)
connect.commit()

# print(a)
print(b)
#6.关闭游标(如果不关闭会占用内存资源)
cursor.close()

#7.关闭连接
connect.close()