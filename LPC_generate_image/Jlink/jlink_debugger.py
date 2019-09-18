# import os
# import subprocess
# import pylink
# import time

# class JLink(object):
#     def __init__(self, jlinkID, deviceName):
        
#         self.jlinkID = jlinkID
#         self.deviceName = deviceName
#         self.jlink = pylink.JLink()

#     def check_connect(self):
#         # jlink = pylink.JLink()
#         self.jlink.open(self.jlinkID)
#         self.jlink.set_tif(pylink.enums.JLinkInterfaces.SWD)
#         try:
#             self.jlink.connect(self.deviceName)
#         except pylink.errors.JLinkException:
#             return "Jlink doesn't be connected"
#         if self.jlink.target_connected():
#             return "Jlink connected"

#     def enter_debug_session(self):

#         currentDir = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')
#         enterMailbox = os.path.abspath(os.path.join(currentDir, '../Tools/tool.exe -p 1.0 -i jlink start')).replace('\\', '/')
#         process = subprocess.Popen(enterMailbox, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#         output1, error = process.communicate()
#         print output1


#         time.sleep(1)
#         enabldDebugCmd = os.path.abspath(os.path.join(currentDir, '../Tools/tool.exe -p 1.0 -i jlink enterdebug')).replace('\\', '/')
#         process = subprocess.Popen(enabldDebugCmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#         output2, error = process.communicate()
#         time.sleep(1)
#         print output2

#         return output1 + output2 + '\n'


#     def Reset(self):
#         if (self.check_connect() == "Jlink doesn't be connected"):
#             assert 1 ==0
#         else:
#             print 'jlink connected'
#         print self.jlink.reset(ms = 100, halt = False)
#         print 'reset'
#         return '--- Jlink Reset--- \n'
#         # self.jlink.close()

#     def write_register(self, destimation, value):
#         if (self.check_connect() == "Jlink doesn't be connected"):           
#             assert 1 == 0
#         else:
#             print 'jlink connected'
#         Data = []
#         Data.append(value)
#         self.jlink.flash_write32(addr = destimation, data = Data)
#         print 'writing %x: %x\n' %(destimation, value)
#         return 'Writing 0x%x ==> 0x%x\n' %(destimation, value)



# if __name__ == '__main__':

#     jlink = JLink(600111626, 'Cortex-M33')
#     jlink.enter_debug_session()
#     jlink.write_register(0x40130180, 0x900001)
#     jlink.write_register(0x40130194, 0x80)
#     jlink.write_register(0x401301e0, 0x24371f32)
#     jlink.write_register(0x401301e4, 0xb30bd1b5)
#     jlink.write_register(0x401301e8, 0x3b70e2e6)
#     jlink.write_register(0x401301ec, 0x1e1319d5)
#     jlink.write_register(0x401301f0, 0x89e54def)
#     jlink.write_register(0x401301f4, 0xf0d588b2)
#     jlink.write_register(0x401301f8, 0x99f239d3)
#     jlink.write_register(0x401301fc, 0x2f3f75ff)

#     print jlink.Reset()
#     print 'writing %s: %s\n' %('destimation', 'value')

import os
import subprocess
import pylink
import time

class JLink(object):
    def __init__(self, jlinkID, deviceName, enterDebugTool):
        
        self.jlinkID = jlinkID
        self.deviceName = deviceName
        self.jlink = pylink.JLink()
        self.enterDebugTool = enterDebugTool

    def check_connect(self):
        # jlink = pylink.JLink()
        try:
            self.jlink.open(self.jlinkID)
        except pylink.errors.JLinkException:
            print 'jlink emulator connect failed'
        # self.jlink.set_tif(pylink.enums.JLinkInterfaces.SWD)
        try:
            self.jlink.connect(self.deviceName)
        except pylink.errors.JLinkException:
            return "connect Jlink raise a Exception"
        if self.jlink.target_connected():
            return "Jlink connected"
        else:
            return 'Jlink connected failed'

    def enter_debug_session(self):

        # currentDir = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')
        # enterMailbox = os.path.abspath(os.path.join(currentDir, '../Tools/tool.exe -p 1.0 -i jlink start')).replace('\\', '/')
        enterMailbox = self.enterDebugTool + ' -p 1.0 -i jlink start'
        print enterMailbox
        process = subprocess.Popen(enterMailbox, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output1, error = process.communicate()
        print output1
        time.sleep(1)
        # enabldDebugCmd = os.path.abspath(os.path.join(currentDir, '../Tools/tool.exe -p 1.0 -i jlink enterdebug')).replace('\\', '/')

        enabldDebugCmd = self.enterDebugTool + ' -p 1.0 -i jlink enterdebug'
        process = subprocess.Popen(enabldDebugCmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output2, error = process.communicate()
        time.sleep(1)
        print output2

        try:
            jlinkStatus = self.check_connect()
            print jlinkStatus
        except:
            self.close_jlink()

        return output1 + output2 + '\n' + str(jlinkStatus) + '\n'


    def reset(self):
        try:
            self.jlink.reset(ms = 100, halt = False)
        except:
            self.close_jlink()
        print 'reset'
        return '--- Jlink Reset--- \n'
        # self.jlink.close()

    def write_register(self, destimation, value):
        Data = []
        Data.append(value)
        try:
            self.jlink.flash_write32(addr = destimation, data = Data)
        except:
            self.close_jlink()
        print 'writing 0x%x ==> 0x%x\n' %(destimation, value)
        return 'Writing 0x%x ==> 0x%x\n' %(destimation, value)

    def close_jlink(self):
        try:
            self.jlink.close()
        except:
            return 'Close Jlink failed'




if __name__ == '__main__':

    # currentDir = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')
    # enterMailbox = os.path.abspath(os.path.join(currentDir, '../Tools/tool.exe -p 1.0 -i jlink start')).replace('\\', '/')
    # process = subprocess.Popen(enterMailbox, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # output1, error = process.communicate()
    # print output1


    # time.sleep(1)
    # enabldDebugCmd = os.path.abspath(os.path.join(currentDir, '../Tools/tool.exe -p 1.0 -i jlink enterdebug')).replace('\\', '/')
    # process = subprocess.Popen(enabldDebugCmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # output2, error = process.communicate()
    # time.sleep(1)
    # print output2

    # test = pylink.JLink()
    # test.open(600111626)
    # test.connect('Cortex-M33')
    # print test.memory_read8(0x1c000, 0x10)



    jlink = JLink(600111626, 'Cortex-M33')
    jlink.enter_debug_session()
    jlink.write_register(0x401301e0, 0x24371f32)
    jlink.write_register(0x401301e4, 0xb30bd1b5)
    jlink.write_register(0x401301e8, 0x3b70e2e6)
    jlink.write_register(0x401301ec, 0x1e1319d5)
    jlink.write_register(0x401301f0, 0x89e54def)
    jlink.write_register(0x401301f4, 0xf0d588b2)
    jlink.write_register(0x401301f8, 0x99f239d3)
    jlink.write_register(0x401301fc, 0x2f3f75ff)

    #write master key
    jlink.write_register(0x401301c0, 0xccddeeff)
    jlink.write_register(0x401301c4, 0x8899aabb)
    jlink.write_register(0x401301c8, 0x44556677)
    jlink.write_register(0x401301cc, 0x00112233)
    jlink.write_register(0x401301d0, 0x0c0d0e0f)
    jlink.write_register(0x401301d4, 0x08090a0b)
    jlink.write_register(0x401301d8, 0x04050607)

    jlink.write_register(0x40130180, 0x900004)


    jlink.reset()
    jlink.close_jlink()




# import os
# import sys
# import random
# import inspect
# import string
# import subprocess
# import time
# import glob
# import threading
# import logging

# class JLink():
#     def __init__(self, jlinkUsbId, deviceName):
#         self._jlinkUsbId = jlinkUsbId
#         self._deviceName = deviceName
#         self._jlinkInterface = "SWD"        # Use "SWD" as default device interface

#         # Should add two system variables: SEGGER, MinGW
#         self._jlinkGdbServerClExe = os.path.expandvars('%SEGGER%\\JLinkGDBServerCL.exe')
#         self._jlinkExe = os.path.expandvars('%SEGGER%\\JLink.exe')
#         # self._jlinkExe = "C:\\Program Files (x86)\\SEGGER\\JLink\\JLink.exe"
#         # self._jlinkExe = r"C:\Program Files (x86)\IAR Systems\Embedded Workbench 8.0\arm\bin\jlink.exe"
#         self._gdbExe = os.path.expandvars('%MinGW%\\bin\\gdb.exe')

#         thisFile = inspect.getfile(inspect.currentframe())
#         self._currentPath = os.path.abspath(os.path.dirname(thisFile))

     
#     # @breif Command execution.    
#     def run_script(self, filename, timeout_sec=18):
#         """Run jlink script with JLink.exe under a timeout.

#         Arguments:
#             filename -- {string} path to jlink script
#             timeout_sec -- {int} seconds for timeout value

#         Returns:
#             tuple -- (jlink_exit_code, console_output)
#         """
#         _params = [
#             self._jlinkExe,
#             "-SelectEmuBySN",
#             "{0}".format(self._jlinkUsbId),
#             "-Device",
#             "{0}".format(self._deviceName),
#             "-IF",
#             "{0}".format(self._jlinkInterface), # Use "SWD" as default device interface
#             "-Speed",
#             "auto",
#             "-ExitOnError",
#             "-CommanderScript",
#             filename
#         ]
#         process = subprocess.Popen(_params, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell = True)
#         # print process.communicate()[0]

#         if timeout_sec is not None:
#             # Use a timer to stop the subprocess if the timeout is exceeded.
#             # This helps prevent very subtle issues with deadlocks on reading
#             # subprocess output.  See: http://stackoverflow.com/a/10012262
#             def timeout_exceeded(p):
#                 # Stop the subprocess and kill the whole program.
#                 p.kill()
#                 raise Exception('JLink process exceeded timeout!')

#             timeout = threading.Timer(timeout_sec, timeout_exceeded, [process])
#             timeout.start()

#         if self._jlinkInterface.upper() == "JTAG":
#             process.stdin.write("-1,-1\r\n")

#         # Grab output of JLink.
#         output, err = process.communicate()
#         if timeout_sec is not None:
#             # Stop timeout timer when communicate call returns.
#             timeout.cancel()


#         # logging.debug('JLink response: {0}'.format(output))
#         # logging.info(output)
#         return process.returncode, output
            
#     # @brief Unlock the Kinetis device by JLink command line.
#     def unlock(self):
#         commands = ["si {0}".format(self._jlinkInterface), # Use "SWD" as default device interface
#                     "speed 100",
#                     "rnh", 
#                     "unlock kinetis",
#                     "qc"
#         ]
#         cmdFile = os.path.join(self._currentPath, 'unlock_%d.jlink'%(random.randint(10000, 80000))) 
#         fileObj = file(cmdFile, 'w+')
#         for cmd in commands:
#             print >> fileObj, cmd
#         fileObj.close()

#         returncode, output = self.run_script(cmdFile)
#         logging.info('Unlock Device:\n%s'%output)
#         os.remove(cmdFile)
     
#     # @brief Erase the whole internal flash by JLink command line.
#     def erase(self):        
#         commands = ["r",        # Reset
#                     "erase",    # Erase
#                     "r",        # Reset
#                     "qc"        # Quit
#         ]
#         cmdFile = os.path.join(self._currentPath, 'erase_%d.jlink'%(random.randint(10000, 80000)))
#         print cmdFile
#         fileObj = file(cmdFile, 'w+')
#         for cmd in commands:
#             print >> fileObj, cmd
#         fileObj.close() 
#         returncode, output = self.run_script(cmdFile)
#         logging.info('Erase Internal Flash:\n%s'%output)
#         os.remove(cmdFile)

#     # @brief Reset the device by JLink command line
#     def reset(self):
#         commands = ["rnh",        # Reset chip and not halt
#                     "qc"        # Quit
#         ]
#         cmdFile = os.path.join(self._currentPath, 'reset_%d.jlink'%(random.randint(10000, 80000)))
#         fileObj = file(cmdFile, 'w+')
#         for cmd in commands:
#             print >> fileObj, cmd
#         fileObj.close() 
#         returncode, output = self.run_script(cmdFile)
#         logging.info('returncode:\n%s',returncode)
#         logging.info('Reset Device:\n%s'%output)
#         os.remove(cmdFile)
#         # assert returncode == 0
#         return output + '\n'


#     def enter_debug_session(self):

#         currentDir = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')
#         print currentDir
#         enterMailbox = os.path.abspath(os.path.join(currentDir, '../Tools/tool.exe -p 1.0 -i jlink start')).replace('\\', '/')
#         process = subprocess.Popen(enterMailbox, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#         output1, error = process.communicate()
 
#         time.sleep(1)
#         enabldDebugCmd = os.path.abspath(os.path.join(currentDir, '../Tools/tool.exe -p 1.0 -i jlink enterdebug')).replace('\\', '/')
#         process = subprocess.Popen(enabldDebugCmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#         output2, error = process.communicate()
#         time.sleep(1)

#         return output1 + '\n' + output2 + '\n'

#     def debug_authen(self):

#         currentDir = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')
#         # print currentDir
#         # debugDir = currentDir + '/../../OtherCases/Debug_authentication/1_test_SOCU_single_cert_2KnoCA_ROTK0'
#         # os.chdir(debugDir)
#         # debugDir = os.getcwd().replace('\\', '/')

#         debugAuthenticationCmd = os.path.abspath(os.path.join(currentDir, '../Tool/tool.exe -p 1.0 -i jlink auth -c debug_auth.yml')).replace('\\', '/')
#         print debugAuthenticationCmd
#         process = subprocess.Popen(debugAuthenticationCmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#         output, error = process.communicate()
#         logging.info(output)

#         time.sleep(1)
#         exitCmd = os.path.abspath(os.path.join(currentDir, '../Tool/tool.exe -p 1.0 -i jlink exit')).replace('\\', '/')
#         process = subprocess.Popen(exitCmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#         output, error = process.communicate()
#         logging.info(output)
#         time.sleep(1)



#     def check_connection(self):
#         time.sleep(1)
#         commands = ["usb",
#                     "connect",
#                     "qc"

#         ]
#         cmdFile = os.path.join(self._currentPath, 'write_register_%d.jlink'%(random.randint(10000, 80000)))
#         fileObj = file(cmdFile, 'w+')
#         for cmd in commands:
#             print >> fileObj, cmd
#         fileObj.close() 
#         returncode, output = self.run_script(cmdFile)
#         logging.info('returncode:%s',returncode)
#         logging.info('write :\n%s'%output)
#         os.remove(cmdFile)
#         # assert returncode == 0




#     def write_register(self, destimation, value):
#         commands = ["w4 " + hex(destimation) + ' ' + hex(value) ,
#                     # destimation ,
#                     # value ,        # write value to register
#                     "qc"        # Quit
#         ]
#         cmdFile = os.path.join(self._currentPath, 'write_register_%d.jlink'%(random.randint(10000, 80000)))
#         print cmdFile
#         fileObj = file(cmdFile, 'w+')
#         for cmd in commands:
#             print >> fileObj, cmd
#         fileObj.close() 
#         returncode, output = self.run_script(cmdFile)
#         print 'run'
#         logging.info('returncode:%s',returncode)
#         logging.info('write :\n%s'%output)
#         # os.remove(cmdFile)
#         # assert returncode == 0
#         return output


#     def read_register(self, filename, address, size):
#         commands = ["savebin " + filename + ' ' + hex(address).strip('L') + ' ' + hex(size),
#                     # filename ,
#                     # address ,     # read value from register
#                     "qc"            # Quit
#         ]
#         cmdFile = os.path.join(self._currentPath, 'read_register_%d.jlink'%(random.randint(10000, 80000)))

#         # print cmdFile
#         fileObj = file(cmdFile, 'w+')
#         for cmd in commands:
#             print >> fileObj, cmd
#         fileObj.close() 
#         returncode, output = self.run_script(cmdFile)
#         logging.info('Reset Device:\n%s'%output)
#         os.remove(cmdFile)

#     # @brief Flash image to the device by JLink command line
#     def flash_image(self, hexFile, binFile, targetName, projectName):
#         # Get SP and PC from the given bin file. SP: the first four bytes, PC: the second four bytes.
#         fileObj = file(binFile, 'rb')
#         data = fileObj.read(8)
#         fileObj.close()
#         SP = hex(ord(data[0]) | (ord(data[1]) << 8) | (ord(data[2]) << 16) | (ord(data[3]) << 24))
#         PC = hex(ord(data[4]) | (ord(data[5]) << 8) | (ord(data[6]) << 16) | (ord(data[7]) << 24))
#         cmdFile = os.path.join(self._currentPath, 'flash_image_%d.jlink'%(random.randint(10000, 80000)))
#         fileObj = file(cmdFile, 'w+')

#         if(projectName == 'flashloader'):
#             # Note: for KL82, must issue 'rnh' so that CPU will run, after reset flashloader will nerver run,
#             #       so KL82 flashloader project can't be tested by this script.
#             print >> fileObj, "r"   # Reset
#             print >> fileObj, "h"   # Halt
#             print >> fileObj, "loadfile %s" %(hexFile.replace('\\', '/'))   # Download image
#             print >> fileObj, "SetPC %s" %(PC)      # Set PC value
#             print >> fileObj, "wreg MSP, %s" %(SP)  # Set SP value
#             print >> fileObj, "wreg PSP, %s" %(SP)
#             print >> fileObj, "g"                   # go
#             print >> fileObj, "Sleep 5000"          # Wait 5000ms
#             print >> fileObj, "qc"                  # Quit 
           
#         else:   # For flash-resident bootloader and flashloader_loader
#             print >> fileObj, "r"   # Reset
#             print >> fileObj, "h"   # Halt
#             print >> fileObj, "loadfile %s" %(hexFile.replace('\\', '/'))   # Download image
#             '''
#             https://jira.sw.nxp.com/browse/KIBV-517: [KBOOT Automation] Bug Fix -- Targets with ROM inside will jump to ROM code during the run test for some test cases.

#             For the targets with ROM inside, here wait about 5s after reset to let ROM boot the app in flash, 
#             usually the app sets flash address 0x40d as 0x3D, which means boot from flash not from ROM.
#             '''
#             if(targetName == 'KL82Z7' or targetName == 'KL28Z7' or targetName == 'K80F25615' or targetName == 'K82F25615'):
#                 print >> fileObj, "rnh"                 # Reset not Halt
#                 print >> fileObj, "Sleep 6000"          # Wait 6000ms
#                 print >> fileObj, "r"                   # Reset
#                 print >> fileObj, "h"                   # Halt
#                 pass
#             else:
#                 pass

#             print >> fileObj, "SetPC %s" %(PC)      # Set PC value
#             print >> fileObj, "wreg MSP, %s" %(SP)  # Set SP value
#             print >> fileObj, "wreg PSP, %s" %(SP)                  # go
#             print >> fileObj, "g"                   # go
#             print >> fileObj, "Sleep 5000"          # Wait 5000ms
#             print >> fileObj, "qc"                  # Quit
           
#         fileObj.close() 
#         returncode, output = self.run_script(cmdFile)
#         logging.info('Flash Image:\n%s'%output) 
#         os.remove(cmdFile)


#     # @breif Start JLinkGDBServer.
#     def start_gdb_server(self):
#         gdbConnectionTimes = 2
#         for i in xrange(gdbConnectionTimes):
#             gdbServerListeningPort = str(random.randint(10000, 80000)) 
#             logFile = os.path.join(self._currentPath, 'startGDBServer_%s.txt'%gdbServerListeningPort)
#             fileObj = open(logFile, 'w+')
#             fileObj.truncate()
#             fileObj.close()    
#             if self._deviceName == None:
#                 cmdArgs = '"%s" -select usb=%s -if SWD -port %s -speed auto -singlerun >> %s 2>&1' %(
#                             self._jlinkGdbServerClExe,
#                             self._jlinkUsbId,
#                             gdbServerListeningPort,
#                             logFile)
#             else:
#                 cmdArgs = '"%s" -select usb=%s -if SWD -port %s -device %s -speed auto -singlerun >> %s 2>&1' %( 
#                             self._jlinkGdbServerClExe,
#                             self._jlinkUsbId,
#                             gdbServerListeningPort,
#                             self._deviceName,
#                             logFile)
        
#             logging.info('Start GDB Server...\n%s' %(cmdArgs))
#             p = subprocess.Popen(cmdArgs, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, shell=True)
#             pid = p.pid
#             time.sleep(2)
#             content = open(logFile,'r').read()
#             if 'Waiting for GDB connection...' in content:
#                 # It means GDB server started successfully, but the process will not stop running
#                 # until the gdb commands are executed sucessfully.
#                 # Here the logFile cannot be accessed as it is being used, should delete it when this process ends.
#                 logging.info('\n' + content)
#                 return (gdbServerListeningPort, pid) 

#             # while(p.poll() == None):
#             #     time.sleep(1)
#             #     content = open(logFile,'r').read()
#             #     if 'Waiting for GDB connection...' in content:
#             #         # It means GDB server started successfully, but the process will not stop running
#             #         # until the gdb commands are executed sucessfully.
#             #         # Here the logFile cannot be accessed as it is being used, should delete it when this process ends.
#             #         logging.info('\n' + content)
#             #         return gdbServerListeningPort            
#             # # logging.info(content)
#             # # The process is finished, the logFile can be deleted.
#             os.remove(logFile)
#         logging.info("-------------Failed to start the GDB server!-------------")
#         assert False
        
#     # # @brief Flash image by JLinkGDBServer. Note that the hexFile and binFile come from the same project.
#     # def flash_image(self, hexFile, binFile, targetName):
#     #     # Get SP and PC from the given bin file. SP: the first four bytes, PC: the second four bytes.
#     #     fileObj = file(binFile, 'rb')
#     #     data = fileObj.read(8)
#     #     fileObj.close()
#     #     SP = hex(ord(data[0]) | (ord(data[1]) << 8) | (ord(data[2]) << 16) | (ord(data[3]) << 24))
#     #     PC = hex(ord(data[4]) | (ord(data[5]) << 8) | (ord(data[6]) << 16) | (ord(data[7]) << 24))
#     #     # Start GDB Server
#     #     (gdbServerListeningPort, pid) = self.start_gdb_server()
#     #     cmdFile = os.path.join(self._currentPath, '%s_flash_image.init'%targetName)
#     #     fileObj = file(cmdFile, 'w+')
#     #     fileObj.write(r"set tcp connect-timeout 10" + "\n")
#     #     fileObj.write(r"set remotetimeout 10"  + "\n")
#     #     fileObj.write(r"target remote localhost:%s" %(gdbServerListeningPort) + "\n")
#     #     fileObj.write(r"monitor flash device = %s" %(self._deviceName) + "\n")
#     #     fileObj.write(r"monitor endian little" + "\n")
#     #     fileObj.write(r"monitor speed auto" + "\n") 
#     #     # For K82, need reset here
#     #     fileObj.write(r"monitor reset 0" + "\n")

#     #     fileObj.write(r"monitor waithalt 5000" + "\n")
#     #     fileObj.write(r'load "%s"' %(hexFile.replace('\\', '/')) + "\n")
#     #     # Set PC and SP values
#     #     fileObj.write(r"monitor reg SP = %s" %(SP) + "\n")
#     #     fileObj.write(r"monitor reg PC = %s" %(PC) + "\n") 
#     #     # Read PC and SP values
#     #     fileObj.write(r"monitor reg SP" + "\n")
#     #     fileObj.write(r"monitor reg PC" + "\n")
#     #     # For the flashloader_loader and flash-resident bootloader, reset the target here or not
#     #     # are both OK, but on the kl81/kl82, here must add the reset command.
#     #     if(targetName == 'KL82Z7'):        
#     #         fileObj.write(r"monitor reset 0" + "\n")
#     #     else:
#     #         fileObj.write(r"monitor go" + "\n")
        
        
#     #     # For kl81/kl82, when download the image to flash, then reset and go, PC will point to ROM, it's a strange issue.
#     #     # So here needs to delay more than 5s so than it will jump to the flash.
#     #     fileObj.write(r"monitor sleep 6000" + "\n")        
#     #     fileObj.write(r"q" + "\n")
#     #     fileObj.close()

#     #     cmd = '%s -x %s' %(self._gdbExe, cmdFile)
#     #     process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#     #     pid_2 = process.pid
#     #     output, error = process.communicate()
#     #     logging.info("\nFlash Image:\n%s\n%s"%(cmd, output))  
        
#     #     if(targetName == 'KL82Z7' or targetName == 'KL28Z7'):        
#     #         time.sleep(6)
#     #         self.reset()
#     #         time.sleep(3)
#     #     else:
#     #         pass

#     #     try:
#     #         os.system(os.getenv('SYSTEMROOT') + '/System32/taskkill' + ' /T /F /pid ' + str(pid))
#     #         os.system(os.getenv('SYSTEMROOT') + '/System32/taskkill' + ' /T /F /pid ' + str(pid_2))
#     #     except:
#     #         pass

    
#     # @brief Dump the binary memory from the specific device by JLink GDB server.
#     # Write contents of memory to a raw binary file
#     def dump_memory(self, address, bytes):
#         dumpMemoryFile = os.path.join(self._currentPath, 'dumpBinary_%s.bin' %(''.join(random.sample(string.ascii_letters, 10))))
#         # Start GDB Server
#         gdbServerListeningPort = self.start_gdb_server()
#         cmdFile = os.path.join(self._currentPath, 'dumpMemory_%s.init' %(''.join(random.sample(string.ascii_letters, 10))))
#         fileObj = file(cmdFile, 'w+')
#         print >> fileObj, "set tcp connect-timeout 10" 
#         print >> fileObj, "set remotetimeout 10"
#         print >> fileObj, "target remote localhost:%s" %(gdbServerListeningPort)
#         print >> fileObj, "monitor flash device = %s" %(self._deviceName)
#         print >> fileObj, "monitor endian little"
#         print >> fileObj, "monitor speed auto"
#         print >> fileObj, "dump binary memory %s 0x%x 0x%x" %(dumpMemoryFile, address, address + bytes)
#         print >> fileObj, "q"
#         fileObj.close()
        
#         cmd = '%s -x %s' %(self._gdbExe, cmdFile)
#         process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#         output, error = process.communicate()
#         logging.info('\nDump 0x%x bytes data from target address 0x%x:\n%s\n%s' %(bytes, address, cmd, output))
        
        
#         return dumpMemoryFile

#     # @brief Restore the binary file to the device memory.
#     # Restore the contents of the binary file to target memory.
#     def restore_memory(self, memoryAddress, binFile):
#         # Start GDB Server
#         gdbServerListeningPort = self.start_gdb_server()
#         cmdFile = os.path.join(self._currentPath, 'restoreMemory_%s.init' %(''.join(random.sample(string.ascii_letters, 10))))
#         fileObj = file(cmdFile, 'w+')
#         logging.info >> fileObj, "set tcp connect-timeout 10" 
#         logging.info >> fileObj, "set remotetimeout 10"
#         logging.info >> fileObj, "target remote localhost:%s" %(gdbServerListeningPort)
#         logging.info >> fileObj, "monitor flash device = %s" %(self._deviceName)
#         logging.info >> fileObj, "monitor endian little"
#         logging.info >> fileObj, "monitor speed auto"
#         logging.info >> fileObj, "restore %s binary 0x%x" %(binFile, memoryAddress)
#         logging.info >> fileObj, "monitor reset 0"
#         logging.info >> fileObj, "q"
#         fileObj.close()
        
#         cmd = '%s -x %s' %(self._gdbExe, cmdFile)
#         process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#         output, error = process.communicate()
#         logging.info('\nRestore the binary data to the memory address 0x%x:\n%s\n%s' %(memoryAddress, cmd, output))
        

    
 
# class ElfTool:
#     @staticmethod
#     def sparse_elf_info(elfFile):
#         readelf_exe = os.path.expandvars('%KDS_WORKBENCH%\\toolchain\\bin\\arm-none-eabi-readelf.exe')
#         logging.info('elfFile: %s'%elfFile)
#         cmd = '%s -l %s' %(readelf_exe, elfFile)
#         p = subprocess.Popen(cmd, 0, None, None, subprocess.PIPE, subprocess.PIPE, shell=True)
#         (sout, serr) = p.communicate()
#         # Find the Entry point
#         output_arr = sout.split('\n')
#         i = 1
#         for per_line in output_arr:
#             logging.info('Line %d: %s'%(i, per_line))
#             i = i + 1
#             if per_line.find('LOAD') != -1:
#                 vector_start = per_line.split()[3]
#                 sp = vector_start
#                 pc = hex(eval(sp) + 4)
#                 logging.info(sp, pc)
#                 return (sp, pc)
#         raise TypeError('\nFile Type Error: please provide the .elf or .out file.')


# if __name__ == "__main__":
#     test = JLink('600111626', 'Cortex-M33')
#     print test.enter_debug_session()
#     print test.write_register(0x40130180, 0x01)
#     # test.check_connection()

