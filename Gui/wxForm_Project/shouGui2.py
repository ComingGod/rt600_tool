import wx
import test2

class mainWin(test2.MyFrame1):
	def multi(self, event):
		gotValue = int(self.m_textCtrl1.GetValue())
		self.m_textCtrl2.SetValue(str(5*gotValue))


if __name__ == "__main__":
	app = wx.App()
	main_Win = mainWin(None)
	main_Win.Show()
	app.MainLoop()
