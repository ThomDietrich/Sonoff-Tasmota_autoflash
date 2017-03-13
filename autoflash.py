import pip
import os
import sys
import serial.tools.list_ports

def install(package):
    pip.main(['install', package])

def ports():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print p


#user input
print("Please connect your device now")
print("Aviable Ports:")
ports()

port=raw_input("Which port do you want to use?\n")
device= raw_input("Which device are you using? Type 0 for touch or 4CH and 1 for the others\n")
filepath=raw_input("Enter the filepath of the firmwarefile\n(Please be aware that only ASCII letters are allowed) \n")

#install esptools
install("esptool")

# clear flash
err_erase=os.system("esptool.py --port "+port+" erase_flash")
print(err_erase)

#Process Error
if(err_erase !=0):
    print("Error while erasing. Check your connection.")
    sys.exit()


#Wait to reconnect (I'm not sure if it's ESPtools oder my usb to serial converter,
#but after erasing the flash, I cannot find the device, so you have to reconnect it
raw_input("Reconnect then press enter\n")

#Select device
if(device == "0"):
#Flash with command for 4CH and Touch
    err_write=os.system("esptool.py --port "+port+" write_flash -fm dout -fs detect 0x0 "+filepath)
elif(device == "1"):
#Flash with command for all others
    err_write=os.system("esptool.py --port "+port+" write_flash -fm dio -fs detect 0x0 "+filepath)

#Process Error
if(err_write !=0):
    print("Error while writing. Check your connection.")
    sys.exit()

print("Successful")
#
