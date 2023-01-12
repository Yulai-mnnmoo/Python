#coding=utf-8
#有条件查询
import sqlite3
i_name=input('请输入姓名：')
i_sex=input("请输入性别（1表示男 0表示女）：")
i_birthday=input('请输入生日（yyyyMMdd）：')
try:
    #建立数据连接
    con=sqlite3.connect('../SQLite/my_db.db')
    #创建游标对象
    cursor=con.cursor()
    #执行sql查询操作
    sql='INSERT INTO student(s_name,s_sex,s_birthday) VALUES(?,?,?)'
    cursor.execute(sql,[i_name,i_sex,i_birthday])
    #提交数据库事务
    con.commit()
    print("插入数据成功")
except sqlite3.Error as e:
    print('插入数据失败{}'.format(e))
    #回滚事务
    con.rollback()
finally:
    #关闭游标
    if cursor:
        cursor.close()
    #关闭数据连接
    if con:
        con.close()
