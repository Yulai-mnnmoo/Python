#coding=utf-8
import wx
#创建应用程序对象
app=wx.App()
#自定义窗口类 MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='布局管理器嵌套',size=(300,180),pos=(100,100))
        panel=wx.Panel(parent=self)
        self.staticText = wx.StaticText(parent=panel,label="请单击按钮")
        b1=wx.Button(parent=panel,label='Button1',id=10)
        b2 = wx.Button(parent=panel, label='Button2', id=20)

        hbox=wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(b1,proportion=1,flag=wx.EXPAND|wx.ALL,border=10)
        hbox.Add(b2,proportion=1,flag=wx.EXPAND|wx.ALL,border=10)

        vbox=wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.staticText,proportion=1,flag=wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE|wx.Top,border=10)
        vbox.Add(hbox,proportion=1,flag=wx.CENTER)

        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON,self.on_click,id=10,id2=20)

    def on_click(self,event): #事件处理程序
        event_id=event.GetId()
        print(event_id)
        if event_id==10:
            self.staticText.SetLabelText("BUTTON1")
        else:
            self.staticText.SetLabelText("BUTTON2")
#创建窗口对象
frm=MyFrame()
#显示窗口
frm.Show()    #窗口 默认是隐藏 需要调用show方法才能显示
#进入主事件循环   事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示和响应用户事件的处理都是通过主事件循环实现的
app.MainLoop()
