import meshtastic
import meshtastic.serial_interface
import pyqrcode
import os

interface = meshtastic.serial_interface.SerialInterface()
ourNode = interface.getNode('^local')

setChannel = True  # Sets lora channel to the default for LongFast

regions_ch = {'US':20,
              'EU_433':4,
              'EU_868':1,
              'CN':36,
              'JP':20,
              'ANZ':20,
              'KR':12,
              'TW':16,
              'RU':2,
              'IN':4,
              'NZ_865':4,
              'TH':16,
              'LORA_24':6,
              'UA_433':6,
              'UA_868':2,
              'MY_433':4,
              'MY_919':16,
              'SG_923':4}

path = 'qrs' # Folder Name
prefix = 'private-primary-' # File prefix

try: # create a directory, if one doesn't exist
    os.mkdir(path)
except OSError as error:
    print(error)

for region, channel in regions_ch.items():
    ourNode.localConfig.lora.region = region
    if setChannel:
        ourNode.localConfig.lora.channel_num = channel
    url = interface.localNode.getURL(includeAll=True)
    qr = pyqrcode.create(url)
    qr.png('qrs/'+prefix+region+'.png', scale=8)
    print("File "+ prefix+region+" saved in directory: "+path)

interface.close()