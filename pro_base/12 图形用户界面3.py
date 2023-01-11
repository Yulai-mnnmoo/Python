#coding=utf-8
import wx
#创建应用程序对象
app=wx.App()
#自定义窗口类 MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='事件处理',size=(300,180),pos=(100,100))
        panel=wx.Panel(parent=self)
        self.staticText = wx.StaticText(parent=panel,label="请单击ok按钮")
        b = wx.Button(parent=panel, label='ok')
        self.Bind(wx.EVT_BUTTON,self.on_click,b)

        #创建垂直方向的盒子布局管理对象vbox
        vbox=wx.BoxSizer(wx.VERTICAL)
        #添加静态文本到vbox的布局管理器
        vbox.Add(self.staticText,proportion=1,flag=wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE|wx.Top,border=30) #wx.FIXED_MINSIZE  刚好包裹控件   wx.ALIGN_CENTER_HORIZONTAL 控制水平居中
        #添加按钮b到vbox布局管理器
        vbox.Add(b,proportion=1,flag=wx.EXPAND|wx.BOTTOM,border=10)  #wx.EXPAND  完全填满有效空间   propertion 都为1  所以两个控件各占1/2
        #设置面板panel 采用vbox布局管理器
        panel.SetSizer(vbox)  #两个控件都被放到面板中 所以需要设置面板布局为盒子布局
    def on_click(self,event): #事件处理程序
        self.staticText.SetLabelText("JJJJlk")
#创建窗口对象
frm=MyFrame()
#显示窗口
frm.Show()    #窗口 默认是隐藏 需要调用show方法才能显示
#进入主事件循环   事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示和响应用户事件的处理都是通过主事件循环实现的
app.MainLoop()
