import os
import subprocess
# filePath = os.path.abspath(os.getcwd()).replace('//', '/')

class GenerateImage():
	def __init__(self, **arg):

		self.elftosbTool = arg['elftosbTool']
		self.jsonFile = arg['jsonFile']

	def generate_json_file(self, arg):
		jsonFileContent = '''{
	"family": "rt6xx",
	"inputImageFile": "%s",
	"imageLinkAddress": "%s",
	"imageLinkAdressFromImage": false,
	"outputImageExecutionTarget": "%s",
	"outputImageAuthenticationType": "%s",
	"deviceKeySource": "%s",
	"outputImageEncryptionKeyFile": "%s", 
	"enableTrustZone": %s,
	"trustZonePresetFile": "%s",
	"enableHwUserModeKeys": false, 
	"useKeyStore": %s,
	"keyStoreFile": "%s",
	"rootCertificate0File": "%s",
	"rootCertificate1File": "%s",
	"rootCertificate2File": "%s",
	"rootCertificate3File": "%s",
	"mainCertChainId": %s,
	"mainCertPrivateKeyFile": "%s",
	"masterBootOutputFile": "image.bin"
}''' %(arg['inputImage'], arg['linkAddr'], arg['executeTarget'], arg['imageAuthType'], \
    arg['keySource'], arg['imageEncKeyFile'], arg['enableTrustZone'], arg['presetFile'], \
	arg['useKeystore'], arg['keyStoreFile'], arg['certFile0'], arg['certFile1'], \
	arg['certFile2'], arg['certFile3'], arg['certChainID'], arg['privateKeyFile'] \

)

		with open(self.jsonFile, 'w') as file:
			file.write(jsonFileContent)
	
 
	def generate_image(self):
		elftosb = self.elftosbTool
		JsonFile = self.jsonFile

		cmd = [self.elftosbTool, '-J', self.jsonFile, '-f', 'rt6xx']
		cmdStr = ' '.join(cmd)

		process = subprocess.Popen(cmdStr, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
		out = process.communicate()[0]
		err = process.stderr

		print out
		return out


if __name__ == '__main__':
	elftosbTool = 'C:/Users/nxa28190/Desktop/LPC_generate_image/Tools/elftosb.exe'
	imageFile = 'C:/Users/nxa28190/Desktop/LPC_generate_image/GenImage/led_ram_0x1c000.bin'

	# arg = {'useKeystore': 'true', 'imageEncKeyFile': u'', 'presetFile': u'', 'imageAuthType': u'Signed', 'executeTarget': u'RAM', 'enableTrustZone': 'flase', 'certChainID': u'0', 'inputImage': u'D:/Git_repo/rom_validation/Test/Generate_image/input_image/led_ram_0x1c000.bin', 'privateKeyFile': u'D:/Git_repo/rom_validation/Test/Generate_image/keys_and_certs/rotk0_cert0_2048.pem', 'keyStoreFile': u'D:/Git_repo/rom_validation/Test/Generate_image/AES_key/key_store_user.bin', 'keySource': u'Key Store', 'linkAddr': u'0x1c000', 'certFile1': u'D:/Git_repo/rom_validation/Test/Generate_image/keys_and_certs/rotk1_cert0_2048_noca.der.crt', 'certFile0': u'D:/Git_repo/rom_validation/Test/Generate_image/keys_and_certs/rotk0_cert0_2048_noca.der.crt', 'certFile3': u'D:/Git_repo/rom_validation/Test/Generate_image/keys_and_certs/rotk3_cert0_2048_noca.der.crt', 'certFile2': u'D:/Git_repo/rom_validation/Test/Generate_image/keys_and_certs/rotk2_cert0_2048_noca.der.crt'}
	arg = {'useKeystore': 'true', 'imageEncKeyFile': u'', 'presetFile': u'', 'imageAuthType': u'Signed', 'executeTarget': u'RAM', 'enableTrustZone': 'flase', 'certChainID': u'0', 'inputImage': u'D:/Git_repo/rom_validation/Test/Generate_image/input_image/led_ram_0x1c000.bin', 'privateKeyFile': u'D:/Git_repo/rom_validation/Test/Generate_image/keys_and_certs/rotk0_cert0_2048.pem', 'keyStoreFile': u'D:/Git_repo/rom_validation/Test/Generate_image/AES_key/key_store_user.bin', 'keySource': u'Key Store', 'linkAddr': u'0x1c000', 'certFile1': u'D:/Git_repo/rom_validation/Test/Generate_image/keys_and_certs/rotk1_cert0_2048_noca.der.crt', 'certFile0': u'D:/Git_repo/rom_validation/Test/Generate_image/keys_and_certs/rotk0_cert0_2048_noca.der.crt', 'certFile3': u'D:/Git_repo/rom_validation/Test/Generate_image/keys_and_certs/rotk3_cert0_2048_noca.der.crt', 'certFile2': u'D:/Git_repo/rom_validation/Test/Generate_image/keys_and_certs/rotk2_cert0_2048_noca.der.crt'}


	genImage = GenerateImage(elftosbTool = elftosbTool, jsonFile = 'test.json')
	# genImage.generate_json_file(arg)
	genImage.generate_image()








