#序列 索引
a="Hedzx"

print(a[0],a[4],a[-1],a[-5]) #下标 >= 数组长度 会报错   [0,4] [-5,-1]
print(max(a),min(a),len(a))  #max() 函数用于返回最后一个元素 ？？  min()函数用于返回第一个元素 len()函数用于获取序列的长度

#序列 加和乘操作
aa="Hedzx"

print(aa*2)
aa*=2
print(aa,aa+',woll')

#序列 切片操作
aaa="Hedzx"

print(aaa[1:3],aaa[:3],aaa[0:],aaa[:],aaa[0:5],a[1:-1])
print(aaa[1:5:4],aaa[::-1])  #aaa[::-1] 是倒序排列

#序列 成员测试 in   not in
aaaa="Hedzx"

print('e'in aaaa,'E'in aaaa,'E'not in aaaa)

#列表  创建列表
b=[10,20,30,40,50,90]
c=[] #创建空列表
d=["ddd",23,44,'xx'] #创建 字符串和数字的混合列表 列表每个元素后面都有一个逗号 最后一个元素可以省略
e=list("dddkklloecvd")  #list 里面参数是序列对象

print(b,c,d,e)

#列表  追加元素
list =[20,10,60,80,0]
list.append(11)  #在列表后追加一个元素 不能追加多个
t=['ww',22]
l=[33,44]

print(list,list+t,list.extend(l)) #list.extend(l) 方法不能直接放到打印地方 先计算在打印
list.extend(t)
print(list)

#列表  插入元素
list =[20,10,60,80,0]
list.insert(2,80)

print(list,list.insert(1,11))

#列表  替换元素
list =[20,10,60,80,0]
list[0]=100

print(list)

#列表  删除元素
list =[20,10,60,80,0]
list.remove(20)

print(list)


#===================

# 元组  创建元组
li=1,2,3
li1=(1,2,3)
li2=("jj",1,2)
li3=tuple("hhheccl")
li4=1,
li5=(1,)#创建一个元素的元组后面的逗号不能省略

print(li,li1,li2,li3,li4,li5,type(li5))

# 元组  元组拆包
s_id,s_name=(101,'zhangsan')

print(s_id,s_name)

# 集合  创建集合
se=set("hhheddsls")
se1={10,20,55,88}

print(se,se1,type(se))

# 集合  修改集合
se2={'zhangsan','lisi','wangwu'}
se2.add('dongliu')

print(se2)
se2.remove('lisi')  #删除时  如果集合中不存在该元素 则会抛出错误

print(se2,'lisi' in se2)
se2.clear()
print(se2)

# 字典  创建字典
dict0={101:'zhangsan',102:'lisi'}
dict1=dict({101:'zzz',102:'lll'})
dict2=dict(((101,'zs'),(100,'ls')))
dict3=dict(zip([11,12],['xx','yy']))

print(dict0,dict1,dict2,dict3)

# 字典  修改字典
dict0={101:'zhangsan',102:'lisi'}
dict0[103]='wangwu'
dict0[102]='ssss'
di=dict0.pop(102)  #使用字典的pop()方法 删除键值对 返回值是key 对应的value值

print(dict0[101],dict0,di)

# 字典  访问字典视图
dict0={101:'zhangsan',102:'lisi'}
# ll=list(dict0.keys()) #这里会报错？？？

print(dict0.items(),dict0.keys())

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
