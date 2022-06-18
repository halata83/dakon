
import time
import serial
import binascii
import urllib.request

print ("RS reading started...")

seru = serial.Serial('/dev/ttyS0', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS, timeout = 1)

while True:
        i = seru.readline()
        print (i)
        a = i.hex()
        print(a)
        values = bytearray() #02 26 FF F4 02 8E 00 2D 02 18 DC 57
        values.append(2)
        values.append(38)
        values.append(255)
        values.append(244)
        values.append(2)
        values.append(69)
        values.append(0)
        values.append(3)
        values.append(2)
        values.append(24)
        values.append(55)
        values.append(23)
        seru.write(values)
        print("sent")
        print (values)
        break
