
#coding=utf-8
import wx
#创建应用程序对象
app=wx.App()

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='文本输入控件',size=(300,260))
        panel=wx.Panel(parent=self)

        st1=wx.StaticText(panel,label='选择你喜欢的编程语言：')
        list1=['Python','Java','C++']
        lb1=wx.ListBox(panel,choices=list1,style=wx.LB_SINGLE)  #wx.LB_SINGLE  表示创建单选列表控件   参数choices用于设置选项
        self.Bind(wx.EVT_LISTBOX,self.on_list1,lb1)    #绑定列表选择事件

        st2 = wx.StaticText(panel, label='选择你喜欢吃的水果：')
        list2 = ['苹果', '橘子', '香蕉']
        lb2 = wx.ListBox(panel, choices=list2, style=wx.LB_EXTENDED)    #wx.LB_EXTENDED 表示创建多选列表控件
        self.Bind(wx.EVT_LISTBOX, self.on_list2, lb2)

        hbox1=wx.BoxSizer()
        hbox1.Add(st1,proportion=1,flag=wx.LEFT|wx.RIGHT,border=5)
        hbox1.Add(lb1,proportion=1)

        hbox2 = wx.BoxSizer()
        hbox2.Add(st2, proportion=1, flag=wx.LEFT | wx.RIGHT, border=5)
        hbox2.Add(lb2, proportion=1)

        vbox=wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox1,flag=wx.ALL|wx.EXPAND,border=5)
        vbox.Add(hbox2,flag=wx.ALL|wx.EXPAND,border=5)

        panel.SetSizer(vbox)

    def on_list1(self,event):
        listbox=event.GetEventObject()
        print('选择{}'.format(listbox.GetSelection()))  # GetSelection    返回单个选中项目的索引序号
    def on_list2(self,event):
        listbox=event.GetEventObject()
        print('选择{}'.format(listbox.GetSelections()))   # GetSelections  返回多个 选中项目索引列表
#创建窗口对象
frm=MyFrame()

#显示窗口
frm.Show()    #窗口 默认是隐藏 需要调用show方法才能显示

#进入主事件循环   事件循环是一种事件或消息分发处理机制，大部分图形用户界面在界面中的显示和响应用户事件的处理都是通过主事件循环实现的
app.MainLoop()

app=wx.App()

