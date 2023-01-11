
#coding=utf-8
import wx
#创建应用程序对象
app=wx.App()

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='复选框和单选按钮，',size=(500,260))
        panel=wx.Panel(parent=self)

        st1=wx.StaticText(panel,label='选择你喜欢的编程语言：')
        cb1=wx.CheckBox(panel,id=1,label='Python')
        cb2 = wx.CheckBox(panel, id=2, label='java')
        cb2.SetValue(True)  #设置cb2的初始状态为选中
        cb3 = wx.CheckBox(panel, id=3, label='C++')

        self.Bind(wx.EVT_CHECKBOX,self.on_check_box,id=1,id2=3)  #绑定id为1~3的所有控件的事件处理到on_check_box方法

        st2=wx.StaticText(panel,label='选择性别')
        radio1=wx.RadioButton(panel,id=4,label='男',style=wx.RB_GROUP)  #设置style=wx.RB_GROUP是一个组的开始，直到遇到另外设置style=wx.RB_GROUP为止都是同一个组  所以radio1  radio2是同一组，且互斥
        radio2 = wx.RadioButton(panel, id=5, label='女')

        self.Bind(wx.EVT_RADIOBUTTON,self.on_radio_box,id=4,id2=5)  #定id为4~5的所有控件的事件处理到on_radio_box方法

        hbox1=wx.BoxSizer()
        hbox1.Add(st1,flag=wx.LEFT|wx.RIGHT,border=5)
        hbox1.Add(cb1)
        hbox1.Add(cb2)
        hbox1.Add(cb3)

        hbox2=wx.BoxSizer()
        hbox2.Add(st2,flag=wx.LEFT|wx.RIGHT,border=5)
        hbox2.Add(radio1)
        hbox2.Add(radio2)

        vbox=wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox1,flag=wx.ALL,border=10)
        vbox.Add(hbox2,flag=wx.ALL,border=10)

        #设置面板采用vbox布局管理器
        panel.SetSizer(vbox)

    def on_check_box(self,event):
        cb=event.GetEventObject()
        print("选择{0}，状态{1}".format(cb.GetLabel,event.IsChecked()))
    def on_radio_box(self,event):
        rb=event.GetEventObject()
        print("第一组，{1}被选中".format(rb.GetLabel))
#创建窗口对象
frm=MyFrame()

#显示窗口
frm.Show()    #窗口 默认是隐藏 需要调用show方法才能显示

#进入主事件循环   事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示和响应用户事件的处理都是通过主事件循环实现的
app.MainLoop()

app=wx.App()

