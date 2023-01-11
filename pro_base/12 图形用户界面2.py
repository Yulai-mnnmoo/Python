
#coding=utf-8
import wx
#创建应用程序对象
app=wx.App()

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='事件处理',size=(500,300),pos=(100,100))
        panel=wx.Panel(parent=self)
        self.staticText=wx.StaticText( parent=panel,label='请单击ok按钮',pos=(110,20))
        b=wx.Button(parent=panel,label='ok',pos=(100,50))  #创建按钮事件
        self.Bind(wx.EVT_BUTTON,self.on_click,b)   #绑定事件 wx.EVT_BUTTON 是事件类型 self_on_click 是事件处理程序 b 是事件源 即按钮对象
    def on_click(self,event): #事件处理程序
        self.staticText.SetLabelText("JJJJlk")
#创建窗口对象
frm=MyFrame()

#显示窗口
frm.Show()    #窗口 默认是隐藏 需要调用show方法才能显示

#进入主事件循环   事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示和响应用户事件的处理都是通过主事件循环实现的
app.MainLoop()

app=wx.App()

