import triforcetools
from time import sleep
from sys import argv

if len(argv) < 3:
    print "Usage: python ./upload.py ip_address path_to_rom"
    exit()

netdimm_ip = argv[1]
rompath = argv[2]

print "Trying to connect to NetDIMM on "+netdimm_ip+"..."
while True:
    try:
        triforcetools.connect(netdimm_ip, 10703)
    except:
        pass
    
    sleep(1)

print "Uploading "+rompath+"..."
triforcetools.HOST_SetMode(0, 1)
triforcetools.SECURITY_SetKeycode("\x00" * 8)
triforcetools.DIMM_UploadFile(rompath)
triforcetools.HOST_Restart()
triforcetools.TIME_SetLimit(10*60*1000)
triforcetools.disconnect()

print "All done"
