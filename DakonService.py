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
# v3.1
zarizeni = []
dzurl = "http://192.168.1.107:1080/"
start_time = time.time()
last_time = start_time
tsend = 300
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
        a = a.upper()
#---- otestuju dostupnost domoticz pokud neni pokracuju ve smyccse ----
        dzonline = dz_online(dzurl)
        if (dzonline == False):
           continue
#nactu data z domoticz a poslu do kotle
        for i in zarizeni:
            if (i.value_load_on_dz == "True"):
                if (i.type == "temp"):
                    i.value = load_dz_data(dzurl+"json.htm?type=devices&rid="+str(i.idx),"SetPoint")
                    i.mess_for_dz = mess_for_send(i.para,i.value)
                    if (i.LastValue != i.value):
                        i.LastValue = i.value
                        print ("odesilam data TV do kotle:", i.value)
                        seru.write(i.mess_for_dz)
                if (i.type == "stav"):
                    i.value = load_dz_data(dzurl+"json.htm?type=devices&rid="+str(i.idx),"Level")
                    i.mess_for_dz = mess_for_send(i.para,i.value)
                    if (i.LastValue != i.value):
                        i.LastValue = i.value
                        print ("odesilam data TV do kotle:", i.value)
                        seru.write(i.mess_for_dz)

# overim crc prijatych dat
        crc_cajk = porovnej_crc(a)
        if ( crc_cajk != True ):
             #print ("spatne crc")
             continue
#nactu a upravim data z kotle
        y = 0
        for x in range(len(a)):
            parametr = a[y:y+4]
            data = a[y+4:y+8]
            upravData(zarizeni,data,parametr)
            y = y + 8
            if (y >= len(a)):
                break
        zobrazData(zarizeni)
        posliDataPriZmene(zarizeni)
        last_time = posli_data_5m(akt_time,last_time,tsend,zarizeni)
        
