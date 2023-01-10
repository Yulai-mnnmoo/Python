#数学计算模块  math
import math

print(math.ceil(2.4),math.floor(2.4),math.ceil(-2.4),
      math.floor(-2.4),math.pow(5,3),math.sqrt(3.6),math.log(125,5),
      math.degrees(0.5*math.pi),math.radians(180/math.pi),math.sin(0.3))

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

#日期时间模块 date类
import datetime

print(datetime.date(2022,2,28))
print(datetime.date.today())
print(datetime.date.fromtimestamp(9999999999.999))


#日期时间模块 time类
import datetime

print(datetime.time(23,59,59,10000))
#print(datetime.time(23,60,59,10000))  #分 60 超出范围

#日期时间模块 timedelta类
import datetime
d=datetime.datetime.today()
delta=datetime.timedelta(10)   #创建10天后的对象
d+=delta
d1=datetime.date(2020,1,1)
dalta1=datetime.timedelta(weeks=5)  #创建五周后的对象
d1-=dalta1

print(d,d1)

#字符串时间格式转化
import datetime
d=datetime.datetime.today()
d.strftime('%Y-%m-%d %H:%M:%S') #设置日期时间格式化

print(d)
d.strftime('%Y-%m-%d')

print(d)

str_date='2020-02-29 10:40:26'
date=datetime.datetime.strptime(str_date,'%Y-%m-%d %H:%M:%S')  #将一个字符串按照指定格式破解为日期时间对象


#正则 字符串匹配
import re
p=r'\w+@zhijieketang\.com'
email1='tang@zhijieketang.com'

m=re.match(p,email1)   #返回非空的match对象 说明匹配成功
email2='abc@163.com'
m1=re.match(p,email2)   #m1为None 表示匹配失败

print(m,type(m),m1)


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

#正则 字符串查找
import re
p=r'\d+' #匹配数字出现一次或多次的正则表达式
text='AB12cd34Ef'
replace=re.sub(p," ",text)

print(replace) #返回值是替换过后的字符串
replace=re.sub(p," ",text,count=1)

print(replace) #count=1 表示要替换的最大数量


#正则 字符串分割
import re
p=r'\d+' #匹配数字出现一次或多次的正则表达式
text='AB12cd34Ef'
clist=re.split(p,text,maxsplit=0)

print(clist)
clist=re.split(p,text,maxsplit=1)

print(clist)








