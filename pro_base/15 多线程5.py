#coding=utf-8
#线程管理  线程停止
import threading
import time
#线程停止变量
isrunning=True  #控制流程结束

#工作线程体函数
def workthread_body(): #工作线程体执行一些任务
   while isrunning:   #工作线程 死循环
       #线程开始工作
       print('工作线程执行中....')
       #线程休眠
       time.sleep(2)
   print('工作线程结束')
#控制线程体函数
def controlthread_body():   #控制线程体 从控制台读取指令 根据指令修改线程停止变量
    global isrunning        #要修改isrunning 故声明变量为global
    while isrunning:        #控制线程体  死循环
        #从键盘输入停止指令
        command=input('请输入停止指令：')
        if command=='exit':
            isrunning =False
            print('控制线程结束')

#主线程
#创建工作线程对象workthead
workthead=threading.Thread(target=workthread_body)
#启动工作线程
workthead.start()
#创建控制线程对象controlthead
controlthead=threading.Thread(target=controlthread_body)
#启动控制线程
controlthead.start()


