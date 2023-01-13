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


