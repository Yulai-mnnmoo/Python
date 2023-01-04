#coding=utf-8
#变量
#声明变量   变量的数据类型根据赋值数据而定
a="JJJJ"
b=1
b=True
print("a",a,type(a),type(b)) #变量 b 可以接收其他数据类型数据


#语句
gree="Hkkeevv"
student_score=0.0; # 语句结束后可以加分号 但不符合py编程规则
a=b=c=10 #链式赋值可以同时给多个变量赋值


#模块
#第一种  模块m.py
import  m
y=20
print("第一种m模块的x",m.x,y)
#第二种  模块m.py
from m import x
y=10
print("第二种m模块的x",x)
#第三种  模块m.py
from m import x as x1
x=100
y=10
print("第二种m模块的x",x1,x)#第三种重命名引入模块的变量 不会与本模块同名变量冲突


