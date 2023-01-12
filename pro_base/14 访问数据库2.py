#coding=utf-8
#有条件查询
import sqlite3
istr=input('请输入生日(yyyyMMdd):')
try:
    #建立数据连接
    con=sqlite3.connect('../SQLite/my_db.db')
    #创建游标对象
    cursor=con.cursor()
    #执行sql查询操作
    sql='SELECT s_id,s_name,s_sex,s_birthday FROM student WHERE s_birthday<?'
    cursor.execute(sql,[istr])
    #提取结果集
    result_set=cursor.fetchall()
    for row in result_set:
        print("学号：{0}，姓名：{1},性别：{2},生日：{3}".format(row[0],row[1],row[2],row[3]))
except sqlite3.Error as e:
    print('数据查询发生错误{}'.format(e))
finally:
    #关闭游标
    if cursor:
        cursor.close()
    #关闭数据连接
    if con:
        con.close()
