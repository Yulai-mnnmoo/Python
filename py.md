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

注意：

```python
s="Hello World"

print(s[-5:],s[-5:0])  #截取时 start end  要么都为正 要么都为负  否则没有返回值

s="World"

print(s[-1::-1],s[::-1])#倒序  
```



## 字符串

### 字符串的表示方式

​	三种表示方式：普通字符串、原始字符串和长字符串。

#### 普通字符串

​	普通字符串指用单引号（'）或双引号（＂）括起来的字符串

```python
#普通字符串
a="hrlllo"
s='\u0048\u0065'

print(a,s)
```

​	常用的转义符 

![](D:\work\个人包\Python\图片\常用转义符.png)

```python
# 转义字符应用
aa='hh\nkk'
b="hh\u000a kk"
print(aa,b,'hh\tkk','hh\"kk','hh\\kk')
```



#### 原始字符串

​	原始字符串(row string)表示，原始字符串中的特殊字符不需要被转义，按照字符串本来的样子展示。

```python
# 原始字符串
aaa='hh\nkk'
print(aaa,r'hh\nkk')
```



#### 长字符串

​	要使用字符串表示一篇文章，其中包含了换行、缩进等排版字符，则可以使用长字符串表示。对于长字符串，要使用三个单引号（'''）或三个双引号（＂＂＂）括起来。

```python
# 长字符号
s='''ddsdsfdsfdsf颠三倒四大多
数的SV方式'''

print(s)
```



### 字符串与数字的相互转换

#### 将字符串转换为数字 

​	可以使用int（）和float（）实现，如果成功则返回数字，否则引发异常

#### 将数字转换为字符串

​	将数字转换为字符串，可以使用str（）函数，str（）函数可以将很多类型的数据都转换为字符串。

```python
# 字符串相互转化
i=int("80")
l=float("80")

print(i,l)
ii=str(80)
ll=str(80.1)
k=str(True)

print(ii,ll,k)

```



### 格式化字符串

​	使用format()方法，不仅可以实现字符串拼接，还可以格式化字符串

#### 使用占位符

​	要想将表达式的计算结果插入字符串中，则需要用到占位符。对于占位符，使用一对大括号（{}）表示

#### 格式化控制符

​	在占位符中还可以有格式化控制符，对字符串的格式进行更加精准的控制。
	格式化控制符位于占位符索引或占位符名字的后面，之间用冒号分隔，语法：{参数序号：格式控制符}或{参数名：格式控制符}
![](D:\work\个人包\Python\图片\格式化控制符.png)

```python
# 格式化字符串
p=20

print('p*p=',str(p*p),'p*p={}'.format(p*p),'{0}*{1}={2}'.format(p,p,p*p))
name="Tom"
money=5594.20
age=26

print("{0:s}的年龄是{1:d},工资是{2:0.2f}".format(name,age,money))
print("{0:s}的年龄是{1:d},工资是{2:G}".format(name,age,money))
print("{0:s}的年龄是{1:d},工资是{2:e}".format(name,age,money))
print("{0:s}的年龄是{1:x},工资是{2:0.2f}".format(name,age,money))
```



### 操作字符串

#### 字符串查找

​	字符串的find（）方法用于查找子字符串。该方法的语法为str.find（sub[，start[，end]]），表示：在索引start到end之间查找子字符串sub，如果找到，则返回最左端位置的索引；如果没有找到，则返回-1

#### 字符串替换

​	可以使用replace（）方法替换匹配的子字符串，返回值是替换之后的字符串。该方法的语法为str.replace（old，new[，count]），表示：用new子字符串替换old子字符串

#### 字符串分割

​	可以使用split（）方法，按照子字符串来分割字符串，返回字符串列表对象。该方法的语法为str.split（sep=None，maxsplit=-1），表示：使用sep子字符串分割字符串str
	maxsplit是最大分割次数，如果maxsplit被省略，则表示不限制分割次数
	

```python
# 操作字符串
sr='ddsskkllea'

print(sr.find('e'),sr.find('d',1),sr.find('l',4,8))  #找得到值返回 下标  找不到值 返回-1
print(sr.replace('dd','kk')) #返回值 是改变后的字符串
print(sr.replace('k','|',2)) #返回值 是改变后的字符串
print(sr.split('k'),sr.split('k',1))  #返回值是数组   maxsplit是最大分割次数
```

​		





## 函数

​	函数具有函数名、参数和返回值。可以在中但是类之外定义，作用域是当前模块，称为函数；可以在别的函数中定义，称为嵌套函数；可以在类中定义，称为方法。

### 定义函数

​	def 函数名（形式参数列表）:
		函数体
		return返回值

```python
#定义函数
def rect_area(width,height):
    area=width*height
    return area

def print_area(width,height):
    a=width*height
    print('{0}x{1}的长方形的面积是:{2:0.2f}',width,height,a)
```



### 调用函数

#### 	使用位置参数调用函数

​		在调用函数时传递的实参与定义函数时的形参顺序一致，这是调用函数的基本形式

#### 	使用关键字参数调用函数

​		在调用函数时可以采用“关键字=实参”的形式，其中，关键字的名称就是定义函数时形参的名称。

```python
#调用函数  使用位置参数调用
r_area = rect_area(200,100)
print('{0}x{1}的长方形的面积是:{2:0.2f}'.format(200,100,r_area))

#调用函数  使用关键字产参数调用
r_area = rect_area(width=200,height=100)
print('{0}x{1}的长方形的面积是:{2:0.2f}'.format(200,100,r_area))  #关键字的名称定义函数时形参的名称  不在受顺序限制

```



### 参数的默认值

​	调用时没有提供参数，则使用默认值

```python
#参数的默认值
def make_coffee(name='冰美式'):
    return '制作一杯{0}'.format(name)

coffee1=make_coffee('xxx')
coffee2=make_coffee() #不传参数时 使用默认值

print('kkk',coffee1,coffee2)
```



### 可变参数

​	Py中的函数可以定义接收不确定数据的参数，即可变参数，可变参数有两种，即在参数前加*或**

#### 	基于元组的可变参数（*可变参数）	

​		*可变参数在函数中被组装成一个元组。

```python
#可变参数   基于元组
def sum(*numbers):
    total =0.0
    for i in numbers:
        total+=i
    return total

print(sum(10,30,50))
print(sum(20))

```



#### 	基于字典的可变参数（**可变参数）

​		**可变参数在函数中被组装成一个字典。

```python
#可变参数   基于字典
def show_info(**info):
    for key,value in info.items():
        print('{0} -- {1}'.format(key,value))

show_info(s_sto=1002,s_name='zhangsan')
show_info(s_sto=1001,s_name='lisi',sex=True)
```



### 函数中变量的作用域

​	变量可以在模块中创建，作用域（变量的有效范围）是整个模块，被称为全局变量。变量也可以在函数中创建，在默认情况下作用域是整个函数，被称为局部变量。

```python
#变量的作用域
x=20

def f1():
    # global x    global变量 将局部变量提升为全局变量
    x=10
    print('x={0}'.format(x))

f1()
print('xxx={0}'.format(x))
```



### 函数类型

​	Python中的任意一个函数都有数据类型，这种数据类型是function，被称为函数类型。

#### 	理解函数类型

​		函数类型的数据与其他类型的数据是一样的，任意类型的数据都可以作为函数返回值使用，还可以作为函数参数使用

```python
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
```



#### 	过滤函数filter（）

​		在Python中定义了一些用于数据处理的函数，如filter（）和map（）等

```python
#过滤函数
def f3(x):
    return x>50

data1=[20,30,50,53,83,22]
filterd=filter(f3,data1)
data2=list(filterd)

print(data2)
```

​	

#### 	映射函数map（）

​		map（）函数用于对容器中的元素进行映射（或变换）



### lambd

```python
#映射函数
def f4(x):
    return x*2

data3=list(map(f4,data1))

print(data3)
```

### lambda（）函数   --  匿名函数

​	Python中使用lambda关键字定义匿名函数 
	语法：lambda参数列表：lambda体
	lambda（）函数与有名称的函数一样，都是函数类型	

```python
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
```


​		
​	



## 类与对象

### 面向对象

​	类和对象都是面向对象中的重要概念。面向对象是一种编程思想，即按照真实世界的思维方式构建软件系统

### 定义类

​	Python中的数据类型都是类，我们可以自定义类，即创建一种新的数据类型。
	语法： class 类名（父类）:
				类体
		pass语句只用于维持程序结构的完整性，pass语句占位

```python
#定义类
class Car(object):
    pass
```



### 创建对象

​	类相当于一个模板，依据这样的模板来创建对象，就是类的实例化，所以对象也被称为“实例”

```python
#创建对象
car= Car()
```



### 类的成员

​	成员变量也被称为数据成员，保存了类或对象的数据。例如，学生的姓名和学号
	构造方法是一种特殊的函数，用于初始化类的成员变量。
	成员方法是在类中定义的函数。
	属性是对类进行封装而提供的特殊方法。

![](D:\work\个人包\Python\图片\类的成员.png)

![](D:\work\个人包\Python\图片\类变量类方法实例变量实例方法.png)

#### 实例变量	

​	实例变量就是对象个体特有的“数据”，例如狗狗的名称和年龄等。	

​	对实例变量通过"对象.实例变量"形式访问

```python
# 实例变量
class Dog:
    def __init__(self,name,age):  # __int__  是构造方法，构造方法用来初始化实例变量
        self.name=name
        self.age=age

d=Dog('shan',2)

print('狗子名字是{0}，今年{1}岁了'.format(d.name,d.age)) #对实例变量通过"对象.实例变量"形式访问

```



#### 构造方法	

​	类中的__init__（）方法是一个非常特殊的方法，用来创建和初始化实例变量，这种方法就是“构造方法”	在定义__init__（）方法时，它的第1个参数应该是self，之后的参数用来初始化实例变量。调用构造方法时不需要传入self参数。

```python
# 构造方法
class Dogs:
    def __init__(self,name,age,sex='雌性'):  # __int__  是构造方法，构造方法用来初始化实例变量
        self.name=name
        self.age=age
        self.sex=sex

d1=Dogs('球球',3)
d2=Dogs('哈哈',1,'雌性')
d3=Dogs(name='拖布',sex='雄性',age=1)

print('{0}:{1}岁{2}'.format(d1.name,d1.age,d1.sex))
print('{0}:{1}岁{2}'.format(d2.name,d2.age,d2.sex))
print('{0}:{1}岁{2}'.format(d3.name,d3.age,d3.sex))
```



#### 实例方法	

​	实例方法与实例变量一样，都是某个实例（或对象）个体特有的方法	

​	定义实例方法时，它的第1个参数也应该是self，这会将当前实例与该方法绑定起来，这也说明该方法属于实例。在调用方法时不需要传入self，类似于构造方法

```python
# 实例方法
class Dog1:
    def __init__(self,name,age,sex='雌性'):  # __int__  是构造方法，构造方法用来初始化实例变量
        self.name=name
        self.age=age
        self.sex=sex

    def run(self):
        print('{0}在跑。。。'.format(self.name))
    def speak(self,sound):      #定义实例方法 第一个参数是self 第二个参数是sound
        print('{0}在叫：{1}'.format(self.name,sound))

dog1=Dog1('球球',2)
dog1.run()
dog1.speak('旺旺')
```



#### 类变量	

​	类变量是属于类的变量，不属于单个对象。	对类变量通过"类名.类变量"形式访问

```python
#类变量
class Account:
    interest_rate=0.0568  #类变量利率
    def __init__(self,owner,amount):
        self.owner=owner
        self.amount=amount

account=Account('Tony',80000.0)

print('账户名：{0}'.format(account.owner))
print('余额：{0}'.format(account.amount))
print('利率：{0}'.format(Account.interest_rate))   #对类变量通过‘类名.类变量’形式访问
```



#### 类方法	

​	类方法与类变量类似，属于类，不属于个体实例。在定义类方法时，它的第1个参数不是self，而是类本身。	

​	定义类方法需要装饰器，装饰器以@为开头的修饰函数、方法和类，用来约束它们	对类方法可以通过"类名.类方法"形式访问

```python
#类方法
class Account1:
    interest_rate=0.0668  #类变量利率
    def __init__(self,owner,amount):
        self.owner=owner
        self.amount=amount
    @classmethod
    def interert_by(cls,amt): #cls 代表类自身
        return cls.interest_rate * amt

interest = Account1.interert_by(12000.0) #对类方法 用’类名.类方法‘形式访问

print('利息计算：{0:.4f}'.format(interest))

# 注意 ： 类方法可以访问类变量和其他类方法 但不可以访问其他实例变量和其他实例变量
```



### 封装性

​	封装性是面向对象重要的基本特性之一。封装隐藏了对象的内部细节，只保留有限的对外接口，外部调用者不用关心对象的内部细节，使得操作对象变得简单

#### 私有变量

​	为了防止外部调用者随意存取类的内部数据（成员变量），内部数据（成员变量）会被封装为“私有变量”。外部调用者只能通过方法调用私有变量。
	默认情况下，Python中的变量是公有的，可以在类的外部访问它们。如果想让它们成为私有变量，则在变量前加上双下画线（__）即可

```python
#私有变量
class Account2:
    __interest_rate=0.0568  #类变量利率
    def __init__(self,owner,amount):
        self.owner=owner
        self.__amount=amount
    def desc(self):
        print('{0}金额：{1}利率：{2}'.format(self.owner,self.__amount,Account2.__interest_rate))

ac=Account2('zahngsan',800000.0)
ac.desc()

print(ac.owner)
# print(ac.__amount)    发生错误   在类的外部 不可以访问私有变量
# print(Account2.__interest_rate)  发生错误   在类的外部 不可以访问私有变量
```



#### 私有方法

​	私有方法与私有变量的封装是类似的，在方法前加上双下画线（__）就是私有方法

```python
#私有方法  类似私有变量
class Account3:
    __interest_rate=0.0568  #类变量利率
    def __init__(self,owner,amount):
        self.owner=owner
        self.__amount=amount
    def __get_info(self):  #定义私有方法
        print('{0}金额：{1}利率：{2}'.format(self.owner,self.__amount,Account3.__interest_rate))
    def desc(self):
        self.__get_info()     #在类的内部 可以访问私有方法

am=Account3('zahngsan1',800000.0)
am.desc()
#am.__get_info()   #在类得外部不能访问私有变量  发生错误
```



#### 使用属性

​	为了实现对象的封装，在一个类中不应该有公有的成员变量，这些成员变量应该被设计为私有的，然后通过公有的set赋值）和get（取值）方法访问。

```python
#使用属性  全设置为私有变量 实现封装  然后用set get方法 获取
class Account4:
    __interest_rate=0.0568  #类变量利率
    def __init__(self,owner,amount):
        self.owner=owner
        self.__amount=amount
    def get_amount(self):
        return self.__amount
    def set_amount(self,amount):
        self.__amount=amount

    def get_rate(self):
        return self.__interest_rate
    def set_rate(self,interest_rate):
        self.__interest_rate=interest_rate

acc=Account4('zhangsan222',80000.0)
print('{0}金额：{1}利率：{2}'.format(acc.owner,acc.get_amount(),acc.get_rate()))
acc.set_amount(60000.0)
acc.set_rate(0.0666)
print('修改后的 {0}金额：{1}利率：{2}'.format(acc.owner,acc.get_amount(),acc.get_rate()))
###############################################
#替代set  get 方法
class Do:
    def __init__(self,name,age):
        self.name =name
        self._age = age
    @property      #定义属性age的get方法 使用 @property 修饰 方法名就是属性名
    def age(self):
        return self._age
    @age.setter     #定义属性age的set方法 使用  @age.setter 修饰 方法名就是属性名
    def age(self,age):
        self._age=age
do=Do('拖布',1)

print('狗子年龄：{0}'.format(do.age))  #这样可以 通过属性取值
do.age=3        #可以 通过属性修改值
print('修改后 狗子年龄：{0}'.format(do.age))
```



### 继承性

​	继承性也是面向对象重要的基本特性之一。特殊类拥有一般类的全部数据和操作，可称之为子类继承父类。

#### Python中的继承

​	在Python中声明子类继承父类，语法很简单，定义类时在类的后面使用一对小括号指定它的父类就可以了

```python
#继承   子类继承父类是 只有公有的成员变量和方法才能被继承
class Animal:
    def __init__(self,name):
        self.name=name
    def show_info(self):
        print('动物的名字是：{0}'.format(self.name))
    def move(self):
        print('动了。。。')
class Cat(Animal):  #定义子类
    def __init__(self,name,age):
        super().__init__(name)  #调用父类构造方法  初始化成员变量
        # self.name=name
        self.age=age

cat =Cat('Tom',3)
cat.move()
cat.show_info()
```



#### 多继承

​	在Python中，当子类继承多个父类时，如果在多个父类中有相同的方法或成员变量，则子类优先继承左边父类中的成员方法或成员变量，从左到右继承级别从高到低

```python
#多继承    子类优先继承左边父类中的成员方法或成员变 量，从左到右继承级别从高到低
class Horse:
    def __init__(self,name):
        self.name=name
    def show_info(self):
        print('马的名字：{0}'.format(self.name))
    def run(self):
        print('马跑...')

class Donkey:
    def __init__(self,name):
        self.name=name
    def show_info(self):
        print('驴的名字：{}'.format(self.name))
    def run(self):
        print('驴跑...')
    def roll(self):
        print('驴打滚...')

class Mule(Horse,Donkey):
    def __init__(self,name,age):
        super().__init__(name)
        self.age =age
m=Mule('lisi',2)
m.run()         #  两个父类都有run方法 调用前者 马的run方法
m.roll()        #只有父类驴友roll方法 所以调用 驴的roll方法
m.show_info()   #  两个父类都有show_info方法 调用前者 马的show_info方法
```



#### 方法重写

​	如果子类的方法名与父类的方法名相同，则在这种情况下，子类的方法会重写（Override）父类的同名方法。		

```python
#多继承    子类优先继承左边父类中的成员方法或成员变 量，从左到右继承级别从高到低
class Horse:
    def __init__(self,name):
        self.name=name
    def show_info(self):
        print('马的名字：{0}'.format(self.name))
    def run(self):
        print('马跑...')

class Donkey:
    def __init__(self,name):
        self.name=name
    def show_info(self):
        print('驴的名字：{}'.format(self.name))
    def run(self):
        print('驴跑...')
    def roll(self):
        print('驴打滚...')

class Mule(Horse,Donkey):
    def __init__(self,name,age):
        super().__init__(name)
        self.age =age
    def show_info(self):     #方法重写
        print('骡子的名字是：{}'.format(self.name))
m=Mule('lisi',2)
m.run()         #  两个父类都有run方法 调用前者 马的run方法
m.roll()        #只有父类驴友roll方法 所以调用 驴的roll方法
m.show_info()   #  两个父类都有show_info方法 调用前者 马的show_info方法
```



### 多态性 

​	多态性也是面向对象重要的基本特性之一。“多态”指对象可以表现出多种形态

#### 继承与多态

​	在多个子类继承父类，并重写父类方法后，这些子类所创建的对象之间就是多态的。这些对象采用不同的方式实现父类方法

```python
#多态性
class Animal1:
    def speak(self):
        print('动物叫了，但不知道是那种动物')

class Cat1(Animal1):
    def speak(self):
        print('小猫喵喵叫。。。')

class Dogd(Animal1):
    def speak(self):
        print("小狗旺旺叫。。。")

an1 =Dogd()
an2=Cat1()
an1.speak()
an2.speak()
```



#### 鸭子类型测试与多态

​	Python的多态性更加灵活，支持鸭子类型测试
	Python解释器不检查发生多态的对象是否继承了同一个父类，只要它们有相同的行为（方法），它们之间就是多态的

```python
#鸭子类型测试与多态  鸭子类型测试:若看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟可以被称为鸭子

def start(obj):
    obj.speak()
class Animal2:
    def speak(self):
        print('动物叫了，但不知道是那种动物')

class Cat2(Animal2):
    def speak(self):
        print('小猫喵喵叫。。。')

class Dogd1(Animal2):
    def speak(self):
        print("小狗旺旺叫。。。")
class Car3:
    def speak(self):
        print('小汽车滴滴叫。。。')

start(Dogd1())
start(Cat2())
start(Car3())
```







## 异常

### 除零异常 

​	在数学中，任何整数都不能除以0，如果在计算机程序中将整数除以0，则会引发异常   ZeroDivisionError

```python
#除0异常
i=input('请输入数字：')
n=8888
result=n/int(i)

print(result)
print('{0}除以{1}等于{2}'.format(n,i,result))

```



### 捕获异常

​	不能防止用户输入0，但在出现异常后我们能捕获并处理异常，不至于让程序发生终止并退出

#### 	try-except语句

​		在try代码块中包含在执行过程中可能引发异常的语句，如果没有发生异常，则跳到except代码块执行，这就是异常捕获
			语法：try:
					<可能引发异常的语句>
				  except[异常类型]：
					<处理异常>

```python
#捕获异常  
i=input('请输入数字：')
n=8888
try:
    result=n/int(i)

    print(result)
    print('{0}除以{1}等于{2}'.format(n,i,result))
except ZeroDivisionError as e:  #指定具体的异常类型
    print('不能除以0，异常：{}'.format(e))
```



#### 	多个except代码块

​			语法：try:
					<可能引发异常的语句>
				  except[异常类型1]
					<处理异常>
				  except[异常类型2]
					<处理异常>
				  ...
				  except：
					<处理异常>

```python
#捕获异常  多个except代码块
i=input('请输入数字：')
n=8888
try:
    result=n/int(i)

    print(result)
    print('{0}除以{1}等于{2}'.format(n,i,result))
except ZeroDivisionError as e:  #指定具体的异常类型
    print('不能除以0，异常：{}'.format(e))
except ValueError as e:  #指定具体的异常类型
    print('输入的是无效数字，异常：{}'.format(e))
```



#### 	多重异常捕获

​		存在多个except代码块，会客观上增加代码，可以合并处理

```python
#多重捕获异常
i=input('请输入数字：')
n=8888
try:
    result=n/int(i)

    print(result)
    print('{0}除以{1}等于{2}'.format(n,i,result))
except (ZeroDivisionError,ValueError) as e:  #指定具体的异常类型
    print('不能除以0，异常：{}'.format(e))
```



#### 	try-except语句嵌套

​			try-except语句还可以嵌套

​	

```python
# try-except语句嵌套
i=input('请输入数字：')
n=8888
try:
    i2=int(i)
    try:
        result = n / int(i)
        print('{0}除以{1}等于{2}'.format(n, i, result))
    except ZeroDivisionError as e1:
        print('不能除以0，异常：{}'.format(e1))
except ValueError as e2:  #指定具体的异常类型
    print('输入的是无效数字，异常：{}'.format(e2))
```



### finally代码块释放资源

​	有时在try-except语句中会占用一些资源，例如打开的文件、网络连接、打开的数据库及数据结果集等都会占用计算机资源，需要程序员释放这些资源。为了确保这些资源能够被释放，可以使用finally代码块
		语法：try:
				<可能引发异常的语句>
			  except[异常类型1]
				<处理异常>
			  except[异常类型2]
				<处理异常>
			  ...
			  except：
				<处理异常>
			  finally:
				<释放资源>

```python
#finally
i=input('请输入数字：')
n=8888
try:
    i2=int(i)
    try:
        result = n / int(i)
        print('{0}除以{1}等于{2}'.format(n, i, result))
    except ZeroDivisionError as e1:
        print('不能除以0，异常：{}'.format(e1))
except ValueError as e2:  #指定具体的异常类型
    print('输入的是无效数字，异常：{}'.format(e2))

finally:
    # 释放代码资源
    print("资源释放...")
```

### 自定义异常类

​	为了提高代码的可重用性，自己编写一些Python类库，实现自定义异常类，需要继承Exception类或其子类

```python
# 自定义异常
class ZhiException(Exception):
    def __init__(self,message):
        super().__init__(message)
```



### 手动引发异常

​	到目前为止，接触到的异常都是由于解释器引发的，亦可以通过raise语句手动引发

```python
# 手动引发异常
i=input('请输入数字：')
n=8888
try:
    result=n/int(i)

    print(result)
    print('{0}除以{1}等于{2}'.format(n,i,result))
except ZeroDivisionError as e:  #指定具体的异常类型
    #print('不能除以0，异常：{}'.format(e))
    raise ZhiException('不能除以0')
except ValueError as e:  #指定具体的异常类型
    #print('输入的是无效数字，异常：{}'.format(e))
    raise ZhiException('输入的是无效数字')
```





## 常用的内置模块

### 数学计算模块 

​	math 在math模块中包含数学运算相关的函数等，例如指数、对数、平方根和三角函数等

![](D:\work\个人包\Python\图片\math模块常用函数.png)

```python
#数学计算模块  math
import math

print(math.ceil(2.4),math.floor(2.4),math.ceil(-2.4),
      math.floor(-2.4),math.pow(5,3),math.sqrt(3.6),math.log(125,5),
      math.degrees(0.5*math.pi),math.radians(180/math.pi),math.sin(0.3))
```



### 日期时间模块

datetime模块中提供了以下几个类：
	datetime：包含时间和日期。
	date：只包含日期。
	time：只包含时间。
	timedelta：计算时间跨度。
	tzinfo：时区信息。

#### datetime类

​	datetime类表示日期和时间等信息，我们可以使用如下构造方法创建datetime对象:
	datetime.datetime(year,month,day,hour=0,minute=0,second=0,microsecond=0,tzinfo=None)
	常用方法：
		datetime.today（）：返回当前的本地日期和时间
		datetime.now（tz=None）：返回指定时区的当前日期和时间，参数tz用于设置时区，如果参数tz为None或省略，则等同于today（）。
		datetime.fromtimestamp（timestamp，tz=None）：返回与UNIX时间戳对应的本地日期和时间。UNIX时间戳是从1970年1月1日00：00：00开始到现在为止的总秒数。

![](D:\work\个人包\Python\图片\datatime类参数.png)

```python
#日期时间模块 datetime类
import datetime

# print(datetime.datetime(2020,2,30))  #30 指定的day 参数超出范围 会发生ValueError 异常
print(datetime.datetime(2020,1,29))
print(datetime.datetime(2020,1,29,0,0))
#print(datetime.datetime(2020,1,29,23,60,59,10000)) #60 指定的minute 参数超出范围 会发生ValueError 异常
print(datetime.datetime(2020,1,29,23,56,59,10000))
print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.fromtimestamp(9999999999.999)) #在python中  时间戳的单位是秒
```



#### date类

​	date类表示日期信息，我们可以使用如下构造方法创建date对象：
	datetime.date(year,month,day)
	常用方法：
		date.today（）：返回当前的本地日期
		date.fromtimestamp（timestamp）：返回与UNIX时间戳对应的本地日期

```python
#日期时间模块 date类
import datetime

print(datetime.date(2022,2,28))
print(datetime.date.today())
print(datetime.date.fromtimestamp(9999999999.999))
```



#### time类

​	time类表示一天中的时间信息，我们可以使用如下构造方法创建time对象：
	datetime.time(hour=0,minute=0,second=0,microsecond=0,tzinfo=None)

```python
#日期时间模块 time类
import datetime

print(datetime.time(23,59,59,10000))
#print(datetime.time(23,60,59,10000))  #分 60 超出范围
```



#### 计算时间跨度类——timedelta

​	timedelta用于计算datetime date类 time类对象的时间间隔，可以使用如下构造方法创建对象：
				  			     datetime.timedelta(days=0,seconds=0,microsecond=0,milliseconds=0,minutes=0,hours=0,weeks=0)

![](D:\work\个人包\Python\图片\timedelta类参数.png)

```python
#日期时间模块 timedelta类
import datetime
d=datetime.datetime.today()
delta=datetime.timedelta(10)   #创建10天后的对象
d+=delta
d1=datetime.date(2020,1,1)
dalta1=datetime.timedelta(weeks=5)  #创建五周后的对象
d1-=dalta1

print(d,d1)
```



#### 将日期时间与字符串相互转换

​	1.将日期时间对象转换为字符串时，称之为日期时间格式化 
		使用strftime（）方法进行日期时间的格式化
	2.将字符串转换为日期时间对象的过程，叫作日期时间解析		

​		使用datetime.strptime（date_string，format）类方法进行日期时间解析。

![](D:\work\个人包\Python\图片\常用的日期和时间格式控制符.png)

```python
#字符串时间格式转化
import datetime
d=datetime.datetime.today()
d.strftime('%Y-%m-%d %H:%M:%S') #设置日期时间格式化

print(d)
d.strftime('%Y-%m-%d')

print(d)

str_date='2020-02-29 10:40:26'
date=datetime.datetime.strptime(str_date,'%Y-%m-%d %H:%M:%S')  #将一个字符串按照指定格式破解为日期时间对象
```



### 正则表达式模块  --  re

​	正则表达式指预先定义好一个“字符串模板”，通过这个“字符串模板”可以匹配、查找和替换那些匹配“字符串模板”的字符串

#### 字符串匹配

​	字符串匹配指验证一个字符串是否符合指定的“字符串模板”，常用于用户输入验证。
	使用match（p，text）函数进行字符串匹配  其中的参数p是正则表达式，即字符串模板，text是要验证的字符串。

```python
#正则 字符串匹配
import re
p=r'\w+@zhijieketang\.com'
email1='tang@zhijieketang.com'

m=re.match(p,email1)   #返回非空的match对象 说明匹配成功
email2='abc@163.com'
m1=re.match(p,email2)   #m1为None 表示匹配失败

print(m,type(m),m1)
```



#### 字符串查找

​	字符串查找指从一个字符串中查找匹配正则表达式的子字符串，常用于数据分析、网络爬虫等数据处理中
	search（p，text）：在text字符串中查找匹配的内容，如果找到，则返回第1个匹配的Match对象，否则返回None。p是正则表达式。
	findall（p，text）：在text字符串中查找所有匹配的内容，如果找到，则返回所有匹配的字符串列表；如果一个都没有匹配，则返回None。

```python
#正则 字符串查找
import re
p=r'\w+@zhijieketang\.com'
text="Tom's email is tang@zhijieketang.com"
text1="Tom's email is abc@163.com"
m=re.search(p,text)
m1=re.search(p,text1)

print(m,m1)  #查找成功返回match对象   查找失败则返回为None

p=r'Java|java|JAVA'
text='I like java and Java and JAVA'

m=re.findall(p,text)  #findall 返回匹配的字符串列表  没有匹配的值 则为None
print(m)
```



#### 字符串替换

​	正则表达式的字符串替换函数是sub（），该函数替换匹配的子字符串
	语法：re.sub(pattern,repl,string,count=0)

```python
#正则 字符串查找
import re
p=r'\d+' #匹配数字出现一次或多次的正则表达式
text='AB12cd34Ef'
replace=re.sub(p," ",text)

print(replace) #返回值是替换过后的字符串
replace=re.sub(p," ",text,count=1)

print(replace) #count=1 表示要替换的最大数量
```



#### 字符串分割

​	split（）函数进行字符串分割该函数按照匹配的子字符串进行字符串分割，返回字符串列表对象
	语法：re.split(pattern,string,maxsplit=0)
	参数pattern是正则表达式；参数string是要分割的字符串；参数maxsplit是最大分割次数；maxsplit的默认值为零，表示分割次数没有限制。

```python
#正则 字符串分割
import re
p=r'\d+' #匹配数字出现一次或多次的正则表达式
text='AB12cd34Ef'
clist=re.split(p,text,maxsplit=0)

print(clist)
clist=re.split(p,text,maxsplit=1)

print(clist)
```





## 文件读写

### 文本文件和二进制文件的区别

​	在文本文件的内部以字符形式存储数据，字符是有编码的；在二进制文件的内部以字节形式存储数据，没有编码概念

### 打开文件

​	使用文件之前要先将文件打开，这通过open（）函数实现。
	语法：open(file,mode='r',encding=None,errors=None)

#### 	file参数

​		用于表示要打开的文件，可以是字符串或整数 
		file是字符串，则表示文件名，文件名既可以是当前目录的相对路径 也可以是绝对路径
		file是整数，则表示一个已经打开的文件

#### 	mode参数

​		用于设置文件打开模式，用字符串表示
		t：以文本文件模式打开文件
		b：以二进制文件模式打开文件
		r：以只读模式打开文件
		w：以只写模式打开文件，不能读内容。 如果文件不存在，则创建文件；如果文件存在，则覆盖文件的内容。
		x：以独占创建模式打开文件，如果文件不存在，则创建并以写入模式打开；如果文件已存在，则引发FileExistsError异常。
		a：以追加模式打开文件，不能读内容。如果文件不存在，则创建文件；如果文件存在，则在文件末尾追加。
		+：以更新（读写）模式打开文件，必须与r、w或a组合使用，才能设置文件为读写模式。

![](D:\work\个人包\Python\图片\文件的打开模式.png)

#### 	encoding参数

​		用来指定打开文件时的文件编码，默认是UTF-8编码，主要用于打开文本文件。

#### 	errors参数

​		errors参数用来指定在文本文件发生编码错误时如何处理  'ignore'  --》 忽略该错误，程序会继续执行
	

```python
#打开文件
f=open('test.txt','w+')  #以w+模式打开文件 如果不存在 则创建文件
f.write("World")

print('创建了test.txt文件 ,world写入到文件中')

f=open('test.txt','r+') #以r+模式打开文件 文件已存在 则覆盖文件内容
f.write('Hello')

print('覆盖了文件内容')

f=open('test.txt','a') #以a模式打开文件 会在文件末尾追加内容
f.write(" ")

print("在文件内容后追加了 空格")

# fname=r'D:\work\个人包\Python\pro_base\test.txt'  #采用原始字符串表示绝对路径文件名 其中的 \ 不需要转义
# fname='D:\\work\\个人包\\Python\\pro_base\\test.txt' #采用普通字符串 其中的 \ 需要转义
fname='D:/work/个人包/Python/pro_base/test.txt'  # 采用【普通字符串表示绝对路径文件名 可将反斜杠(\)改为斜杠(/)
f=open(fname,"a+") #以a+模式打开文件 也会在文件末尾追加内容
f.write("World")
print("在文件内容后追加了 world")
```

打开文件时，a和a+有什么区别？
	a能追加文件，不可读文件；a+可以追加写文件，也可以读文件



### 关闭文件

​	在打开文件后，如果不再使用该文件，则应该将其关闭，会用到close（）方法

#### 在finally代码块中关闭文件

​	保证对文件的操作无论是正常结束还异常结束，都能够关闭文件

```python
#关闭文件  使用finally关闭
f_name='test.txt'
f=None
try:
    f=open(f_name)    #可能引发FileNotFoundError异常
    print("打开文件成功")
    content=f.read()   # 可能引发OSError异常
    print(content)
except FileExistsError as e:
    print("文件不存在")
except OSError as e:
    print("处理OSError异常")
finally:
    if f is not None:  # 判断文件是否有数据 如果有数据 说明文件是已经打开成功了的
        f.close() #关闭文件
        print('关闭文件成功')

```



#### 在with as代码块中关闭文件

​	with as提供了一个代码块，在as后面声明一个资源变量，在with as代码块结束之后自动释放资源
读写文本文件

```python
#关闭文件  使用with as 关闭
f_name='test.txt'
with open(f_name) as f:   #代码结束后自动关闭释放资源  优化代码结构 更简洁
    content = f.read()
    print(content)
```



#### 读写文本文件的相关方法

​	read（size=-1）：从文件中读取字符串，size限制读取的字符数，size=-1指对读取的字符数没有限制。
	readline（size=-1）：在读取到换行符或文件尾时返回单行字符串。如果已经到文件尾，则返回一个空字符串。size是限制读取的字符数，size=-1表示没有限制。
	readlines（）：读取文件数据到一个字符串列表中，每一行数据都是列表的一个元素。
	write（s）：将字符串s写入文件中，并返回写入的字符数。
	writelines（lines）：向文件中写入一个字符串列表。不添加行分隔符，因此通常为每一行末尾都提供行分隔符。
	flush（）：刷新写缓冲区，在文件没有关闭的情况下将数据写入文件中。

### 复制文本文件

```python
#复制文本文件
f_name1='test.txt'

with open(f_name1,'r',encoding='gbk') as f:  #以只读模式 打开文件 注意文件编码是gbk 与字符集的大小没有关系
    lines=f.readlines()   #读取所有数据到一个列表中
    copy_f_name='src_test.txt'
    with open(copy_f_name,'w',encoding='utf-8') as copy_f: #以只写模式 打开文本文件 注意文件编码格式为utf-8
        copy_f.writelines(lines)  #把列表数据lines写到文件中
        print('文件复制成功')

```



### 读写二进制文件

​	二进制文件的读写单位是字节，不需要考虑编码问题

#### 主要读写方法

​	read（size=-1）：从文件中读取字节，size限制读取的字节数，如果size=-1，则读取全部字节。
	readline（size=-1）：从文件中读取并返回一行。size是限制读取的行数，如果size=-1，则没有限制。
	readlines（）：读取文件数据到一个字节列表中，每一行数据都是列表的一个元素。
	write（b）：写入b字节，并返回写入的字节数。
	writelines（lines）：向文件中写入一个字节列表。不添加行分隔符，因此通常为每一行末尾都提供行分隔符。
	flush（）：刷新写缓冲区，在文件没有关闭的情况下将数据写入文件中。
		

### 复制二进制文件

```python
#复制二进制文件
f_name ='logo.png'
with open(f_name,'rb') as f:
    b=f.read()
    copy_f_name='logo2.png'
    with open(copy_f_name,'wb') as copy_f:
        copy_f.write(b)
        print("文件复制成功")
```

​			



## 图形用户界面

### Py中的图形用户界面开发库

#### 	1 Tkinter 

​		Tkinter是Python官方提供的图形用户界面开发库，用于封装Tk GUI工具包，跨平台。但是，Tkinter工具包所包含的控件较少，帮助文档不健全，不便于我们开发复杂的图形用户界面

#### 	2 PyQt

​		PyQt是非Python官方提供的图形用户界面开发库，用于封装Qt工具包，跨平台。若想使用PyQt工具包，则需要额外安装软件包。

#### 	3 wxPython

​		wxPython是非Python官方提供的图形用户界面开发库，也跨平台。它提供了丰富的控件，可用于开发复杂的图形用户界面。它的工具包帮助文档很完善，案例也很丰富

### 安装wxPython

​	在命令提示符（终端）窗口输入pip指令：pip install wxPython     ---> successfully

#### 	第一个wxPython程序

​		编写wxPython程序其实主要是创建窗口和添加控件的过程
		建一个最简单的wxPython程序，则至少需要一个应用（wx.App）对象和一个窗口（wx.Frame）对象。

```python
#coding=utf-8
import wx
#创建应用程序对象
app=wx.App()

#创建窗口对象
frm=wx.Frame(None,title="第一个程序",size=(400,300),pos=(100,100)) #参数1：所在父窗口 没有则用None  参数2：窗口名称   参数3：窗口大小  参数4：窗口位置

#显示窗口
frm.Show()    #窗口 默认是隐藏 需要调用show方法才能显示

#进入主事件循环   事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示和响应用户事件的处理都是通过主事件循环实现的
app.MainLoop()
```

### 自定义窗口类

​	可以自定义窗口（wx.Frame）类，以便于扩展功能

```python

#coding=utf-8
import wx
#创建应用程序对象
app=wx.App()

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='事件处理',size=(500,300),pos=(100,100))
        panel=wx.Panel(parent=self)
        self.staticText=wx.StaticText( parent=panel,label='请单击ok按钮',pos=(110,20))
        b=wx.Button(parent=panel,label='ok',pos=(100,50))  #创建按钮事件
        self.Bind(wx.EVT_BUTTON,self.on_click,b)   #绑定事件 wx.EVT_BUTTON 是事件类型 self_on_click 是事件处理程序 b 是事件源 即按钮对象
    def on_click(self,event): #事件处理程序
        self.staticText.SetLabelText("JJJJlk")
#创建窗口对象
frm=MyFrame()

#显示窗口
frm.Show()    #窗口 默认是隐藏 需要调用show方法才能显示

#进入主事件循环   事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示和响应用户事件的处理都是通过主事件循环实现的
app.MainLoop()

app=wx.App()

```



### 在窗口中添加控件

​	一个面板（Panel）和一个静态文本（StaticText）。面板是一个没有标题栏的容器（可以容纳其他控件的控件）。
	面板被放到窗口中，而静态文本对象被放到面板中

### 事件处理

​	图形界面的控件要响应用户的操作，就必须添加事件处理机制
	主要内容:
		1 事件源：事件发生的场所，就是各个控件，例如按钮事件的事件源是按钮。
		2 事件：wxPython中的事件被封装为事件类wx.Event及其子类，例如按钮事件类是wx.CommandEvent，鼠标事件类是wx.MoveEvent。
		3 事件处理程序：一个响应用户事件的方法。

```python
#coding=utf-8
import wx
#创建应用程序对象
app=wx.App()
#自定义窗口类 MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='事件处理',size=(300,180),pos=(100,100))
        panel=wx.Panel(parent=self)
        self.staticText = wx.StaticText(parent=panel,label="请单击ok按钮")
        b = wx.Button(parent=panel, label='ok')
        self.Bind(wx.EVT_BUTTON,self.on_click,b)

        #创建垂直方向的盒子布局管理对象vbox
        vbox=wx.BoxSizer(wx.VERTICAL)
        #添加静态文本到vbox的布局管理器
        vbox.Add(self.staticText,proportion=1,flag=wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE|wx.Top,border=30) #wx.FIXED_MINSIZE  刚好包裹控件   wx.ALIGN_CENTER_HORIZONTAL 控制水平居中
        #添加按钮b到vbox布局管理器
        vbox.Add(b,proportion=1,flag=wx.EXPAND|wx.BOTTOM,border=10)  #wx.EXPAND  完全填满有效空间   propertion 都为1  所以两个控件各占1/2
        #设置面板panel 采用vbox布局管理器
        panel.SetSizer(vbox)  #两个控件都被放到面板中 所以需要设置面板布局为盒子布局
    def on_click(self,event): #事件处理程序
        self.staticText.SetLabelText("JJJJlk")
#创建窗口对象
frm=MyFrame()
#显示窗口
frm.Show()    #窗口 默认是隐藏 需要调用show方法才能显示
#进入主事件循环   事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示和响应用户事件的处理都是通过主事件循环实现的
app.MainLoop()
```

### 布局管理

​	wxPython提供了布局管理器类帮助实现界面布局，主要分为两大类：盒子布局管理器和网格布局管理器

#### 	盒子布局管理器

​		盒子布局管理器类是wx.BoxSizer，Box布局管理器是最常用的布局管理器，它可以让其中的子窗口（或控件）沿垂直或水平方向布局。

##### 		创建盒子布局管理器对象

​			wx.BoxSizer(wx.HORIZONTAL)   --》 水平方向布局  默认值
			wx.BoxSizer(wx.VERTICAL)     --》 垂直方向布局

##### 		添加子窗口（或控件）到父窗口

​			wx.BoxSizer对象的Add（）方法添加子窗口（或控件）到父窗口
			Add(window,proportion=0,flag=0,border=0)
				proportion参数用于设置当前子窗口（或控件）在父窗口中所占的空间比例
				flag参数是布局标志，用来控制对齐方式、边框和调整尺寸
				border参数用于设置边框的宽度。

flag参数对齐方式：

![](D:\work\个人包\Python\图片\flag对齐标志.png)

flag参数边框标志：

![](D:\work\个人包\Python\图片\flag边框标志.png)

flag参数调整尺寸：

![](D:\work\个人包\Python\图片\flag调整尺寸.png)

##### 		盒子布局管理器嵌套示例

​			布局管理器还可以进行嵌套

```python
#coding=utf-8
import wx
#创建应用程序对象
app=wx.App()
#自定义窗口类 MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='布局管理器嵌套',size=(300,180),pos=(100,100))
        panel=wx.Panel(parent=self)
        self.staticText = wx.StaticText(parent=panel,label="请单击按钮")
        b1=wx.Button(parent=panel,label='Button1',id=10)
        b2 = wx.Button(parent=panel, label='Button2', id=20)

        hbox=wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(b1,proportion=1,flag=wx.EXPAND|wx.ALL,border=10)
        hbox.Add(b2,proportion=1,flag=wx.EXPAND|wx.ALL,border=10)

        vbox=wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.staticText,proportion=1,flag=wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE|wx.Top,border=10)
        vbox.Add(hbox,proportion=1,flag=wx.CENTER)

        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON,self.on_click,id=10,id2=20)

    def on_click(self,event): #事件处理程序
        event_id=event.GetId()
        print(event_id)
        if event_id==10:
            self.staticText.SetLabelText("BUTTON1")
        else:
            self.staticText.SetLabelText("BUTTON2")
#创建窗口对象
frm=MyFrame()
#显示窗口
frm.Show()    #窗口 默认是隐藏 需要调用show方法才能显示
#进入主事件循环   事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示和响应用户事件的处理都是通过主事件循环实现的
app.MainLoop()
```

### 控件

​	wxPython的所有控件都继承自wx.Control类

#### 	文本输入控件

​		文本输入控件（wx.TextCtrl）是可以输入文本的控件

```python
#coding=utf-8
import wx
#创建应用程序对象
app=wx.App()

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='文本输入控件',size=(300,260))
        panel=wx.Panel(parent=self)
        tc1=wx.TextCtrl(panel)   #创建普通文本输入控件
        tc2=wx.TextCtrl(panel,style=wx.TE_PASSWORD)  #创建密码输入控件
        tc3=wx.TextCtrl(panel,style=wx.TE_MULTILINE) #创建多行文本输入控件

        userid=wx.StaticText(panel,label='用户ID')
        pwd=wx.StaticText(panel,label='密码')
        content=wx.StaticText(panel,label='多行文本')

        #创建垂直方向的盒子管理器对象
        vbox=wx.BoxSizer(wx.VERTICAL)

        #添加控件到盒子管理器对象中去
        vbox.Add(userid,flag=wx.EXPAND|wx.LEFT,border=10)
        vbox.Add(tc1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(pwd, flag=wx.EXPAND | wx.LEFT, border=10)
        vbox.Add(tc2, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(content, flag=wx.EXPAND | wx.LEFT, border=10)
        vbox.Add(tc3, flag=wx.EXPAND | wx.ALL, border=10)

        #设置面板panel采用vbox布局
        panel.SetSizer(vbox)

        #设置tc1初始值
        tc1.SetValue('Tom')
        #获取tc1的值
        print('读取用户ID,{0}'.format(tc1.GetValue()))

#创建窗口对象
frm=MyFrame()

#显示窗口
frm.Show()    #窗口 默认是隐藏 需要调用show方法才能显示

#进入主事件循环   事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示和响应用户事件的处理都是通过主事件循环实现的
app.MainLoop()

app=wx.App()
```

#### 	复选框和单选按钮

​		多选控件是复选框（wx.CheckBox），复选框（wx.CheckBox）有时也能单独使用，能提供两种状态的开和关。
		单选控件是单选按钮（wx.RadioButton），同一组的多个单选按钮应该具有互斥性，就是当一个按钮按下时，其他按钮一定释放

```python

#coding=utf-8
import wx
#创建应用程序对象
app=wx.App()

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='复选框和单选按钮，',size=(500,260))
        panel=wx.Panel(parent=self)

        st1=wx.StaticText(panel,label='选择你喜欢的编程语言：')
        cb1=wx.CheckBox(panel,id=1,label='Python')
        cb2 = wx.CheckBox(panel, id=2, label='java')
        cb2.SetValue(True)  #设置cb2的初始状态为选中
        cb3 = wx.CheckBox(panel, id=3, label='C++')

        self.Bind(wx.EVT_CHECKBOX,self.on_check_box,id=1,id2=3)  #绑定id为1~3的所有控件的事件处理到on_check_box方法

        st2=wx.StaticText(panel,label='选择性别')
        radio1=wx.RadioButton(panel,id=4,label='男',style=wx.RB_GROUP)  #设置style=wx.RB_GROUP是一个组的开始，直到遇到另外设置style=wx.RB_GROUP为止都是同一个组  所以radio1  radio2是同一组，且互斥
        radio2 = wx.RadioButton(panel, id=5, label='女')

        self.Bind(wx.EVT_RADIOBUTTON,self.on_radio_box,id=4,id2=5)  #定id为4~5的所有控件的事件处理到on_radio_box方法

        hbox1=wx.BoxSizer()
        hbox1.Add(st1,flag=wx.LEFT|wx.RIGHT,border=5)
        hbox1.Add(cb1)
        hbox1.Add(cb2)
        hbox1.Add(cb3)

        hbox2=wx.BoxSizer()
        hbox2.Add(st2,flag=wx.LEFT|wx.RIGHT,border=5)
        hbox2.Add(radio1)
        hbox2.Add(radio2)

        vbox=wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox1,flag=wx.ALL,border=10)
        vbox.Add(hbox2,flag=wx.ALL,border=10)

        #设置面板采用vbox布局管理器
        panel.SetSizer(vbox)

    def on_check_box(self,event):
        cb=event.GetEventObject()
        print("选择{0}，状态{1}".format(cb.GetLabel,event.IsChecked()))
    def on_radio_box(self,event):
        rb=event.GetEventObject()
        print("第一组，{1}被选中".format(rb.GetLabel))
#创建窗口对象
frm=MyFrame()

#显示窗口
frm.Show()    #窗口 默认是隐藏 需要调用show方法才能显示

#进入主事件循环   事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示和响应用户事件的处理都是通过主事件循环实现的
app.MainLoop()

app=wx.App()


```



#### 	列表

​		对列表控件可以进行单选或多选,列表控件类是wx.ListBox。
		创建列表控件时参数style取值：
			wx.LB_SINGLE  单选
			wx.LB_EXTENDED 多选
			wx.LB_EXTENDED  多选，但是需要在按住Ctrl或Shift键时选择项目。
			wx.LB_SORT 对列表选择项进行排序

```python

#coding=utf-8
import wx
#创建应用程序对象
app=wx.App()

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='文本输入控件',size=(300,260))
        panel=wx.Panel(parent=self)

        st1=wx.StaticText(panel,label='选择你喜欢的编程语言：')
        list1=['Python','Java','C++']
        lb1=wx.ListBox(panel,choices=list1,style=wx.LB_SINGLE)  #wx.LB_SINGLE  表示创建单选列表控件   参数choices用于设置选项
        self.Bind(wx.EVT_LISTBOX,self.on_list1,lb1)    #绑定列表选择事件

        st2 = wx.StaticText(panel, label='选择你喜欢吃的水果：')
        list2 = ['苹果', '橘子', '香蕉']
        lb2 = wx.ListBox(panel, choices=list2, style=wx.LB_EXTENDED)    #wx.LB_EXTENDED 表示创建多选列表控件
        self.Bind(wx.EVT_LISTBOX, self.on_list2, lb2)

        hbox1=wx.BoxSizer()
        hbox1.Add(st1,proportion=1,flag=wx.LEFT|wx.RIGHT,border=5)
        hbox1.Add(lb1,proportion=1)

        hbox2 = wx.BoxSizer()
        hbox2.Add(st2, proportion=1, flag=wx.LEFT | wx.RIGHT, border=5)
        hbox2.Add(lb2, proportion=1)

        vbox=wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox1,flag=wx.ALL|wx.EXPAND,border=5)
        vbox.Add(hbox2,flag=wx.ALL|wx.EXPAND,border=5)

        panel.SetSizer(vbox)

    def on_list1(self,event):
        listbox=event.GetEventObject()
        print('选择{}'.format(listbox.GetSelection()))  # GetSelection    返回单个选中项目的索引序号
    def on_list2(self,event):
        listbox=event.GetEventObject()
        print('选择{}'.format(listbox.GetSelections()))   # GetSelections  返回多个 选中项目索引列表
#创建窗口对象
frm=MyFrame()

#显示窗口
frm.Show()    #窗口 默认是隐藏 需要调用show方法才能显示

#进入主事件循环   事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示和响应用户事件的处理都是通过主事件循环实现的
app.MainLoop()

app=wx.App()


```



#### 	静态图片控件

​		静态图片控件用于显示一张图片，图片可以是wx.Python所支持的任意图片格式，静态图片控件类是wx.StaticBitmap。  在图片替换后 需要重新绘制窗口，否则布局会发生混乱

```python

#coding=utf-8
import wx
#创建应用程序对象
app=wx.App()

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='文本输入控件',size=(300,260))
        self.panel=wx.Panel(parent=self)   #创建一个面板 他是该类的实例变量

        self.bmps=[wx.Bitmap('logo.png',wx.BITMAP_TYPE_PNG),wx.Bitmap('logo2.png',wx.BITMAP_TYPE_PNG),wx.Bitmap('logo1.png',wx.BITMAP_TYPE_PNG)]  #创建wx.Bitmap的列表对象

        b1=wx.Button(self.panel,id=1,label="Button1")
        b2= wx.Button(self.panel, id=2, label="Button2")
        self.Bind(wx.EVT_BUTTON,self.on_click,id=1,id2=2)

        self.image=wx.StaticBitmap(self.panel,bitmap=self.bmps[0])  #静态图片控件对象  self.bmps[0]是静态图片控件要显示的图片对象

        vbox=wx.BoxSizer(wx.VERTICAL)
        vbox.Add(b1,proportion=1,flag=wx.EXPAND)
        vbox.Add(b2, proportion=1, flag=wx.EXPAND)
        vbox.Add(self.image, proportion=3, flag=wx.EXPAND)

        self.panel.SetSizer(vbox)

    def on_click(self,event):
        event_id=event.GetId()
        if event_id==1:
            self.image.SetBitmap(self.bmps[1])   #重新设置图片 实现图片切换
        else:
            self.image.SetBitmap(self.bmps[2])

        self.panel.Layout()   #重新设置面板布局  在图片替换后 需要重新绘制窗口，否则布局会发生混乱

#创建窗口对象
frm=MyFrame()

#显示窗口
frm.Show()    #窗口 默认是隐藏 需要调用show方法才能显示

#进入主事件循环   事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示和响应用户事件的处理都是通过主事件循环实现的
app.MainLoop()

app=wx.App()


```





## 网络通信

### 基本的网络知识

#### TCP/IP

​	TCP/IP是非常重要的协议，由IP和TCP两个协议构成   IP（Internet Protocol）是一种低级的路由协议，
它将数据拆分在许多小的数据包中，并通过网络将它们发送到某一特定地址，但无法保证所有包都抵达目的地，
也不能保证包按顺序抵达   ---》传输数据存在不安全性--》。TCP是一种高层次的协议，是面向连接的可靠数据传输协议，如果有些数据包没被收到，则会重发，对数据包的内容准确性进行检查并保证数据包按顺序抵达。

#### IP地址

​	为了实现网络中不同计算机之间的通信，每台计算机都必须有一个与众不同的标识，这就是IP地址，TCP/IP使用IP地址来标识源地址和目的地址
	IPv4 ： 所有的IP地址都是由32位数字构成的，由4个8位的二进制数组成，每8位之间用圆点隔开，例如192.168.1.1
	IPv6 :  IPv6使用128位数字表示一个地址,例如127.0.0.0 (本机：只发送数据，只进行本机进程间通信，不进行任何网络传输)

#### 端口

​	一个IP地址标识一台计算机，每一台计算机又有很多网络通信程序在运行，提供网络服务或进行通信，这就需要不同的端口进行通信
	TCP/IP系统中的端口号是一个16位的数字，它的范围是 0～65535
将小于1024的端口号保留给预定义的服务，例如HTTP是80，FTP是21，Telnet是23，Email是25，等等。除非要和那些服务进行通信，否则不应该使用小于1024的端口

#### HTTP/HTTPS

​	对互联网的访问大多基于HTTP/HTTPS，HTTP/HTTPS是TCP/IP的一种协议

##### 	HTTP

​		HTTP（Hypertext Transfer Protocol，超文本传输协议）属于应用层协议，其简捷、快速的方式适用于分布式超文本信息传输HTTP是无连接协议，即在每一次请求时都建立连接，服务器在处理完客户端的请求后，会先应答客户端，然后断开连接，不会一直占用网络资源
		HTTP/1.1共定义了8种请求方法：OPTIONS、HEAD、GET、POST、PUT、DELETE、TRACE和CONNECT。GET和POST方法最常用。
		GET方法   --》 "明信片"
		用于向指定的资源发出请求，被发送的信息“显式”地跟在URL后面。它一般只用于读取数据，例如静态图片等
		POST方法  --》 "信"
		用于向指定的资源提交数据，请求服务器进行处理，例如提交表单或者上传文件等,数据被包含在请求体中

##### 	HTTPS

​		HTTPS（Hypertext Transfer Protocol Secure，超文本传输安全协议）是超文本传输协议和SSL的组合，用于提供加密通信及对网络服务器身份的鉴定。简单地说，HTTPS是加密的HTTP

##### 	HTTPS与HTTP的区别		

​		HTTPS使用https：//代替http：//，HTTPS使用端口443，而HTTP使用端口80与TCP/IP通信

### 搭建自己的Web服务器

#### 	1 安装JDK（Java开发工具包）

#### 	2 配置Java运行环境

#### 	3 安装Apache Tomcat服务器

#### 	4 启动Apache Tomcat服务器

#### 	5 测试Apache Tomcat服务器

​		

### urllib.request模块

​	发送GET请求  如果要发送HTTP/HTTPS的GET请求，则可以使用urllib.request模块的Request对象

```python
# urllib.request模块  get请求
import urllib.request

url='http://localhost:8080/NoteWebService/note.do?action=query&ID=10'

req=urllib.request.Request(url)   #创建Request请求  默认是get请求
with urllib.request.urlopen(req) as response:  #发送网咯请求 response是需要释放的对象
    data=response.read() #读取数据 为字节序列数据
    json_data=data.decode() #将字节序列数据 转换为字符串
    print(json_data)

```

​	发送POST请求  如果要发送HTTP/HTTPS的POST请求，则其发送流程与发送GET请求非常类似

```python
# urllib.request模块  post请求
import urllib.request

url='http://localhost:8080/NoteWebService/note.do'

#准备http参数
params_dict={"action":"query","ID":'10'}
params_str=urllib.parse.urlencode(params_dict)  #将字典参数转化为字符串
print(params_str)

#字符串转化为字节序列对象
params_bytes=params_str.encode()  #发送post请求时 参数以字节序列形式发送

req=urllib.request.Request(url,data=params_bytes)  #发送post请求 创建了Request请求

with urllib.request.urlopen(req) as response:  #发送网咯请求 response是需要释放的对象
    data=response.read() #读取数据 为字节序列数据
    json_data=data.decode() #将字节序列数据 转换为字符串
    print(json_data)
```



### JSON数据

#### 	JSON文档的结构

​		构成JSON文档的两种结构为：JSON对象和JSON数组
		1 JSON对象

![](D:\work\个人包\Python\图片\JSON对象.png)

​		2 JSON数组	

![](D:\work\个人包\Python\图片\JSON数组.png)

#### 	JSON数据的解码 --》  JSON数据被转换为Python数据

​		JSON数据的解码（decode）指将JSON数据转换为Python数据，当从网络中接收或从磁盘中读取JSON数据时，需要将其解码为Python数据  

![](D:\work\个人包\Python\图片\JSON数据和Python数据对比.png)

​		使用json模块提供的loads（str）函数进行JSON数据的解码参数str是JSON字符串，返回Python数据

```python

import urllib.request
import json

url='http://localhost:8080/NoteWebService/note.do?action=query&ID=10'

req=urllib.request.Request(url)   #创建Request请求  默认是get请求
with urllib.request.urlopen(req) as response:  #发送网咯请求 response是需要释放的对象
    data=response.read() #读取数据 为字节序列数据
    json_data=data.decode() #将字节序列数据 转换为字符串
    print(json_data)

    py_dict=json.loads(json_data)  #解码JSON字符串 返回字典
    print("备忘录ID",py_dict["ID"])
    print("备忘录日期", py_dict["cDate"])
    print("备忘录内容", py_dict["Content"])
    print("用户ID", py_dict["UserID"])
```



### 下载图片示例

```python
import urllib.request

url='http://localhost:8080/NoteWebService/logo.png'

req=urllib.request.Request(url)
with urllib.request.urlopen(url) as response:
    data=response.read()
    f_name='download.png'
    with open(f_name,'wb') as f:
        f.write(data)
        print('文件下载成功')
```



### 返回所有备忘录信息	

```python
import urllib.request
import json

url='http://localhost:8080/NoteWebService/note.do?action=query&ID=10'

req=urllib.request.Request(url)   #创建Request请求  默认是get请求
with urllib.request.urlopen(req) as response:  #发送网咯请求 response是需要释放的对象
    data=response.read() #读取数据 为字节序列数据
    json_data=data.decode() #将字节序列数据 转换为字符串
    print(json_data)

    py_dict=json.loads(json_data)  #解码JSON字符串 返回字典
    record_array=py_dict["Record"]

    for record_obj in record_array:
        print('备忘录记录---------------')
        print("备忘录ID",py_dict["ID"])
        print("备忘录日期", py_dict["cDate"])
        print("备忘录内容", py_dict["Content"])
        print("用户ID", py_dict["UserID"])
```

### 	





## 访问数据库

数据量较少，则我们可以将数据保存到文件中；数据量较大，则我们可以将数据保存到数据库中

### SQLite数据库

​	SQLite是嵌入式系统使用的关系数据库，目前的主流版本是SQLite3。SQLite是开源的，采用C语言编写而成，具有可移植性强、可靠性高、小而易用等特点

#### 	SQLite数据类型

​		SQLite是无数据类型的数据库，在创建表时不需要为字段指定数据类型
		SQLite支持的常见数据类型如下
			INTEGER：有符号的整数类型
			REAL：浮点类型
			TEXT：字符串类型，采用UTF-8和UTF-16字符编码
			BLOB：二进制大对象类型，能够存放任意二进制数据
	 	Python数据类型与SQLite数据类型的映射

![](D:\work\个人包\Python\图片\Python数据类型与SQLite数据类型的映射.png)

#### 	 SQLite和Oracle/MySql的区别

​		SQLite是为嵌入式设备（如智能手机）设计的数据库 SQLite在运行时与使用它的应用程序之间公用相同的进程空间，
		而在运行时，Oracle/MySql程序与使用它的应用程序在两个不同进程中

### 使用GUI管理工具管理SQLite数据库

#### 	1 安装和启动DB Browser for SQLite

​		DB.Browser.for.SQLite-3.11.2-win32.zip  -》将该文件解压到一个目录中，在解压目录下找到DB Browser for SQLite.exe文件，双击该文件即可启动DB Browser for SQLite工具

#### 	2 创建数据库

​		一个SQLite数据库对应一个SQLite数据文件，为了测试DB Browserfor SQLite工具，我们要先创建SQLite数据库

#### 	3 创建数据表

​		在一个SQLite数据库中可以包含多个数据表。在上图所示的界面单击“保存”按钮，弹出建表对话框。

#### 	4 执行SQL语句

​		使用DB Browser for SQLite工具，可以执行任意合法的SQL语句

#### 	5 浏览数据

​		DB Browser for SQLite常用于浏览数据

###  数据库编程的基本操作过程

​	数据库编程主要分为两类：查询（Read）和修改（C插入、U更新、D删除）。

#### 	1 查询数据

​		查询数据时需要6步，在查询过程中需要提取数据结果集，最后释放资源，即关闭游标和数据库

![](D:\work\个人包\Python\图片\SQLite数据库操作.png)

#### 	2 修改数据

​		修改数据时如上图所示，最多需要6步，在修改过程中如果执行SQL操作成功，则提交数据库事务；如果失败，则回滚事务。最后释放资源，关闭游标和数据库

### sqlite3模块API

#### 	数据库连接对象Connection

​		数据库访问的第一步是进行数据库连接。
		通过connect（database）函数参数database是SQLite数据库的文件路径，如果连接成功，则返回数据库连接对象Connection
		Connection对象有如下重要的方法
			close（）：关闭数据库连接，在关闭之后再使用数据库连接将引发异常。
			commit（）：提交数据库事务。
			rollback（）：回滚数据库事务。
			cursor（）：获得Cursor游标对象

#### 	游标对象Cursor

​		一个Cursor游标对象表示一个数据库游标，游标暂时保存了SQL操作所影响到的数据。游标是通过数据库连接创建的。
		游标Cursor对象有很多方法和属性，其中的基本SQL操作方法如下
			execute（sql[，parameters]）：执行一条SQL语句，sql是SQL语句，parameters是为SQL提供的参数，可以是序列或字典类型。返回值是整数，表示执行SQL语句影响的行数。
			executemany（sql[，seq_of_params]）：执行批量SQL语句，sql是SQL语句，seq_of_params是为SQL提供的参数，seq_of_params是序列。返回值是整数，表示执行SQL语句影响的行数。在通过execute（）和executemany（）方法执行SQL查询语句后，还要通过提取方法从查询结果集中返回数据，相关提取方法如下。
			fetchone（）：从结果集中返回只有一条记录的序列，如果没有数据，则返回None。
			fetchmany（size=cursor.arraysize）：从结果集中返回小于等于size记录数的序列，如果没有数据，则返回空序列，size在默认情况下是整个游标的行数。
			fetchall（）：从结果集中返回所有数据。

### 数据库的CRUD操作示例

​		对数据库表中的数据可以进行4类操作：数据插入（Create）、数据查询（Read）、数据更新（Update）和数据删除（Delete），即增、删、改、查

#### 	无条件查询

```python
#coding=utf-8
#无条件查询
import sqlite3

try:
    #建立数据连接
    con=sqlite3.connect('../SQLite/my_db.db')
    #创建游标对象
    cursor=con.cursor()
    #执行sql查询操作
    sql='SELECT s_id,s_name,s_sex,s_birthday FROM student'
    cursor.execute(sql)
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

```



#### 	有条件查询

```python
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

```



#### 	插入数据

```python
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

```



#### 	更新数据

```python
#coding=utf-8
#有条件查询
import sqlite3
i_id=input("请输入学号：")
i_name=input('请输入姓名：')
i_sex=input("请输入性别（1表示男 0表示女）：")
i_birthday=input('请输入生日（yyyyMMdd）：')
try:
    #建立数据连接
    con=sqlite3.connect('../SQLite/my_db.db')
    #创建游标对象
    cursor=con.cursor()
    #执行sql查询操作
    sql='UPDATE student SET s_name=?,s_sex=?,s_birthday=? WHERE s_id=?'
    cursor.execute(sql,[i_name,i_sex,i_birthday,i_id])
    #提交数据库事务
    con.commit()
    print("更新数据成功")
except sqlite3.Error as e:
    print('更新数据失败{}'.format(e))
    #回滚事务
    con.rollback()
finally:
    #关闭游标
    if cursor:
        cursor.close()
    #关闭数据连接
    if con:
        con.close()

```



#### 	删除数据

```python
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

```



### 防止SQL注入攻击

​	在构建SQL时 不采用占位符占位 直接将实参 拼接起来

如：sql='SELECT s_id,s_name,s_sex,s_birthday FROM student WHERE s_birthday<'+istr

 可以实现数据库的操作 但会有潜在风险 ‘SQL注入攻击’

​	SQL注入攻击：是指在传递实参时，使用特殊字符或sql关键字 在拼接成SQL后 这条SQL语句有一定的攻击性 



## 多线程

### 线程相关的知识

#### 	进程

​		一个进程就是一个正在执行的程序，每一个进程都有自己独立的一块内存空间、一组系统资源。在进程的概念中，每一个进程的内部数据和状态都是完全独立的
		在Windows操作系统中，一个进程就是一个exe或者dll程序，它们相互独立，相互也可以通信

#### 	线程

​		在一个进程中可以包含多个线程，多个线程共享一块内存空间和一组系统资源。所以，系统在各个线程之间切换时，开销要比进程小得多，正因如此，线程被称为轻量级进程。

#### 	主线程

​		Python程序至少有一个线程，这就是主线程，程序在启动后由Python解释器负责创建主线程，在程序结束后由Python解释器负责停止主线程。
		在多线程中，主线程负责其他线程的启动、挂起、停止等操作。其他线程被称为子线程。

### 线程模块——threading

​	Python官方提供的threading模块可以进行多线程编程。
	threading模块中提供了线程类Thread，还提供了很多线程相关的函数，如下
		active_count（）：返回当前处于活动状态的线程个数。
		current_thread（）：返回当前的Thread对象。
		main_thread（）：返回主线程对象。

```python
#coding=utf-8
#线程模块
import threading
#当前线程对象
t=threading.current_thread()
#当前线程名
print(t.name)
#返回当前处于活动状态的线程个数
print(threading.active_count())

#当前主线程对象
t=threading.main_thread()
#主线程名
print(t.name)

```



### 创建子线程

​	创建可执行的子线程，需要如下两个要素。
		1 线程对象：线程对象是threading模块的线程类Thread或Thread子类所创建的对象。
		2 线程体：线程体是子线程要执行的代码，代码会被封装到一个函数中。子线程在启动后会执行线程体。
			实现线程体主要有以下两种方式：
				1）自定义函数实现线程体。
				2）自定义线程类实现线程体。

#### 	自定义函数实现线程体

​	创建线程Thread对象的构造方法：Thread(target=None,name=None,args=[])
		target参数指向线程体函数，我们可以自定义该线程体函数
		通过name参数可以设置线程名，如果省略这个参数，则系统会为其分配一个名称
		args是为线程体函数提供的参数，是一个元组类型

```python
#coding=utf-8
#创建子线程  自定义函数实现线程体
import threading
import time

#线程体函数
def thread_body():
    #当前线程对象
    t=threading.current_thread()
    for n in range(5):
        #当前线程名
        print("第{0}次执行线程{1}".format(n,t.name))
        #线程休眠
        time.sleep(2)
    print('线程{0}执行结束'.format(t.name))

#主线程
#创建子线程t1
t1=threading.Thread(target=thread_body)
#创建子线程t2
t2=threading.Thread(target=thread_body,name='MYT')   #name=''   设置线程名
#启动线程
t1.start()
t2.start()
```



#### 	自定义线程类实现线程体

​		另外一种实现线程体的方式是，创建一个Thread子类并重写run（）方法，run（）方法就是线程体函数。

```python
#coding=utf-8
#创建子线程  自定义线程类实现线程体
import threading
import time

class SmallThread(threading.Thread):
    def __init__(self,name=None):
        super().__init__(name=name)
    #线程体函数
    def run(self):
        #当前线程对象
        t=threading.current_thread()
        for n in range(5):
            # 当前线程名
            print("第{0}次执行线程{1}".format(n, t.name))
            # 线程休眠
            time.sleep(2)
        print('线程{0}执行结束'.format(t.name))

#主线程
#创建子线程t1
t1=SmallThread() #通过自定义线程类，创建线程对象
#创建子线程t2
t2=SmallThread(name='MYT') #name=''   设置线程名
#启动线程
t1.start()
t2.start()
```



### 线程管理

​	线程管理包括线程创建、线程启动、线程休眠、等待线程结束和线程停止

#### 等待线程结束

​	一个线程（假设是主线程）需要等待另外一个线程（假设是t1子线程）执行结束才能继续执行。 --> join（）方法
	语法：join(timeout=None)
	参数timeout用于设置超时时间，单位是秒.如果没有设置timeout则可以一直等待，直到结束。

```python
#coding=utf-8
#线程管理  等待线程结束
import threading
import time
#共享变量
value=[]

#线程体函数
def thread_body():
    #当前线程对象
   print('t1子线程开始...')
   for n in range(2):
        print('t1子程序执行...')
        value.append(n)
        #线程休眠
        time.sleep(2)
   print('t1子线程结束。')

#主线程
print('主线程开始...')
#创建子线程t1
t1=threading.Thread(target=thread_body) #通过自定义线程类，创建线程对象
#启动线程
t1.start()
#主程序被阻塞，等待t1子线程结束
t1.join()
print('value={0}'.format(value))
print('主线程继续执行...')
```



#### 线程停止

​	在线程体结束时，线程就停止了,但在某些业务比较复杂时，会在线程体中执行一个“死循环”。

```python
#coding=utf-8
#线程管理  线程停止
import threading
import time
#线程停止变量
isrunning=True  #控制流程结束

#工作线程体函数
def workthread_body(): #工作线程体执行一些任务
   while isrunning:   #工作线程 死循环
       #线程开始工作
       print('工作线程执行中....')
       #线程休眠
       time.sleep(2)
   print('工作线程结束')
#控制线程体函数
def controlthread_body():   #控制线程体 从控制台读取指令 根据指令修改线程停止变量
    global isrunning        #要修改isrunning 故声明变量为global
    while isrunning:        #控制线程体  死循环
        #从键盘输入停止指令
        command=input('请输入停止指令：')
        if command=='exit':
            isrunning =False
            print('控制线程结束')

#主线程
#创建工作线程对象workthead
workthead=threading.Thread(target=workthread_body)
#启动工作线程
workthead.start()
#创建控制线程对象controlthead
controlthead=threading.Thread(target=controlthread_body)
#启动控制线程
controlthead.start()
```



### 下载图片示例

```python
#coding=utf-8
#下载图片示例
import threading
import time
import urllib.request
#线程停止变量
isrunning=True  #控制流程结束

#工作线程体函数
def workthread_body(): #工作线程体执行一些任务
   while isrunning:   #工作线程 死循环
       #线程开始工作
       print('工作线程执行中....')
       download()    #执行下载任务  每5秒调用一次
       #线程休眠
       time.sleep(5)
   print('工作线程结束')
#控制线程体函数
def controlthread_body():   #控制线程体 从控制台读取指令 根据指令修改线程停止变量
    global isrunning        #要修改isrunning 故声明变量为global
    while isrunning:        #控制线程体  死循环
        #从键盘输入停止指令
        command=input('请输入停止指令：')
        if command=='exit':
            isrunning =False
            print('控制线程结束')

def download():   #下载函数  右工作线程调用
    url='http://localhost:8080/NoteWebService/logo.png'
    req=urllib.request.Request(url)
    with urllib.request.urlopen(url) as respose:
        data=respose.read()
        f_name='dowbload.png'
        with open(f_name,'wb') as f:
            f.write(data)
            print("下载文件成功")
#主线程
#创建工作线程对象workthead
workthead=threading.Thread(target=workthread_body)
#启动工作线程
workthead.start()
#创建控制线程对象controlthead
controlthead=threading.Thread(target=controlthread_body)
#启动控制线程
controlthead.start()
```

​				
​					
​		
​		
​		
		
​		
​		
​		
​		
​		
​		
​		
​		