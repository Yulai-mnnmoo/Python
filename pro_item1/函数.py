def rec_area(height,width):
    area=height*width
    return area

print("{0}x{1}的长方形的面积是:{2}".format(30,20,rec_area(30,20)))
print("{0}x{1}的长方形的面积是:{2:.2f}".format(30,20,rec_area(30,20)))

def make_coffee(name='卡布奇洛'):
    return  '制作一杯{0}咖啡'.format(name)

coffee1=make_coffee('拿铁')
coffee2=make_coffee()

print(coffee1)
print(coffee2)


def sum(*numbers):
    total=0
    for number in numbers:
        total+=number

    return total

print(sum(100.0,20.0,30.0))
print(sum(30.0,80.0))

def show_info(**infos):
    for key,value in infos.items():
        print('{0}-{1}'.format(key,value))

show_info(name='Tom',age=16,sex=True)
show_info(student_name='Tom',student_code='1002')


x=20
def print_value():
    global x
    x=10
    print('局部变量x={}'.format(x))

print_value()
print('全局变量x={}'.format(x))

def add(a,b):
    return a+b

def sub(a,b):
    return a-b
def squre(a):
    return a*a
def cal(op):
    if op=='+':
        return add
    else:
        return sub

f1=cal("+")
f2=cal("-")

print("10+3={}".format(f1(10,3)))
print("10-3={}".format(f2(10,3)))


def f1(x):
    return x>50
data=[23,45,67,99,21,211]
list1=filter(f1,data)
print(list(list1))

def f2(x):
    return x*2
list2=map(f2,data)
print(list(list2))


def clal(opr):
    if opr=='+':
        return lambda a,b:a+b
    else:
        return lambda a,b:a-b

f3=clal('+')
f4=clal('-')
# print(f3(1,2))
print('{0}+{1}={2}'.format(1,2,f3(1,2)))
print('{0}-{1}={2}'.format(1,2,f4(1,2)))

data1=[23,45,67,99,21,211]
filtered=filter(lambda x:x>50,data1)
filterList=list(filtered)
print(filterList)

maped=map(lambda x:x*2,data1)
mapList=list(maped)
print(mapList)

