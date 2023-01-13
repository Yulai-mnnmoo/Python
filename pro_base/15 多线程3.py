#coding=utf-8
#创建子线程  自定义线程类实现线程体
import threading
import time

class SmallThread(threading.Thread):
    def __init__(self,name=None):
        super().__init__(name=name)
    #线程体函数
    def run(self):
        #当前线程对象
        t=threading.current_thread()
        for n in range(5):
            # 当前线程名
            print("第{0}次执行线程{1}".format(n, t.name))
            # 线程休眠
            time.sleep(2)
        print('线程{0}执行结束'.format(t.name))

#主线程
#创建子线程t1
t1=SmallThread() #通过自定义线程类，创建线程对象
#创建子线程t2
t2=SmallThread(name='MYT') #name=''   设置线程名
#启动线程
t1.start()
t2.start()


