import os
import sys
import serial.tools.list_ports
import json
import tempfile
import urllib

API_URL = "https://api.github.com/repos/arendst/Sonoff-Tasmota/releases"

def download():
    temp = tempfile.NamedTemporaryFile(suffix='.sonoff-tasmota-firmare.bin')
    #get api data and parse it
    response = urllib.urlopen(API_URL)
    data = json.loads(response.read())
    tag_name = data[0]['tag_name']
    body = data[0]['body']
    download_url = data[0]['assets'][0]['browser_download_url']
    print "Downloading Sonoff-Tasmota firmware version", tag_name
    print body
    #download file
    print "\nDownloading to temporary file", temp.name
    response = urllib.urlopen(download_url)
    temp.write(response.read())
    temp.flush()
    #get size of the downloaded file
    filesize=os.path.getsize(temp.name)
    filesize_given = data[0]['assets'][0]['size']
    #filesize verification
    if (filesize == filesize_given):
        print("Download successful")
    else:
        sys.exit("Error: The size of the downloaded file does not match")
    return temp

#user input
print("Please connect your device now")
print("Available Ports:")
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print p

port = raw_input("Which port do you want to use?\n")

if not any(port in p for p in ports):
    sys.exit("Error: Invalid port name, please try again.")

device = raw_input("Which device are you using? Type 0 for touch or 4CH and 1 for the others\n")

firmware_file = download()

# clear flash
err_erase = os.system("esptool.py --port " + port + " erase_flash")
print(err_erase)

#Process Error
if(err_erase != 0):
    sys.exit("Error while erasing. Check your connection.")

#Wait to reconnect
raw_input("Reconnect then press enter\n")

#Select device
if(device == "0"):
    #Flash with command for 4CH and Touch
    err_write = os.system("esptool.py --port " + port + " write_flash -fm dout -fs detect 0x0 " + firmware_file.name)
elif(device == "1"):
    #Flash with command for all others
    err_write = os.system("esptool.py --port " + port + " write_flash -fm dio -fs detect 0x0 " + firmware_file.name)

#Process Error
if(err_write != 0):
    sys.exit("Error while writing. Check your connection.")

print("Successful")
