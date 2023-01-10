#ecoding = utf-8
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


#关闭文件  使用with as 关闭
f_name='test.txt'
with open(f_name) as f:   #代码结束后自动关闭释放资源  优化代码结构 更简洁
    content = f.read()
    print(content)


#复制文本文件
f_name1='test.txt'

with open(f_name1,'r',encoding='gbk') as f:  #以只读模式 打开文件 注意文件编码是gbk 与字符集的大小没有关系
    lines=f.readlines()   #读取所有数据到一个列表中
    copy_f_name='src_test.txt'
    with open(copy_f_name,'w',encoding='utf-8') as copy_f: #以只写模式 打开文本文件 注意文件编码格式为utf-8
        copy_f.writelines(lines)  #把列表数据lines写到文件中
        print('文件复制成功')


#复制二进制文件
f_name ='logo.png'
with open(f_name,'rb') as f:
    b=f.read()
    copy_f_name='logo2.png'
    with open(copy_f_name,'wb') as copy_f:
        copy_f.write(b)
        print("文件复制成功")




