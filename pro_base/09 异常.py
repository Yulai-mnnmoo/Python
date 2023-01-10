#除0异常
i=input('请输入数字：')
n=8888
result=n/int(i)

print(result)
print('{0}除以{1}等于{2}'.format(n,i,result))

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

#多重捕获异常
i=input('请输入数字：')
n=8888
try:
    result=n/int(i)

    print(result)
    print('{0}除以{1}等于{2}'.format(n,i,result))
except (ZeroDivisionError,ValueError) as e:  #指定具体的异常类型
    print('不能除以0，异常：{}'.format(e))

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

finally:
    # 释放代码资源
    print("资源释放...")


# 自定义异常
class ZhiException(Exception):
    def __init__(self,message):
        super().__init__(message)

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