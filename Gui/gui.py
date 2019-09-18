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
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"RT600 Tool", pos = wx.DefaultPosition, size = wx.Size( 450,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		wSizer4 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_notebook5 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 450,400 ), 0 )
		self.m_panel5 = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText23 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Input Image", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
		self.m_staticText23.Wrap( -1 )

		gSizer3.Add( self.m_staticText23, 0, wx.ALL, 5 )

		self.m_filePicker_input_image = wx.FilePickerCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( -1,20 ), wx.FLP_DEFAULT_STYLE )
		gSizer3.Add( self.m_filePicker_input_image, 0, wx.ALL, 5 )

		self.m_staticText24 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Image Link address", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
		self.m_staticText24.Wrap( -1 )

		gSizer3.Add( self.m_staticText24, 0, wx.ALL, 5 )

		self.m_textCtrl_link_address = wx.TextCtrl( self.m_panel5, wx.ID_ANY, u"0x1c000", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
		gSizer3.Add( self.m_textCtrl_link_address, 0, wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Image Execute Target", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
		self.m_staticText25.Wrap( -1 )

		gSizer3.Add( self.m_staticText25, 0, wx.ALL, 5 )

		m_choice_image_execute_targetChoices = [ u"RAM", u"External flash (XIP)" ]
		self.m_choice_image_execute_target = wx.Choice( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,20 ), m_choice_image_execute_targetChoices, 0 )
		self.m_choice_image_execute_target.SetSelection( 0 )
		gSizer3.Add( self.m_choice_image_execute_target, 0, wx.ALL, 5 )

		self.m_staticText26 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Image Authen Type", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
		self.m_staticText26.Wrap( -1 )

		gSizer3.Add( self.m_staticText26, 0, wx.ALL, 5 )

		m_choice_image_auth_typeChoices = [ u"Encrypted + Signed", u"Signed", u"crc" ]
		self.m_choice_image_auth_type = wx.Choice( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,20 ), m_choice_image_auth_typeChoices, 0 )
		self.m_choice_image_auth_type.SetSelection( 2 )
		gSizer3.Add( self.m_choice_image_auth_type, 0, wx.ALL, 5 )

		self.m_staticText27 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Image Encryption Key", wx.DefaultPosition, wx.Size( -1,25 ), 0 )
		self.m_staticText27.Wrap( -1 )

		gSizer3.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.m_filePicker_image_enc_key = wx.FilePickerCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( -1,20 ), wx.FLP_DEFAULT_STYLE )
		gSizer3.Add( self.m_filePicker_image_enc_key, 0, wx.ALL, 5 )

		self.m_staticText28 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Device Key Source", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		gSizer3.Add( self.m_staticText28, 0, wx.ALL, 5 )

		m_choice_key_sourceChoices = [ u"Key Store", u"OTP" ]
		self.m_choice_key_source = wx.Choice( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,20 ), m_choice_key_sourceChoices, 0 )
		self.m_choice_key_source.SetSelection( 0 )
		gSizer3.Add( self.m_choice_key_source, 0, wx.ALL, 5 )

		self.m_staticText29 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Enable TrustZone", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		gSizer3.Add( self.m_staticText29, 0, wx.ALL, 5 )

		self.m_checkBox_enable_trustzone = wx.CheckBox( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_checkBox_enable_trustzone, 0, wx.ALL, 5 )

		self.m_staticText30 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"TrustZone preset", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		gSizer3.Add( self.m_staticText30, 0, wx.ALL, 5 )

		self.m_filePicker_trustzone_presetfile = wx.FilePickerCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( -1,20 ), wx.FLP_DEFAULT_STYLE )
		gSizer3.Add( self.m_filePicker_trustzone_presetfile, 0, wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Use Key Store", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		gSizer3.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.m_checkBox_use_keystore = wx.CheckBox( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_checkBox_use_keystore, 0, wx.ALL, 5 )

		self.m_staticText32 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Key Store File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		gSizer3.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.m_filePicker_keystore_file = wx.FilePickerCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( -1,20 ), wx.FLP_DEFAULT_STYLE )
		gSizer3.Add( self.m_filePicker_keystore_file, 0, wx.ALL, 5 )

		self.m_staticText35 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Cert File 0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		gSizer3.Add( self.m_staticText35, 0, wx.ALL, 5 )

		self.m_filePicker_cert_file0 = wx.FilePickerCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( -1,20 ), wx.FLP_DEFAULT_STYLE )
		gSizer3.Add( self.m_filePicker_cert_file0, 0, wx.ALL, 5 )

		self.m_staticText36 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Cert File 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		gSizer3.Add( self.m_staticText36, 0, wx.ALL, 5 )

		self.m_filePicker_cert_file1 = wx.FilePickerCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( -1,20 ), wx.FLP_DEFAULT_STYLE )
		gSizer3.Add( self.m_filePicker_cert_file1, 0, wx.ALL, 5 )

		self.m_staticText37 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Cert File 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )

		gSizer3.Add( self.m_staticText37, 0, wx.ALL, 5 )

		self.m_filePicker_cert_file2 = wx.FilePickerCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( -1,20 ), wx.FLP_DEFAULT_STYLE )
		gSizer3.Add( self.m_filePicker_cert_file2, 0, wx.ALL, 5 )

		self.m_staticText38 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Cert File 3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )

		gSizer3.Add( self.m_staticText38, 0, wx.ALL, 5 )

		self.m_filePicker_cert_file3 = wx.FilePickerCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( -1,20 ), wx.FLP_DEFAULT_STYLE )
		gSizer3.Add( self.m_filePicker_cert_file3, 0, wx.ALL, 5 )

		self.m_staticText39 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Private Key File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )

		gSizer3.Add( self.m_staticText39, 0, wx.ALL, 5 )

		self.m_filePicker_private_key_file = wx.FilePickerCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( -1,20 ), wx.FLP_DEFAULT_STYLE )
		gSizer3.Add( self.m_filePicker_private_key_file, 0, wx.ALL, 5 )

		self.m_staticText40 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Cert Chain ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )

		gSizer3.Add( self.m_staticText40, 0, wx.ALL, 5 )

		m_choice_cert_chain_idChoices = [ u"0", u"1", u"2", u"3" ]
		self.m_choice_cert_chain_id = wx.Choice( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,20 ), m_choice_cert_chain_idChoices, 0 )
		self.m_choice_cert_chain_id.SetSelection( 0 )
		gSizer3.Add( self.m_choice_cert_chain_id, 0, wx.ALL, 5 )

		self.m_button_genImage = wx.Button( self.m_panel5, wx.ID_ANY, u"GenIMG", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button_genImage, 0, wx.ALL, 5 )

		self.m_button_reConfig = wx.Button( self.m_panel5, wx.ID_ANY, u"Confg", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button_reConfig, 0, wx.ALL, 5 )


		self.m_panel5.SetSizer( gSizer3 )
		self.m_panel5.Layout()
		gSizer3.Fit( self.m_panel5 )
		self.m_notebook5.AddPage( self.m_panel5, u"Generate Image", False )
		self.m_panel231 = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer51 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText81 = wx.StaticText( self.m_panel231, wx.ID_ANY, u"ComPort", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		gSizer51.Add( self.m_staticText81, 0, wx.ALL, 5 )

		self.m_textCtrl_genKeystore_comPort = wx.TextCtrl( self.m_panel231, wx.ID_ANY, u"com10", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer51.Add( self.m_textCtrl_genKeystore_comPort, 0, wx.ALL, 5 )

		self.m_staticText661 = wx.StaticText( self.m_panel231, wx.ID_ANY, u"UserKey", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText661.Wrap( -1 )

		gSizer51.Add( self.m_staticText661, 0, wx.ALL, 5 )

		self.m_filePicker_userKey = wx.FilePickerCtrl( self.m_panel231, wx.ID_ANY, u".\\Material\\AESkey\\userkey.bin", u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		gSizer51.Add( self.m_filePicker_userKey, 0, wx.ALL, 5 )

		self.m_button_genKeystore1 = wx.Button( self.m_panel231, wx.ID_ANY, u"GenKeyStore", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer51.Add( self.m_button_genKeystore1, 0, wx.ALL, 5 )


		self.m_panel231.SetSizer( gSizer51 )
		self.m_panel231.Layout()
		gSizer51.Fit( self.m_panel231 )
		self.m_notebook5.AddPage( self.m_panel231, u"Generate KeyStore", True )
		self.m_panel37 = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText_uartPort = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Uart Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_uartPort.Wrap( -1 )

		gSizer9.Add( self.m_staticText_uartPort, 0, wx.ALL, 5 )

		self.m_textCtrl_run_uartPort = wx.TextCtrl( self.m_panel37, wx.ID_ANY, u"com10", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_textCtrl_run_uartPort, 0, wx.ALL, 5 )

		self.m_staticText74 = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Buspal Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText74.Wrap( -1 )

		gSizer9.Add( self.m_staticText74, 0, wx.ALL, 5 )

		self.m_textCtrl_run_buspalPort = wx.TextCtrl( self.m_panel37, wx.ID_ANY, u"com14", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_textCtrl_run_buspalPort, 0, wx.ALL, 5 )

		self.m_staticText75 = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Jlink ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText75.Wrap( -1 )

		gSizer9.Add( self.m_staticText75, 0, wx.ALL, 5 )

		self.m_textCtrl_run_jlinkID = wx.TextCtrl( self.m_panel37, wx.ID_ANY, u"600111626", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_textCtrl_run_jlinkID, 0, wx.ALL, 5 )

		self.m_staticText69 = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Target", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( -1 )

		gSizer9.Add( self.m_staticText69, 0, wx.ALL, 5 )

		m_choice_config_fuseShadow_targetChoices = [ u"Fuse", u"Shadow" ]
		self.m_choice_config_fuseShadow_target = wx.Choice( self.m_panel37, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_config_fuseShadow_targetChoices, 0 )
		self.m_choice_config_fuseShadow_target.SetSelection( 1 )
		gSizer9.Add( self.m_choice_config_fuseShadow_target, 0, wx.ALL, 5 )

		self.m_staticText70 = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Boot Type", wx.Point( 50,50 ), wx.DefaultSize, 0 )
		self.m_staticText70.Wrap( -1 )

		gSizer9.Add( self.m_staticText70, 0, wx.ALL, 5 )

		m_choice_config_fuse_shadow_boot_typeChoices = [ u"CRC", u"Secure boot with OTP", u"Secure boot with PUF", u"Encrypt boot with OTP", u"Encrypt boot with PUF", u"XIP Secure boot", wx.EmptyString ]
		self.m_choice_config_fuse_shadow_boot_type = wx.Choice( self.m_panel37, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_config_fuse_shadow_boot_typeChoices, 0 )
		self.m_choice_config_fuse_shadow_boot_type.SetSelection( 0 )
		gSizer9.Add( self.m_choice_config_fuse_shadow_boot_type, 0, wx.ALL, 5 )

		self.m_staticText71 = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Boot Device", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )

		gSizer9.Add( self.m_staticText71, 0, wx.ALL, 5 )

		m_choice_config_fuse_shadow_boot_deviceChoices = [ u"SPI", u"UART", u"Flexspi Nor" ]
		self.m_choice_config_fuse_shadow_boot_device = wx.Choice( self.m_panel37, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_config_fuse_shadow_boot_deviceChoices, 0 )
		self.m_choice_config_fuse_shadow_boot_device.SetSelection( 2 )
		gSizer9.Add( self.m_choice_config_fuse_shadow_boot_device, 0, wx.ALL, 5 )

		self.m_staticText371 = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Image Addr", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText371.Wrap( -1 )

		gSizer9.Add( self.m_staticText371, 0, wx.ALL, 5 )

		self.m_textCtrl_image_addr = wx.TextCtrl( self.m_panel37, wx.ID_ANY, u"0x1c000", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_textCtrl_image_addr, 0, wx.ALL, 5 )

		self.m_staticText381 = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Flexspi Config0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText381.Wrap( -1 )

		gSizer9.Add( self.m_staticText381, 0, wx.ALL, 5 )

		self.m_textCtrl_flexspi_config0 = wx.TextCtrl( self.m_panel37, wx.ID_ANY, u"0xc0000001", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_textCtrl_flexspi_config0, 0, wx.ALL, 5 )

		self.m_staticText391 = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Flexspi Config1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText391.Wrap( -1 )

		gSizer9.Add( self.m_staticText391, 0, wx.ALL, 5 )

		self.m_textCtrl_flexspi_config1 = wx.TextCtrl( self.m_panel37, wx.ID_ANY, u"0x0", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_textCtrl_flexspi_config1, 0, wx.ALL, 5 )

		self.m_button27 = wx.Button( self.m_panel37, wx.ID_ANY, u"Config Fuse/Shadow", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_button27, 0, wx.ALL, 5 )

		self.m_button15 = wx.Button( self.m_panel37, wx.ID_ANY, u"Download Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_button15, 0, wx.ALL, 5 )


		self.m_panel37.SetSizer( gSizer9 )
		self.m_panel37.Layout()
		gSizer9.Fit( self.m_panel37 )
		self.m_notebook5.AddPage( self.m_panel37, u"Config/Run", False )

		wSizer4.Add( self.m_notebook5, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer7.Add( wSizer4, 1, wx.EXPAND, 5 )

		self.m_notebook101 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,650 ), 0 )
		self.m_panel121 = wx.Panel( self.m_notebook101, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer811 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl_Log = wx.TextCtrl( self.m_panel121, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 450,650 ), wx.TE_MULTILINE )
		bSizer811.Add( self.m_textCtrl_Log, 0, wx.ALL, 5 )


		self.m_panel121.SetSizer( bSizer811 )
		self.m_panel121.Layout()
		bSizer811.Fit( self.m_panel121 )
		self.m_notebook101.AddPage( self.m_panel121, u"Log", False )

		bSizer7.Add( self.m_notebook101, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button_genImage.Bind( wx.EVT_BUTTON, self.genImage )
		self.m_button_reConfig.Bind( wx.EVT_BUTTON, self.configImageConfiguration )
		self.m_button_genKeystore1.Bind( wx.EVT_BUTTON, self.genKeystore )
		self.m_button27.Bind( wx.EVT_BUTTON, self.configshadowFuse )
		self.m_button15.Bind( wx.EVT_BUTTON, self.run )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def genImage( self, event ):
		event.Skip()

	def configImageConfiguration( self, event ):
		event.Skip()

	def genKeystore( self, event ):
		event.Skip()

	def configshadowFuse( self, event ):
		event.Skip()

	def run( self, event ):
		event.Skip()


