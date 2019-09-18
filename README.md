# rt600_tool
a tool which can support generate image/ configure shadow, fuses/ download image for RT600


## environment setup
- install python 2.7 
- install python lib as following commands 
  - pip install wxpython
  - pip install pyinstaller
  - pip install pylink

- install wxFormBuilder_v3.9.0.exe
  - for more information please refer: https://github.com/wxFormBuilder/wxFormBuilder
  
## usage
- generate .exe by using following command  
  - enter into LOC_generate_image folder and execute pyinstaller RT600Tool.spec
  - usage for pyinstaller : http://legendtkl.com/2015/11/06/pyinstaller/
  
- tool usage  
  - generate image  
  ![image generation](https://github.com/ComingGod/rt600_tool/blob/master/Image/1.bmp)
  - generate keystore  
  ![generate keystore](https://github.com/ComingGod/rt600_tool/blob/master/Image/2.bmp)
  - configure fuse/shadow and dowanload image  
  ![config target and download image](https://github.com/ComingGod/rt600_tool/blob/master/Image/3.bmp)

  
  
