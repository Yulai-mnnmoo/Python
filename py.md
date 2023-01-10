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