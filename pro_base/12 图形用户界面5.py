
#coding=utf-8
import wx
#创建应用程序对象
app=wx.App()

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='文本输入控件',size=(300,260))
        panel=wx.Panel(parent=self)
        tc1=wx.TextCtrl(panel)   #创建普通文本输入控件
        tc2=wx.TextCtrl(panel,style=wx.TE_PASSWORD)  #创建密码输入控件
        tc3=wx.TextCtrl(panel,style=wx.TE_MULTILINE) #创建多行文本输入控件

        userid=wx.StaticText(panel,label='用户ID')
        pwd=wx.StaticText(panel,label='密码')
        content=wx.StaticText(panel,label='多行文本')

        #创建垂直方向的盒子管理器对象
        vbox=wx.BoxSizer(wx.VERTICAL)

        #添加控件到盒子管理器对象中去
        vbox.Add(userid,flag=wx.EXPAND|wx.LEFT,border=10)
        vbox.Add(tc1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(pwd, flag=wx.EXPAND | wx.LEFT, border=10)
        vbox.Add(tc2, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(content, flag=wx.EXPAND | wx.LEFT, border=10)
        vbox.Add(tc3, flag=wx.EXPAND | wx.ALL, border=10)

        #设置面板panel采用vbox布局
        panel.SetSizer(vbox)

        #设置tc1初始值
        tc1.SetValue('Tom')
        #获取tc1的值
        print('读取用户ID,{0}'.format(tc1.GetValue()))

#创建窗口对象
frm=MyFrame()

#显示窗口
frm.Show()    #窗口 默认是隐藏 需要调用show方法才能显示

#进入主事件循环   事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示和响应用户事件的处理都是通过主事件循环实现的
app.MainLoop()

app=wx.App()

