import meshtastic
import meshtastic.serial_interface
import pyqrcode
import os

interface = meshtastic.serial_interface.SerialInterface()
ourNode = interface.getNode('^local')
regions = ['US','EU_433','EU_868','CN','JP','ANZ','KR','TW','RU','IN','NZ_865','TH','LORA_24','UA_433','UA_868']
#regions = ['US','UNSET']

path = 'qrs' # Folder Name
prefix = 'all-channels-' # File prefix

try: # create a directory, if one doesn't exist
    os.mkdir(path)
except OSError as error:
    print(error)

for region in regions:
    ourNode.localConfig.lora.region = region
    url = interface.localNode.getURL(includeAll=True)
    qr = pyqrcode.create(url)
    qr.png('qrs/'+prefix+region+'.png', scale=8)
    print("File "+ prefix+region+" saved in directory: "+path)

interface.close()
