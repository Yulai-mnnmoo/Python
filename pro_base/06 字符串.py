#普通字符串
a="hrlllo"
s='\u0048\u0065'

print(a,s)

# 转义字符应用
aa='hh\nkk'
b="hh\u000a kk"
print(aa,b,'hh\tkk','hh\"kk','hh\\kk')

# 原始字符串
aaa='hh\nkk'
print(aaa,r'hh\nkk')

# 长字符号
s='''ddsdsfdsfdsf颠三倒四大多
数的SV方式'''

print(s)

# 字符串相互转化
i=int("80")
l=float("80")

print(i,l)
ii=str(80)
ll=str(80.1)
k=str(True)

print(ii,ll,k)

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

# 操作字符串
sr='ddsskkllea'

print(sr.find('e'),sr.find('d',1),sr.find('l',4,8))  #找得到值返回 下标  找不到值 返回-1
print(sr.replace('dd','kk')) #返回值 是改变后的字符串
print(sr.replace('k','|',2)) #返回值 是改变后的字符串
print(sr.split('k'),sr.split('k',1))  #返回值是数组   maxsplit是最大分割次数


s="Hello World"

print(s[-5:],s[-5:0])  #截取时 start end  要么都为正 要么都为负  否则没有返回值

s="World"

print(s[-1::-1],s[::-1])#倒序