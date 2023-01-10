#定义函数
def rect_area(width,height):
    area=width*height
    return area

def print_area(width,height):
    a=width*height
    print('{0}x{1}的长方形的面积是:{2:0.2f}',width,height,a)

#调用函数  使用位置参数调用
r_area = rect_area(200,100)
print('{0}x{1}的长方形的面积是:{2:0.2f}'.format(200,100,r_area))

#调用函数  使用关键字产参数调用
r_area = rect_area(width=200,height=100)
print('{0}x{1}的长方形的面积是:{2:0.2f}'.format(200,100,r_area))  #关键字的名称定义函数时形参的名称  不在受顺序限制


#参数的默认值
def make_coffee(name='冰美式'):
    return '制作一杯{0}'.format(name)

coffee1=make_coffee('xxx')
coffee2=make_coffee() #不传参数时 使用默认值

print('kkk',coffee1,coffee2)

#可变参数   基于元组
def sum(*numbers):
    total =0.0
    for i in numbers:
        total+=i
    return total

print(sum(10,30,50))
print(sum(20))

#可变参数   基于字典
def show_info(**info):
    for key,value in info.items():
        print('{0} -- {1}'.format(key,value))

show_info(s_sto=1002,s_name='zhangsan')
show_info(s_sto=1001,s_name='lisi',sex=True)

#变量的作用域
x=20

def f1():
    # global x    global变量 将局部变量提升为全局变量
    x=10
    print('x={0}'.format(x))

f1()
print('xxx={0}'.format(x))

# 函数类型
def add(a,b):
    a+b
    return a+b

def sub(a,b):
    a-b
    return a-b

def cal(opr):
    if opr=='+++':
        return add
    else:
        return sub

f1=cal('add')
f2=cal('sub')
print('10-5={0}'.format(f1(10,5)))

#过滤函数
def f3(x):
    return x>50

data1=[20,30,50,53,83,22]
filterd=filter(f3,data1)
data2=list(filterd)

print(data2)
#映射函数
def f4(x):
    return x*2

data3=list(map(f4,data1))

print(data3)

#匿名函数
def cals(opr):
    if opr=='+':
        return lambda a,b:(a+b)   #替代add函数
    else:
        return lambda a,b:(a-b) #替代sub函数

f1=cals('+')
f2=cals('-')
print('10-5={0}'.format(f1(10,5)))

data1=[20,30,50,53,83,22]
fi=filter(lambda a:(a>20),data1)
data5=list(fi)

print(data5)