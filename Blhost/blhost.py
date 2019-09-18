import os
import subprocess
import json
import yaml
import sys

class Blhost():
    """docstring for Blhost"""
    def __init__(self, blhostPath = '', peripheral = 'usb', uartPort = '', jsonFormat = True):
        self.jsonFormat = jsonFormat
        self.blhostTool = blhostPath
        self.timeout = ''
        self.buspalDevice = ''
        if(peripheral == 'uart'):
            self.comport = uartPort
        if(peripheral == 'spi' or peripheral == 'i2c'):
            # self.buspal = True
            self.comport = uartPort
            self.buspalDevice = peripheral


    def __buildCmd(self, *arg):

        if self.jsonFormat:
            cmd = [self.blhostTool, '-p', self.comport, '-j', '--']
        else:
            cmd = [self.blhostTool, '-p', self.comport, '--']

        if self.timeout:
            cmd.insert(cmd.index(self.comport)+1 , '-t 50000')

        if self.buspalDevice:
            cmd.insert(cmd.index(self.comport) + 1 , '-b ' + self.buspalDevice)


        for x in arg:
            cmd.append(x)

        cmd = [str(x) for x in cmd]
        cmdStr = ' '.join(cmd)
        return cmdStr

    def __executeCmd(self,cmd):
        print cmd
        process = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
        out = process.communicate()[0]
        err = process.stderr
        print  out
        # print err
        try:
            status, results = self.__parse(out)
        except ValueError:
            return cmd + '\n' + 'No response' + '\n'
        else:
            print status, results
            # if status == '0 (0x0) Success.':
            # return cmd + '\n' + out + '\n', status
            return cmd + '\n' + out + '\n', status



        # return cmd + '\n' + out + '\n'

    def __parse(self, data):
        if self.jsonFormat:
            jsonData = json.loads(data)
            return jsonData['status']['description'], jsonData['status']['value']
        else:
            return data

    def get_property(self, commandTag):
        cmdStr = self.__buildCmd('get-property', commandTag)
        return self.__executeCmd(cmdStr)

    def write_memoty(self, addr, file):
        if isinstance(addr, int):
            addr = hex(addr).split('L')[0]
      
        cmdStr = self.__buildCmd('write-memory',addr, file)
        return self.__executeCmd(cmdStr)

    def erase_region(self, startAddr, size):
        self.timeout = True
        if isinstance(startAddr, (int, long)):
            startAddr = hex(startAddr).split('L')[0]
        if isinstance(size, (int, long)):
            size = hex(size).split('L')[0]

        cmdStr = self.__buildCmd('flash-erase-region',startAddr, size)
        return self.__executeCmd(cmdStr)

    def configure_memory(self, option, addr):
        if isinstance(option, (int, long)):
            option = hex(option).split('L')[0]
        if isinstance(addr, (int, long)):
            addr = hex(addr).split('L')[0]

        cmdStr = self.__buildCmd('configure-memory', option, addr)
        return self.__executeCmd(cmdStr)

    def fill_memory(self, addr, size, data):
        if isinstance(addr, (int, long)):
            addr = hex(addr).split('L')[0]
        if isinstance(size, (int, long)):
            size = hex(size).split('L')[0]
        if isinstance(data, (int, long)):
            data = hex(data).split('L')[0]

        cmdStr = self.__buildCmd('fill-memory', addr, size, data)
        return self.__executeCmd(cmdStr)

    def efuse_program_once(self, addr, data):
        if isinstance(addr, (int, long)):
            addr = hex(addr).split('L')[0]
        if isinstance(data, (int, long)):
            data = hex(data).split('L')[0]

        cmdStr = self.__buildCmd('efuse-program-once', addr, data)
        return self.__executeCmd(cmdStr)


    def key_porvisioning(self):
        cmdStr = self.__buildCmd('key-provisioning', 'enroll')
        return self.__executeCmd(cmdStr)

    def set_user_key(self, keyfile):
        cmdStr = self.__buildCmd('key-provisioning','set_user_key', 11, keyfile)
        return self.__executeCmd(cmdStr)

    def read_key_store(self, keystoreReadFile):
        cmdStr = self.__buildCmd('key-provisioning','read_key_store', keystoreReadFile)
        return self.__executeCmd(cmdStr)





if __name__ == '__main__':

    blhostPath = 'C:/Users/nxa28190/Desktop/LPC_generate_image/Tools/blhost.exe'
    uart = 'com10'
    imageFile = r'C:\Users\nxa28190\Desktop\LPC_generate_image\Material\InputImage\led_ram_0x1c000.bin'
    keyFile = r'C:\Users\nxa28190\Desktop\LPC_generate_image\Material\AESkey\userkey.bin'

    keystoreReadFile = r'C:\Users\nxa28190\Desktop\LPC_generate_image\Material\AESkey\key_store_user.bin'

    bl = Blhost( blhostPath = blhostPath, peripheral = 'uart', uartPort = uart, jsonFormat = 'False')


    output, status = bl.fill_memory(0x1c000, 0x4, 0xf000000f)
    print status



    # bl.configure_memory(0x9, 0x1c000)
    # bl.erase_region(0x08001000, 0x10000)
    # bl.write_memoty(0x08001000, imageFile)
    # bl.key_porvisioning()
    # bl.set_user_key(keyFile)
    # bl.read_key_store(keystoreReadFile)

    # bl = Blhost( blhostPath = blhostPath, peripheral = 'spi', uartPort = uart, jsonFormat = 'False')
    # bl.get_property(7)













        
