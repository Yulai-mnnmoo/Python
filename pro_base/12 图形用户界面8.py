
#coding=utf-8
import wx
#创建应用程序对象
app=wx.App()

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='文本输入控件',size=(300,260))
        self.panel=wx.Panel(parent=self)   #创建一个面板 他是该类的实例变量

        self.bmps=[wx.Bitmap('logo.png',wx.BITMAP_TYPE_PNG),wx.Bitmap('logo2.png',wx.BITMAP_TYPE_PNG),wx.Bitmap('logo3.jpg',wx.BITMAP_TYPE_JPEG)]  #创建wx.Bitmap的列表对象

        b1=wx.Button(self.panel,id=1,label="Button1")
        b2= wx.Button(self.panel, id=2, label="Button2")
        self.Bind(wx.EVT_BUTTON,self.on_click,id=1,id2=2)

        self.image=wx.StaticBitmap(self.panel,bitmap=self.bmps[0])  #静态图片控件对象  self.bmps[0]是静态图片控件要显示的图片对象

        vbox=wx.BoxSizer(wx.VERTICAL)
        vbox.Add(b1,proportion=1,flag=wx.EXPAND)
        vbox.Add(b2, proportion=1, flag=wx.EXPAND)
        vbox.Add(self.image, proportion=3, flag=wx.EXPAND)

        self.panel.SetSizer(vbox)

    def on_click(self,event):
        event_id=event.GetId()
        if event_id==1:
            self.image.SetBitmap(self.bmps[1])   #重新设置图片 实现图片切换
        else:
            self.image.SetBitmap(self.bmps[2])

        self.panel.Layout()   #重新设置面板布局

#创建窗口对象
frm=MyFrame()

#显示窗口
frm.Show()    #窗口 默认是隐藏 需要调用show方法才能显示

#进入主事件循环   事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示和响应用户事件的处理都是通过主事件循环实现的
app.MainLoop()

app=wx.App()

