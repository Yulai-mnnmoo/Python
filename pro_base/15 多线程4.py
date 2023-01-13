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


