编写和运行python两种方式：交互模式  文件模式

## 编程基础

### 标识符

标识符就是变量、函数、属性、类、模块等可以由程序员指定



### 名称

代码元素  -- 遵循一定的命名规则：
	1 区分大小写：Myname与myname是两个不同的标识符。
	2 首字符可以是下画线（_）或字母，但不能是数字。
	3 除首字符外的其他字符必须是下画线、字母和数字。
	4 关键字不能作为标识符。
	5 不要使用Python的内置函数作为自己的标识符。
	

### 关键字

关键字是由语言本身定义好的有特殊含义的代码元素。 33

![](D:\work\个人包\Python\图片\关键字(33个).png)

### 变量

为一个变量赋值的同时就声明了该变量，该变量的数据

类型就是赋值数据所属的类型，该变量还可以接收其他类型的数据

```python
#coding=utf-8
#声明变量   变量的数据类型根据赋值数据而定
a="JJJJ"
b=1
b=True
print("a",a,type(a),type(b)) #变量 b 可以接收其他数据类型数据

```



### 语句

Python代码是由关键字、标识符、表达式和语句等构成的，语句是代码的重要组成部分

```python
#语句
gree="Hkkeevv"
student_score=0.0; # 语句结束后可以加分号 但不符合py编程规则
a=b=c=10 #链式赋值可以同时给多个变量赋值
```



### 代码注释

在使用＃（井号）时，＃位于注释行的开头，＃后面有一个空格，接着是注释的内容



### 模块

在Python中一个模块就是一个文件，模块是保存代码的最小单位，在模块中可以声明变量、函数、属性和类等Python代码元素
	1  import＜模块名＞
	2  from＜模块名＞import＜代码元素＞
	3  from＜模块名＞import＜代码元素＞as＜代码元素别名＞

```python
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
```





## 数据类型

6种主要的内置数据类型：

、字符串、列表、元组、集合和字典。

列表、元组、集合和字典可以容纳多项数据 --》容器类型的数据

### 数字类型

整数类型、浮点类型、复数类型和布尔类型 
		 布尔类型也是数字类型，它事实上是整数类型的一种

#### 整数类型

int类，整数类型的范围可以很大，表示很大的整数，只受所在计算机硬件的限制。

```python
#整数类型
x=28   #十进制
y=0b11100 #二进制  0b...  0B...
z=0o34 #八进制  0o...  0O...
w=0x1c #十六进制  0x... 0X...

print("xyz值",x,y,z,w,type(x),type(y),type(z),type(w)) #type() 函数返回数据类型
```



#### 浮点类型

浮点类型主要用来存储小数数值，Python的浮点类型为float类。Python只支持双精度浮点类型，而且是与本机相关的

```python
#浮点类型
xx=1.0
yy=3.34e2  #科学计数法表示 e(E)表示10的指数  e2 -->10的平方

print("xxyy",xx,yy,type(xx),type(yy))
```



#### 复数类型

整数和浮点数（小数）在数学中被统称为实数 a+bi，其中a被称为实部，b被称为虚部，i被称为虚数单位

```python
#复数类型
xxx=1+2j
yyy=2+4j

print("xxxyyy",xxx,yyy,(xxx+yyy),type(xxx),type(yyy))#复数类型为complex  复数相加实部相加 复部相加
```



#### 布尔类型

bool类，bool是int的子类，只有两个值：True False

```python
#布尔类型  bool() 函数转化为bool类型数据
a=bool(0)  #False
b=bool(1)  #True
c=bool('')  #False
d=bool(' ') #True
e=bool([])  #False
f=bool({})  #False

print("...",a,b,c,d,e,f)
```



#### 数字类型的相互转换

除复数外，其他三种数字类型如整数、浮
点和布尔都可以相互转换  --》 隐式类型的转换和显式类型的转换
 	1  隐式类型的转换：数字之间可以进行数学计算，在进行数学计		 算时若数字类型不同，则会发生隐式类型的转换

![](D:\work\个人包\Python\图片\数据类型转化.png)

```python
#数据类型转化  隐式
aa=1+True
bb=1.0+1
cc=1.0+True
dd=1.0+1+True
rr=1.0+1+False

print("==",aa,bb,cc,dd,rr)#往‘高’级转化
```

 	2  显式类型的转换  --》 int()  float()  bool()

```python
#数据类型转化  显式
aaa=int(False)
bbb=int(1.0)
ccc=bool(1.0)
ddd=bool(1)
eee=float(False)
fff=float(1)

print("..",aaa,bbb,ccc,ddd,eee,fff)#int()  bool() float()强制数据类型转化 
```



## 运算符

### 算术运算符	

算术运算符用于组织整数类型和浮点类型的数据，有一元运算符和二元运算符之分  
	一元算术运算符有两个：+（正号）和-（负号）
	二元算术运算符如图所示

![](D:\work\个人包\Python\图片\算数运算符.png)

```python
#算术运算符
a=1
b=1+1
c=2-1
d=2/2
e=2*2
f=2%2
g=3//2 # 1
h=-3//2 #-2 地板除法 向下去整
k=10**2

print(-a,b,c,d,e,f,g,h,k)
```



### 比较运算符

比较运算符用于比较两个表达式的大小，其结果是布尔类型的数据，即True或False

![](D:\work\个人包\Python\图片\比较运算符.png)

```python
#比较运算符
aa=1
bb=2
cc=2.0

print(aa>bb,aa<bb,aa==bb,aa<=bb,aa>=bb,aa==cc)
kk="Hello"
ll="Helle"

print(kk>ll) #比较字符串大小 逐一比较字符的Unicode编码大小 依次向后比较

mm=[]
nn=[1,2]
vv=["2"]
print(mm>nn,vv>nn)#列表比较 当两个列类型不兼容时不可以比较
```



### 逻辑运算符

逻辑运算符用于对布尔型变量进行运算，其结果也是布尔型

![](D:\work\个人包\Python\图片\逻辑运算符.png)

```python
#逻辑运算符
a=-1
b=0
def f1():
    print("函数f1")
    return  True

print((a>b) or f1()) #a>b结果为False 结果不确定 要调用f1
print((a>b) and f1()) #a>b结果为False 结果确定 不用调用f1
print(not f1)
```



### 位运算符

位运算是以二进位（bit）为单位进行运算的，操作数和结果都是整数类型的数据

![](D:\work\个人包\Python\图片\位运算符.png)

```python
#位运算符
ss=0b10110010 #178
qq=0b01011110 #94
pp=-0b10110010 #-178

print(~ss)  #10110010  -0b10110011  正数变负数的取反是先取反码 再取补码 再最后位加1
print(ss|qq) # 10110010  01011110   ===> 11111110
print(ss&qq) # 10110010  01011110   ===> 00010010
print(ss^qq) # 10110010  01011110   ===> 11101100
print(ss>>2) #  10110010 ===> 00101100      右位移实际上是去掉最后两位在最前面补右位移位数个0
print(~ss>>2) # -0b10110011 ===> -0b00101101 反码的右位移是 先取反（上面） 再位移  再+1
print(~ss<<2) # -0b10110011 ===> -0b1011001100  同下 左位移
print(ss<<2) # 10110010 ===> 1011001000     左位移实际上是在后面补左位移位数个0
print(pp)  #10110010 01001101 10110001     负数变正数的取反 是先取反码 再取补码 再最后位减1
```



### 赋值运算符

赋值运算符只是一种简写，只有算术运算符和位运算中的二元运算符才有对应的赋值运算符。

![](D:\work\个人包\Python\图片\赋值运算符.png)

```python
#赋值运算符
ge =1
ga =2
# ge+=ga
# ge+=ga+2
# ge-=ga
# ge*=ga
# ge/=ga
# ge%=ga
ge**=ga
go=0b10110010
gk=0b01011110
# go |=gk
go ^=gk
print(ge,go)
```



### 运算符的优先级

 图片表格从上到下优先级依次降低，同一行					 具有相同优先级

![](D:\work\个人包\Python\图片\运算符的优先级.png)

```python
#一个例子 涉及很多 主要的是熟悉这个表格
#运算符的优先级
gs=1-2*2
gq=0b10110010
gw=0b01011110
gc=0b00000011

print(gs,gq|gw&gc,0b10110010)
```





## 流程控制

### 分支语句 

#### if结构 

```xml
if 条件：
	语句组
```

```python
#if 结构
score = int(input("请输入一个人0~100的整数："))

if score<60:
    print("不合格")

if (score>=60) and (score<80):
    print("仍需努力")

if score>=80:
    print("优秀")
```

#### if-else结构

```xml
if 条件：
	语句组1
else:
	语句组2
```

```python
#if-else 结构
score = int(input("请输入一个人0~100的整数："))
if score>=60:
    if score>=85:
        print("优秀")
    else:
        print("还差点！")
else:
    print("不合格")
```

#### if-elif-else结构

```xml
if 条件1：
    语句组1
elif 条件2：
    语句组2
else：
    语句组3
```

```python
#if-elif-else 结构
score3 = int(input("请输入一个人0~100的整数："))
if score3>90:
    print("A")
elif score3>80:
    print("B")
elif score3>70:
    print("C")
else:
    print("D")
```



### 循环语句

```xml
while 循环条件：
		循环语句组
	[else:
		语句组]
```

```python
#while循环
i=0
while i*i<100:
    i+=1
print("i",i,i*i)

#while循环 else 
i=0
while i*i<100:
    i+=1
    print(str(i)+'*'+str(i) +'=',i*i)
else:
    print("over")
```



### for语句

```xml
for 变量 in 可迭代对象：
		循环体语句组
	[else:
		语句组]
```

```python
#for循环
for item in "Hell":
    print("item",item)
numbers = [54,66,88,95,10]
for it in numbers:
    print(it)
else:
    print("over")
```


​		

### 跳转语句

​	跳转语句能够改变程序的执行顺序，包括break、continue和return。
	break和continue用于循环体中，而return用于函数中

break语句
	break语句用于强行退出循环体，不再执行循环体中剩余的语句
continue语句
	continue语句用于结束本次循环，跳过循环体中尚未执行的语句,接着进行终止条件的判断，以决定是否继续循环

```python
#跳转语句
# for ite in range(10):
#     if ite ==3:
#         break
#     print(ite)
# else:
#     print("ove")

for ite in range(10):
    if ite ==3:
        continue
    print(ite)
else:
    print("over11")
```





## 容器类型的数据

Python内置的数据类型如序列（列表、元组等）、集合和字典等可以容纳多项数据，我们称它们为容器类型的数据



### 序列  

​	序列（sequence）是一种可迭代的、元素有序的容器类型的数据
	序列包括列表（list）、字符串（str）、元组（tuple）和字节序列（bytes）等。

#### 序列的索引操作

​	序列中的元素都是有序的，每一个元素都带有序号，这个序号叫作索引。索引有正值索引和负值索引之分。 --》通过下标运算符访问序列中的元素
序列的加和乘操作

```python
#序列 索引
a="Hedzx"

print(a[0],a[4],a[-1],a[-5]) #下标 >= 数组长度 会报错   [0,4] [-5,-1]
print(max(a),min(a),len(a))  #max() 函数用于返回最后一个元素 ？？  min()函数用于返回第一个元素 len()函数用于获取序列的长度
```



#### 加 、乘 运算符也可以用于序列中的元素操作。*

*加（+）运算符可以将两个序列连接起来，乘（*）运算符可以将两个序列重复多次。

```python
#序列 加和乘操作
aa="Hedzx"

print(aa*2)
aa*=2
print(aa,aa+',woll')
```



#### 序列的切片操作

​	序列的切片（Slicing）就是从序列中切分出小的子序列。
	语法形式为[start：end：step]  start是开始索引，end是结束索引，step是步长（切片时获取的元素的间隔，可以为正整数，也可以为负整数）
	注意：切下的小切片包括start位置的元素，但不包括end位置的元素，start和end都可以省略

```python
#序列 切片操作
aaa="Hedzx"

print(aaa[1:3],aaa[:3],aaa[0:],aaa[:],aaa[0:5],a[1:-1])
print(aaa[1:5:4],aaa[::-1])  #aaa[::-1] 是倒序排列
```



#### 成员测试运算符

​	成员测试运算符 in和not in，in用于测试是否包含某一个元素，not in用于测试是否不包含某一个元素。

```python
#序列 成员测试 in   not in
aaaa="Hedzx"

print('e'in aaaa,'E'in aaaa,'E'not in aaaa)
```



### 列表

​	列表（list）是一种可变序列类型，我们可以追加、插入、删除和替换列表中的元素

#### 创建列表

​	创建列表有两种方法。
	1 list（iterable）函数：参数iterable是可迭代对象（字符串、列表、
	元组、集合和字典等）。
	2 [元素1，元素2，元素3，⋯]：指定具体的列表元素，元素之间以
	逗号分隔，列表元素需要使用中括号括起来

```python
#列表  创建列表
b=[10,20,30,40,50,90]
c=[] #创建空列表
d=["ddd",23,44,'xx'] #创建 字符串和数字的混合列表 列表每个元素后面都有一个逗号 最后一个元素可以省略
e=list("dddkklloecvd")  #list 里面参数是序列对象

print(b,c,d,e)
```



#### 追加元素

​	列表是可变的序列对象，列表可以追加元素。
	1 在列表中追加单个元素时，可以使用列表的append（x）方法。
	2 在列表中追加多个元素时，可以使用加（+）运算符或列表的extend（t）方法。

```python
#列表  追加元素
list =[20,10,60,80,0]
list.append(11)  #在列表后追加一个元素 不能追加多个
t=['ww',22]
l=[33,44]

print(list,list+t,list.extend(l)) #list.extend(l) 方法不能直接放到打印地方 先计算在打印
list.extend(t)
print(list)
```



#### 插入元素

​	想向列表中插入元素时，可以使用列表的list.insert（i，x）方法，其中，i指定索引位置，x是要插入的元素

```python
#列表  插入元素
list =[20,10,60,80,0]
list.insert(2,80)

print(list,list.insert(1,11))
```

#### 替换元素

​	想替换列表中的元素时，将列表下标索引元素放在赋值符号（=）的左边，进行赋值即可

```python
#列表  替换元素
list =[20,10,60,80,0]
list[0]=100

print(list)
```

#### 删除元素

​	想在列表中删除元素时，可使用列表的list.remove（x）方法，如果找到匹配的元素x，则删除该元素，如果找到多个匹配的元素，则只删除第一个匹配的元素

```python
#列表  删除元素
list =[20,10,60,80,0]
list.remove(20)

print(list)

```



### 元组

​	元组（tuple）是一种不可变序列类型

#### 创建元组

​		创建元组时有两种方法。
		1 tuple（iterable）函数：参数iterable是可迭代对象（字符串、列表、元组、集合和字典等）。
		2 （元素1，元素2，元素3，⋯）：指定具体的元组元素，元素之间以逗号分隔。对于元组元素，可以使用小括号括起来，也可以省略小括号。

```python
# 元组  创建元组
li=1,2,3
li1=(1,2,3)
li2=("jj",1,2)
li3=tuple("hhheccl")
li4=1,
li5=(1,)#创建一个元素的元组后面的逗号不能省略

print(li,li1,li2,li3,li4,li5,type(li5))
```



#### 元组拆包

​		创建元组，并将多个数据放到元组中，这个过程被称为元组打包。
		与元组打包相反的操作是拆包，就是将元组中的元素取出，分别赋值给不同的变量。

```python
# 元组  元组拆包
s_id,s_name=(101,'zhangsan')

print(s_id,s_name)
```



### 集合

​	集合（set）是一种可迭代的、无序的、不能包含重复元素的容器类型的数据。

#### 创建集合

​		我们可以通过以下两种方式创建集合。
		1 set（iterable）函数：参数iterable是可迭代对象（字符串、列表、元组、集合和字典等）。
		2 {元素1，元素2，元素3，⋯}：指定具体的集合元素，元素之间以逗号分隔。对于集合元素，需要使用大括号括起来。

```python
# 集合  创建集合
se=set("hhheddsls")
se1={10,20,55,88}

print(se,se1,type(se))
```



#### 修改集合

​		修改集合类似于修改列表，可以向其中插入和删除元素。修改可变集合有如右所示的常用方法
		add（elem）：添加元素，如果元素已经存在，则不能添加，不会抛出错误。
		remove（elem）：删除元素，如果元素不存在，则抛出错误。
		clear（）：清除集合

```python
# 集合  修改集合
se2={'zhangsan','lisi','wangwu'}
se2.add('dongliu')

print(se2)
se2.remove('lisi')  #删除时  如果集合中不存在该元素 则会抛出错误

print(se2,'lisi' in se2)
se2.clear()
print(se2)
```



#### 字典

​	字典（dict）是可迭代的、通过键（key）来访问元素的可变的容器类型的数据
	字典由两部分视图构成：键视图和值视图。键视图不能包含重复的元素，值视图能。在键视图中，键和值是成对出现的

#### 创建字典

​		我们可以通过以下两种方法创建字典。
		1 dict（）函数
		2 {key1：value1，key2：value2，...，key_n：value_n}：指定具体的字典键值对，键值对之间以逗号分隔，最后用大括号括起来。

```python
# 字典  创建字典
dict0={101:'zhangsan',102:'lisi'}
dict1=dict({101:'zzz',102:'lll'})
dict2=dict(((101,'zs'),(100,'ls')))
dict3=dict(zip([11,12],['xx','yy']))

print(dict0,dict1,dict2,dict3)
```



#### 修改字典

​		字典可以被修改，但都是针对键和值同时操作的，对字典的修改包括添加、替换和删除。

```python
# 字典  修改字典
dict0={101:'zhangsan',102:'lisi'}
dict0[103]='wangwu'
dict0[102]='ssss'
di=dict0.pop(102)  #使用字典的pop()方法 删除键值对 返回值是key 对应的value值

print(dict0[101],dict0,di)
```



#### 访问字典视图

​		通过字典中的三种方法访问字典视图
		items（）：返回字典的所有键值对视图。

​		keys（）：返回字典键视图

​		values（）：返回字典值视图
		

```python
# 字典  访问字典视图
dict0={101:'zhangsan',102:'lisi'}
# ll=list(dict0.keys()) #这里会报错？？？

print(dict0.items(),dict0.keys())
```

#### 遍历字典 

```python
# 字典  遍历字典
dict0={101:'zhangsan',102:'lisi'}
#遍历键
for item in dict0.keys():
    print("学号：",item)
#遍历值
for it in dict0.values():
    print("姓名：",it)
#遍历键值对
for s_id,s_name in dict0.items():
    print("学号{0}的学生姓名是：{1}",s_id,s_name)
```



#### 总结

​	1  序列元素是有序的 其中列表可变 元组不可变

​	2  集合元素是无序的 且不能重复

​	3  字典通过键来访问元素 由键视图和值视图组成  键视图不能包含重复的元素 值视图可以包含相同元素 













