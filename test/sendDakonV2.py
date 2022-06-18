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
        PARVALSTR = "55"
        PARVALDEC = int(PARVALSTR)
        PARVALBYT = PARVALDEC.to_bytes(2,'big')
        STX = "0226"
        ETX = "0218"
        FOR = "FFF4"
        CMDPAR = "028E"
        PARVAL = PARVALBYT.hex()
        PARVAL = PARVAL.upper()
        #PARVAL = "0032"
        CRC = ""
        message = STX + FOR + CMDPAR + PARVAL + ETX + CRC
        print ("message: ", message)
        CRC = cal_crc(message)
        print ("CRC: ", CRC)
        data = message + CRC
        print ("data: ", data)
        data = bytes.fromhex(data)
        print (data)
        seru.write(data)
        print("sent: ",data)
        break
