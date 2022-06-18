from posixpath import split
import time
import serial
import binascii
import urllib.request
import os
import urllib.request as ur
import urllib.parse as par
import json
import subprocess
import math
from datetime import datetime
from function import *
from tridy import *
from dict import *

zarizeni = []
dzurl = "http://192.168.1.107:1080/"
start_time = time.time()
last_time = start_time
tsend = 5
dzpass = "username=bHVrYXM==&password=QWRtaW5hODMz="
print ("RS reading started...")

seru = serial.Serial('/dev/ttyS0', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS, timeout = 1)
if os.path.isfile(r"setup.dat"):
    print ("setup.dat existuje, načítam zařizeni..")
    dev = loadSetupFile("setup.dat")
    dev = dev.split("\n")
    for x in range(len(dev) -1 ):
        tmp = dev[x].split(",")
        stavy = device(tmp[1],tmp[2],tmp[0],dzurl) 
        stavy.send = tmp[4]
        stavy.idx = tmp[3]
        stavy.value_load_on_dz = tmp[5]
        zarizeni.append(stavy)
    print ("hotovo")
    
else:
    print("Setup.dat nebyl nalezen, spuste prosim setup.py v adresaři: ", os.getcwd())
    exit()



while True:
        now = time.time()
        akt_time = now
        i = seru.readline()
        a = i.hex()
        print (a)
#---- otestuju dostupnost domoticz pokud neni pokracuju ve smyccse ----
        dzonline = dz_online(dzurl)
        print (dzonline)
        if (dzonline == False):
           continue
        for i in zarizeni:
            if (i.value_load_on_dz == "True"):
                if (i.type == "temp"):
                    valu = load_dz_data(dzurl+"json.htm?type=devices&rid="+str(i.idx),"SetPoint")
                    print (valu)
                if (i.type == "stav"):
                    valu = load_dz_data(dzurl+"json.htm?type=devices&rid="+str(i.idx),"Level")
                    print (valu)


        #a = "0226FFFA169E572D169F4B28157C0021157D00D2157E0032166E02941616002D158B00001681F83015CD00021620022516210002158900001587000015880000159B000001F60000028E0000029800000299000002450000157F00011610000002FC000001F9000003110000031200000288000002183A22"
        #a = a.upper()
        #a.strip()
        #print(a)
        #print (len(a))
        crc_cajk = porovnej_crc(a)
        if ( crc_cajk != True ):
             print ("spatne crc")
             continue

        y = 0
        for x in range(len(a)):
            parametr = a[y:y+4]
            data = a[y+4:y+8]
            #dataDec = int(a[y+4:y+8],16)
            upravData(zarizeni,data,parametr)
            y = y + 8
            if (y >= len(a)):
                break
        #zobrazData(zarizeni)
        posliDataPriZmene(zarizeni)
        #last_time = posli_data_5m(akt_time,last_time,tsend,zarizeni)
        #time.sleep(1)
        
