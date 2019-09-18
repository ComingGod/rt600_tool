#coding: utf-8
import os
import yaml
from Blhost import blhost
from GenImage import generate_image
from Gui import gui
from Jlink import jlink_debugger
import wx


filePath = os.path.abspath(os.getcwd()).replace('\\','/')
elftosbTool = os.path.join(filePath,'Tools/elftosb.exe').replace('\\', '/')
blhostTool = os.path.join(filePath, 'Tools/blhost.exe').replace('\\', '/')
enterDebugTool = os.path.join(filePath, 'Tools/tool.exe').replace('\\', '/')



# def ImageConfiguration(gui.MyFrame2):
#     def get_image_configration(self, event):
#     dicConfiguration = {}

#     dicConfiguration['inputImage'] = self.m_filePicker_input_image.GetPath().replace('\\', '/')

#     print dicConfiguration



class mainWin(gui.MyFrame2):

    def get_image_configration(self, event):
        dicConfiguration = {}
        dicConfiguration['inputImage'] = self.m_filePicker_input_image.GetPath().replace('\\', '/')
        dicConfiguration['linkAddr'] = self.m_textCtrl_link_address.GetValue()
        dicConfiguration['executeTarget'] = self.m_choice_image_execute_target.GetStringSelection()
        dicConfiguration['imageAuthType'] = self.m_choice_image_auth_type.GetStringSelection()
        dicConfiguration['imageEncKeyFile'] = self.m_filePicker_image_enc_key.GetPath().replace('\\', '/')
        dicConfiguration['keySource'] = self.m_choice_key_source.GetStringSelection()
        if self.m_checkBox_enable_trustzone.IsChecked():
            dicConfiguration['enableTrustZone'] = 'true'
        else:
            dicConfiguration['enableTrustZone'] = 'false'
        dicConfiguration['presetFile'] = self.m_filePicker_trustzone_presetfile.GetPath().replace('\\', '/')
        if self.m_checkBox_use_keystore.IsChecked():
            dicConfiguration['useKeystore'] = 'true'
        else:
            dicConfiguration['useKeystore'] = 'false'
        dicConfiguration['keyStoreFile'] = self.m_filePicker_keystore_file.GetPath().replace('\\', '/')
        dicConfiguration['certFile0'] = self.m_filePicker_cert_file0.GetPath().replace('\\', '/')
        dicConfiguration['certFile1'] = self.m_filePicker_cert_file1.GetPath().replace('\\', '/')
        dicConfiguration['certFile2'] = self.m_filePicker_cert_file2.GetPath().replace('\\', '/')
        dicConfiguration['certFile3'] = self.m_filePicker_cert_file3.GetPath().replace('\\', '/')
        dicConfiguration['privateKeyFile'] = self.m_filePicker_private_key_file.GetPath().replace('\\', '/')
        dicConfiguration['certChainID'] = self.m_choice_cert_chain_id.GetStringSelection()

        print dicConfiguration
        return dicConfiguration
    def genImage( self, event ):
        dicConfig = self.get_image_configration(event)

        genImage = generate_image.GenerateImage(elftosbTool = elftosbTool, jsonFile = 'test.json')
        genImage.generate_json_file(dicConfig)
        outputImage = genImage.generate_image()
        self.m_textCtrl_Log.Clear()
        self.m_textCtrl_Log.write(outputImage)

    def configImageConfiguration( self, event ):
        defaultInputImage = os.path.join(filePath, 'Material/inputImage/led_ram_0x1c000.bin').replace('\\', '/')
        self.m_filePicker_input_image.SetPath(defaultInputImage)
        defaultImageEncKey = os.path.join(filePath, 'Material/AESkey/userkey.txt')
        self.m_filePicker_image_enc_key.SetPath(defaultImageEncKey)
        defaultTrustzonePresetFile = os.path.join(filePath, 'Material/trustzonePresetFile/ledblinkTZMdata_ram.bin')
        self.m_filePicker_trustzone_presetfile.SetPath(defaultTrustzonePresetFile)
        defaultKeyStore = os.path.join(filePath, 'Material/AESkey/key_store_user.bin')
        self.m_filePicker_keystore_file.SetPath(defaultKeyStore)


        defaultCert0 = os.path.join(filePath, 'Material/keys_and_certs/rotk0_cert0_2048_noca.der.crt')
        self.m_filePicker_cert_file0.SetPath(defaultCert0)
        defaultCert1 = os.path.join(filePath, 'Material/keys_and_certs/rotk1_cert0_2048_noca.der.crt')
        self.m_filePicker_cert_file1.SetPath(defaultCert1)
        defaultCert2 = os.path.join(filePath, 'Material/keys_and_certs/rotk2_cert0_2048_noca.der.crt')
        self.m_filePicker_cert_file2.SetPath(defaultCert2)
        defaultCert3 = os.path.join(filePath, 'Material/keys_and_certs/rotk3_cert0_2048_noca.der.crt')
        self.m_filePicker_cert_file3.SetPath(defaultCert3)
        defaultPrivateKeyFile = os.path.join(filePath, 'Material/keys_and_certs/rotk0_cert0_2048.pem')
        self.m_filePicker_private_key_file.SetPath(defaultPrivateKeyFile)

        self.m_checkBox_use_keystore.SetValue(True) 
    def genKeystore( self, event ):
        uartPort = self.m_textCtrl_genKeystore_comPort.GetValue()
        userKeyFile = self.m_filePicker_userKey.GetPath().replace('\\', '/')
        keystoreReadFile = os.path.join(filePath, 'Material/AESkey/key_store_user.bin')

        bl = blhost.Blhost(blhostPath = blhostTool, peripheral = 'uart', uartPort = uartPort, jsonFormat = 'False')

        self.m_textCtrl_Log.Clear()
        outPut = bl.key_porvisioning()
        self.m_textCtrl_Log.write(outPut[0])
        if outPut[1] != '0 (0x0) Success.':
            assert 1 == 0


        outPut = bl.set_user_key(userKeyFile)
        self.m_textCtrl_Log.write(outPut[0])
        if outPut[1] != '0 (0x0) Success.':
            assert 1 == 0

        outPut = bl.read_key_store(keystoreReadFile)
        self.m_textCtrl_Log.write(outPut[0])
        if outPut[1] != '0 (0x0) Success.':
            assert 1 == 0

    def configshadowFuse( self, event ):
        jlinkID = self.m_textCtrl_run_jlinkID.GetValue()
        uartPort = self.m_textCtrl_run_uartPort.GetValue()

        configTarget = self.m_choice_config_fuseShadow_target.GetStringSelection()
        bootType = self.m_choice_config_fuse_shadow_boot_type.GetStringSelection()
        bootDevice = self.m_choice_config_fuse_shadow_boot_device.GetStringSelection()
    
        if configTarget == 'Shadow':
            jlink = jlink_debugger.JLink(jlinkID, 'Cortex-M33', enterDebugTool)
            self.m_textCtrl_Log.Clear()
            outPutJlink = jlink.enter_debug_session()
            self.m_textCtrl_Log.write(outPutJlink)
        elif configTarget == 'Fuse':
            bl = blhost.Blhost(blhostPath = blhostTool, peripheral = 'uart', uartPort = uartPort, jsonFormat = True)
            self.m_textCtrl_Log.Clear()

        if ('Secure boot' in bootType or 'Encrypt boot' in bootType):
            #write SRK
            self.m_textCtrl_Log.write('Writing SRK\n')
            if configTarget == 'Shadow':
                jlink.write_register(0x401301e0, 0x24371f32)
                jlink.write_register(0x401301e4, 0xb30bd1b5)
                jlink.write_register(0x401301e8, 0x3b70e2e6)
                jlink.write_register(0x401301ec, 0x1e1319d5)
                jlink.write_register(0x401301f0, 0x89e54def)
                jlink.write_register(0x401301f4, 0xf0d588b2)
                jlink.write_register(0x401301f8, 0x99f239d3)
                jlink.write_register(0x401301fc, 0x2f3f75ff)
                jlink.write_register(0x401301dc, 0x00010203)
            elif configTarget == 'Fuse':
                outPut = bl.efuse_program_once(0x78, '24371f32')
                self.m_textCtrl_Log.write(outPut[0])
                if outPut[1] != '0 (0x0) Success.':
                    assert 1 == 0
                outPut = bl.efuse_program_once(0x79, 'b30bd1b5')
                self.m_textCtrl_Log.write(outPut[0])
                if outPut[1] != '0 (0x0) Success.':
                    assert 1 == 0
                outPut = bl.efuse_program_once(0x7a, '3b70e2e6')
                self.m_textCtrl_Log.write(outPut[0])
                if outPut[1] != '0 (0x0) Success.':
                    assert 1 == 0
                outPut = bl.efuse_program_once(0x7b, '1e1319d5')
                self.m_textCtrl_Log.write(outPut[0])
                if outPut[1] != '0 (0x0) Success.':
                    assert 1 == 0
                outPut = bl.efuse_program_once(0x7c, '89e54def')
                self.m_textCtrl_Log.write(outPut[0])
                if outPut[1] != '0 (0x0) Success.':
                    assert 1 == 0
                outPut = bl.efuse_program_once(0x7d, 'f0d588b2')
                self.m_textCtrl_Log.write(outPut[0])
                if outPut[1] != '0 (0x0) Success.':
                    assert 1 == 0
                outPut = bl.efuse_program_once(0x7e, '99f239d3')
                self.m_textCtrl_Log.write(outPut[0])
                if outPut[1] != '0 (0x0) Success.':
                    assert 1 == 0
                outPut = bl.efuse_program_once(0x7f, '2f3f75ff')
                self.m_textCtrl_Log.write(outPut[0])
                if outPut[1] != '0 (0x0) Success.':
                    assert 1 == 0

        if ('OTP' in bootType):
            #write master key
            self.m_textCtrl_Log.write('Writing OTP key\n')
            if configTarget == 'Shadow':
                jlink.write_register(0x401301c0, 0xccddeeff)
                jlink.write_register(0x401301c4, 0x8899aabb)
                jlink.write_register(0x401301c8, 0x44556677)
                jlink.write_register(0x401301cc, 0x00112233)
                jlink.write_register(0x401301d0, 0x0c0d0e0f)
                jlink.write_register(0x401301d4, 0x08090a0b)
                jlink.write_register(0x401301d8, 0x04050607)
            elif configTarget == 'Fuse':
                outPut = bl.efuse_program_once(0x70, 'ccddeeff')
                self.m_textCtrl_Log.write(outPut[0])
                if outPut[1] != '0 (0x0) Success.':
                    assert 1 == 0
                outPut = bl.efuse_program_once(0x71, '8899aabb')
                self.m_textCtrl_Log.write(outPut[0])
                if outPut[1] != '0 (0x0) Success.':
                    assert 1 == 0
                outPut = bl.efuse_program_once(0x72, '44556677')
                self.m_textCtrl_Log.write(outPut[0])
                if outPut[1] != '0 (0x0) Success.':
                    assert 1 == 0
                outPut = bl.efuse_program_once(0x73, '00112233')
                self.m_textCtrl_Log.write(outPut[0])
                if outPut[1] != '0 (0x0) Success.':
                    assert 1 == 0
                outPut = bl.efuse_program_once(0x74, '0c0d0e0f')
                self.m_textCtrl_Log.write(outPut[0])
                if outPut[1] != '0 (0x0) Success.':
                    assert 1 == 0
                outPut = bl.efuse_program_once(0x75, '08090a0b')
                self.m_textCtrl_Log.write(outPut[0])
                if outPut[1] != '0 (0x0) Success.':
                    assert 1 == 0
                outPut = bl.efuse_program_once(0x76, '04050607')
                self.m_textCtrl_Log.write(outPut[0])
                if outPut[1] != '0 (0x0) Success.':
                    assert 1 == 0
                outPut = bl.efuse_program_once(0x77, '00010203')
                self.m_textCtrl_Log.write(outPut[0])
                if outPut[1] != '0 (0x0) Success.':
                    assert 1 == 0
        if ('PUF' in bootType):
            #enable PUF
            self.m_textCtrl_Log.write('Enable PUF\n')    
            if configTarget == 'Shadow':        
                jlink.write_register(0x40130194, 0x80)
            elif configTarget == 'Fuse':
                outPut = bl.efuse_program_once(0x65, '00000080')
                self.m_textCtrl_Log.write(outPut[0])
                if outPut[1] != '0 (0x0) Success.':
                    assert 1 == 0


        if bootDevice == 'Flexspi Nor': 
            if bootType == 'CRC':
                if configTarget == 'Shadow':        
                    outPutJlink = jlink.write_register(0x40130180, 0x1)
                    self.m_textCtrl_Log.write(outPutJlink)
                elif configTarget == 'Fuse':
                    outPut = bl.efuse_program_once(0x60, '00000001')
                    self.m_textCtrl_Log.write(outPut[0])
                    if outPut[1] != '0 (0x0) Success.':
                        assert 1 == 0
            else:
                if configTarget == 'Shadow':        
                    outPutJlink = jlink.write_register(0x40130180, 0x900001)
                    self.m_textCtrl_Log.write(outPutJlink)
                elif configTarget == 'Fuse':
                    outPut = bl.efuse_program_once(0x60, '00900001')
                    self.m_textCtrl_Log.write(outPut[0])
                    if outPut[1] != '0 (0x0) Success.':
                        assert 1 == 0

        if bootDevice == 'SPI': 
            if bootType == 'CRC':
                if configTarget == 'Shadow':        
                    outPutJlink = jlink.write_register(0x40130180, 0x4)
                    self.m_textCtrl_Log.write(outPutJlink)
                elif configTarget == 'Fuse':
                    outPut = bl.efuse_program_once(0x60, '00000004')
                    self.m_textCtrl_Log.write(outPut[0])
                    if outPut[1] != '0 (0x0) Success.':
                        assert 1 == 0
            else:
                if configTarget == 'Shadow':        
                    outPutJlink = jlink.write_register(0x40130180, 0x00900004)
                    self.m_textCtrl_Log.write(outPutJlink)
                elif configTarget == 'Fuse':
                    outPut = bl.efuse_program_once(0x60, '00900004')
                    self.m_textCtrl_Log.write(outPut[0])
                    if outPut[1] != '0 (0x0) Success.':
                        assert 1 == 0

        if bootDevice == 'UART': 
            if bootType == 'CRC':
                if configTarget == 'Shadow':        
                    outPutJlink = jlink.write_register(0x40130180, 0x6)
                    self.m_textCtrl_Log.write(outPutJlink)
                elif configTarget == 'Fuse':
                    outPut = bl.efuse_program_once(0x60, '00000006')
                    self.m_textCtrl_Log.write(outPut[0])
                    if outPut[1] != '0 (0x0) Success.':
                        assert 1 == 0
            else:
                if configTarget == 'Shadow':        
                    outPutJlink = jlink.write_register(0x40130180, 0x900006)
                    self.m_textCtrl_Log.write(outPutJlink)
                elif configTarget == 'Fuse':
                    outPut = bl.efuse_program_once(0x60, '00900006')
                    self.m_textCtrl_Log.write(outPut[0])
                    if outPut[1] != '0 (0x0) Success.':
                        assert 1 == 0

        if configTarget == 'Shadow':
            outPutJlink = jlink.reset()
            self.m_textCtrl_Log.write(outPutJlink)
            jlink.close_jlink()
        elif configTarget == 'Fuse':
   
            self.m_textCtrl_Log.write('Plese POR the device \n')




    def run( self, event ):
        uartPort = self.m_textCtrl_run_uartPort.GetValue()
        buspalPort = self.m_textCtrl_run_buspalPort.GetValue()
        FlexspiConfig0 = self.m_textCtrl_flexspi_config0.GetValue()
        FlexspiConfig1 = self.m_textCtrl_flexspi_config1.GetValue()
        imageAddr = self.m_textCtrl_image_addr.GetValue()
        print FlexspiConfig0
        print FlexspiConfig1
        print imageAddr


        bl = blhost.Blhost(blhostPath = blhostTool, peripheral = 'uart', uartPort = uartPort, jsonFormat = True)

        imageFile = os.path.join(filePath, 'image.bin').replace('\\', '/')

        bootDevice = self.m_choice_config_fuse_shadow_boot_device.GetStringSelection()
        if (bootDevice == 'Flexspi Nor'):
            self.m_textCtrl_Log.Clear()
            outPut = bl.fill_memory(0x1c000, 0x4, FlexspiConfig0)
            self.m_textCtrl_Log.write(outPut[0])
            if outPut[1] != '0 (0x0) Success.':
                assert 1 == 0
            outPut = bl.fill_memory(0x1c004, 0x4, FlexspiConfig1)
            self.m_textCtrl_Log.write(outPut[0])
            if outPut[1] != '0 (0x0) Success.':
                assert 1 == 0
            outPut = bl.configure_memory(0x9, 0x1c000)
            self.m_textCtrl_Log.write(outPut[0])
            if outPut[1] != '0 (0x0) Success.':
                assert 1 == 0
            outPut = bl.erase_region(0x08000000, 0x10000)
            self.m_textCtrl_Log.write(outPut[0])
            if outPut[1] != '0 (0x0) Success.':
                assert 1 == 0
            outPut = bl.fill_memory(0x1d000, 0x4, 0xf000000f)
            self.m_textCtrl_Log.write(outPut[0])
            if outPut[1] != '0 (0x0) Success.':
                assert 1 == 0
            outPut = bl.configure_memory(0x9, 0x1d000)
            self.m_textCtrl_Log.write(outPut[0])
            if outPut[1] != '0 (0x0) Success.':
                assert 1 == 0
            outPut = bl.write_memoty(imageAddr, imageFile)
            self.m_textCtrl_Log.write(outPut[0])
            if outPut[1] != '0 (0x0) Success.':
                assert 1 == 0
        if (bootDevice == 'UART'):
            self.m_textCtrl_Log.Clear()
            outPut = bl.write_memoty(0x1C000, imageFile)
            self.m_textCtrl_Log.write(outPut[0])
            if outPut[1] != '0 (0x0) Success.':
                assert 1 == 0
        if (bootDevice == 'SPI'):
            bl = blhost.Blhost( blhostPath = blhostTool, peripheral = 'spi', uartPort = buspalPort, jsonFormat = True)
            self.m_textCtrl_Log.Clear()
            outPut = bl.write_memoty(0x1C000, imageFile)
            self.m_textCtrl_Log.write(outPut[0])
            if outPut[1] != '0 (0x0) Success.':
                assert 1 == 0


if __name__ == '__main__':
    app = wx.App()

    main_win = mainWin(None)
    main_win.Show()

    app.MainLoop()

