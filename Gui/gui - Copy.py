# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tool", pos = wx.DefaultPosition, size = wx.Size( 693,477 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook4 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_configuration_panel = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText8 = wx.StaticText( self.m_configuration_panel, wx.ID_ANY, u"Property", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		gSizer1.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.m_textCtrl_property = wx.TextCtrl( self.m_configuration_panel, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl_property, 0, wx.ALL, 5 )

		self.run = wx.Button( self.m_configuration_panel, wx.ID_ANY, u"run", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.run, 0, wx.ALL, 5 )


		self.m_configuration_panel.SetSizer( gSizer1 )
		self.m_configuration_panel.Layout()
		gSizer1.Fit( self.m_configuration_panel )
		self.m_notebook4.AddPage( self.m_configuration_panel, u"Configuration", False )

		bSizer11.Add( self.m_notebook4, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_notebook5 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_log_panel = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_log_textCtrl = wx.TextCtrl( self.m_log_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 1000,1000 ), wx.TE_MULTILINE )
		self.m_log_textCtrl.SetMinSize( wx.Size( 1000,400 ) )
		self.m_log_textCtrl.SetMaxSize( wx.Size( 1000,-1 ) )

		bSizer14.Add( self.m_log_textCtrl, 0, wx.ALL, 5 )


		self.m_log_panel.SetSizer( bSizer14 )
		self.m_log_panel.Layout()
		bSizer14.Fit( self.m_log_panel )
		self.m_notebook5.AddPage( self.m_log_panel, u"Log", False )

		bSizer11.Add( self.m_notebook5, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.run.Bind( wx.EVT_BUTTON, self.get_property )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def get_property( self, event ):
		event.Skip()


