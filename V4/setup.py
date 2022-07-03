from ast import Continue
import os
import time
import serial
import binascii
import urllib.request as ur
import urllib.parse as par
import json
import subprocess
import math
import configparser
from datetime import datetime
from function import *
from dict import *
from os.path import exists
from sys import exit
PocetZarizeni = 0
NewDevice = []
dirname = os.path.dirname(__file__)
setupfile = os.path.join(dirname, 'setup.dat')
configfile = os.path.join(dirname, 'config.ini') 
print (configfile)
config = configparser.ConfigParser()
config.read(configfile)
DomoticzUrl = config["DEFAULT"]["domoticzurl"]
useDZhttp = str2bool(config["DEFAULT"]["useDomoticzHttpApi"])
yesorno = input("spustenim se vymaže existujic soubor setup.dat a vytvoří se novy. Chcete Pokracovat? A/N: ")
if (any(yesorno.lower() == f for f in["no", "n","ne"])):
    print ("ok, končime ")
    exit()
if (exists(setupfile)):
    os.remove(setupfile)
    print ("mažu soubor setup.dat")
if (exists(configfile) != True):
    print ("nenešel jsem config.ini")
    exit()
print ("prijimam data po RS...")

#seru = serial.Serial('/dev/ttyS0', baudrate=9600,
#                    parity=serial.PARITY_NONE,
#                    stopbits=serial.STOPBITS_ONE,
#                    bytesize=serial.EIGHTBITS, timeout = 1)

while True:
    print ("Hledám nová zařízeni...")
    #i = seru.readline()
    #a = i.hex()
    a = "0226FFFA169E572D169F4B28157C0021157D00D2157E0032166E02941616002D158B00001681F83015CD00021620022516210002158900001587000015880000159B000001F60000028E0000029800000299000002450000157F00011610000002FC000001F9000003110000031200000288000002183A22"
    a = a.upper()
    crc_cajk = porovnej_crc(a)
    if ( crc_cajk != True ):
        #print ("spatne crc")
        continue
    y = 0
    for x in range(len(a)):
        if a[y:y+4] in parametry:
            parametr, popis, typ, dzidx, sendTo, dzload = LoadDataFromString(a, y, parametry)
            
            
            
            if parametr in NewDevice:
                #print ("zarizeni už je v seznamu")
                #print (NewDevice)
                PocetZarizeni += 1 
            else:
                if (parametr != "0226" and parametr != "0218") :
                    if (useDZhttp) and (sendTo == "True"):
                        dzidx = createDomoticzDevice(DomoticzUrl,popis,typ)
                    if parametr in ("157E","1616", "15CD"):
                        dzload = "True"
                    device = str(parametr) + "," + str(popis) + "," + str(typ) + "," + str(dzidx) + "," + str(sendTo) + "," + str(dzload) + "\n"
                    print ("pridavam zarizeni:", device)
                    NewDevice.append(parametr)
                    writeFile(setupfile,str(device))
        else:
            print(a[y:y+4], "-- nebyl nalezen")
        y = y + 8
        if (y == len(a)):
            break
    if (PocetZarizeni >= 500):
        break    
print ("hotovo")
#print (NewDevice)

