#coding=utf-8
#有条件查询
import sqlite3
i_id=input("请输入要删除学生的学号：")
try:
    #建立数据连接
    con=sqlite3.connect('../SQLite/my_db.db')
    #创建游标对象
    cursor=con.cursor()
    #执行sql查询操作
    sql='DELETE FROM student WHERE s_id=?'
    cursor.execute(sql,[i_id])
    #提交数据库事务
    con.commit()
    print("删除数据成功")
except sqlite3.Error as e:
    print('删除数据失败{}'.format(e))
    #回滚事务
    con.rollback()
finally:
    #关闭游标
    if cursor:
        cursor.close()
    #关闭数据连接
    if con:
        con.close()
