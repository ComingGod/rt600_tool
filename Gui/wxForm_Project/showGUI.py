
#coding: utf-8
import mytestwxForm
import wx

value = ''''
blhost -p com10 -- reset
{
	response: 0 successfully
	value : 0 



}
   			'''


# 创建mainWin类并传入my_win.MyFrame1
class mainWin(mytestwxForm.MyFrame1):

   # 实现Button控件的响应函数showMessage


   def showMsg(self, event):


       self.m_textCtrl1.Clear()
       self.m_textCtrl1.SetValue(value)

if __name__ == '__main__':
    # 下面是使用wxPython的固定用法
    app = wx.App()

    main_win = mainWin(None)
    main_win.Show()

    app.MainLoop()