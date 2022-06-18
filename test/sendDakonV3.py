import time
import serial
import binascii
import urllib.request
from function import porovnej_crc
from function import cal_crc
from function import mess_for_send
print ("RS reading started...")

seru = serial.Serial('/dev/ttyS0', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS, timeout = 1)

while True:
        i = seru.readline()
        print (i)
        a = i.hex()
#        print(a)
        


        PARVALSTR = "45"
        CMDPAR = "028E"
        data = mess_for_send(CMDPAR,PARVALSTR)
        print (data)
        seru.write(data)
        print("sent: ",data)
        break
