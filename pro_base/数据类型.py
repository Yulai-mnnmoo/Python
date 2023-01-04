#整数类型
x=28   #十进制
y=0b11100 #二进制  0b...  0B...
z=0o34 #八进制  0o...  0O...
w=0x1c #十六进制  0x... 0X...

print("xyz值",x,y,z,w,type(x),type(y),type(z),type(w)) #type() 函数返回数据类型

#浮点类型
xx=1.0
yy=3.34e2  #科学计数法表示 e(E)表示10的指数  e2 -->10的平方

print("xxyy",xx,yy,type(xx),type(yy))

#复数类型
xxx=1+2j
yyy=2+4j

print("xxxyyy",xxx,yyy,(xxx+yyy),type(xxx),type(yyy))#复数类型为complex  复数相加实部相加 复部相加

#布尔类型  bool() 函数转化为bool类型数据
a=bool(0)  #False
b=bool(1)  #True
c=bool('')  #False
d=bool(' ') #True
e=bool([])  #False
f=bool({})  #False

print("...",a,b,c,d,e,f)

#数据类型转化  隐式
aa=1+True
bb=1.0+1
cc=1.0+True
dd=1.0+1+True
rr=1.0+1+False

print("==",aa,bb,cc,dd,rr)#往‘高’级转化

#数据类型转化  显式
aaa=int(False)
bbb=int(1.0)
ccc=bool(1.0)
ddd=bool(1)
eee=float(False)
fff=float(1)

print("..",aaa,bbb,ccc,ddd,eee,fff)#int()  bool() float()强制数据类型转化