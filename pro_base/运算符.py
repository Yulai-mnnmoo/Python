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
# print(mm>nn,vv>nn)#列表比较 当两个列类型不兼容时不可以比较

#逻辑运算符
a=-1
b=0
def f1():
    print("函数f1")
    return  True

print((a>b) or f1()) #a>b结果为False 结果不确定 要调用f1
print((a>b) and f1()) #a>b结果为False 结果确定  不用调用f1
print(not f1)

#位运算符
ss=0b10110010 #178
qq=0b01011110 #94
pp=-0b10110010 #-178

print(~ss)  #10110010  -0b10110011  正数变负数的取反是先取反码 再取补码 再最后位加1   ~a=(a+1)x-1
print(ss|qq) # 10110010  01011110   ===> 11111110
print(ss&qq) # 10110010  01011110   ===> 00010010
print(ss^qq) # 10110010  01011110   ===> 11101100
print(ss>>2) #  10110010 ===> 00101100      右位移实际上是去掉最后两位在最前面补右位移位数个0
print(~ss>>2) # -0b10110011 ===> -0b00101101 反码的右位移是 先取反（上面） 再位移  再+1
print(~ss<<2) # -0b10110011 ===> -0b1011001100  同下 左位移
print(ss<<2) # 10110010 ===> 1011001000     左位移实际上是在后面补左位移位数个0
print(pp)  #10110010 01001101 10110001     负数变正数的取反 是先取反码 再取补码 再最后位减1

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

#运算符的优先级
gs=1-2*2
gq=0b10110010
gw=0b01011110
gc=0b00000011

print(gs,gq|gw&gc,0b10110010)


