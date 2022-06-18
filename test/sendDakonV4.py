import time
import serial
import binascii
import urllib.request as ur
import urllib.parse as par
import json
import subprocess
import math
from function import porovnej_crc
from function import cal_crc
from function import mess_for_send
from function import load_dz_data
dzurl = "http://192.168.1.107:1080/"
url_json = dzurl + "json.htm?type=command&param=udevice&idx="
url_json2 = dzurl + "json.htm?type=command&param=switchlight&idx="
print (dzurl)
print (url_json)
print (url_json2)
sent = 0
lastTV = 0
lastTUV = 0
lastRezCer = ""

# ----- domoticz idx ------
setTVidx = 627
actTVidx = 171
setTUVidx = 628
actTUVidx = 172
ventStatIdx = 629
ventOtidx = 633
cerpTVidx = 630
cerTUVidx = 631
podavacidx = 632
cerpStatidx = 639
procPaliva = 637
casPaliva = 638
tempPodavacidx = 174
tempSpalinidx = 636
statKotle = 635
#---------------------------
print ("prijimam data po RS...")

seru = serial.Serial('/dev/ttyS0', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS, timeout = 1)

while True:
        i = seru.readline()
#        print (i)
        a = i.hex()
#        print(a)
#---- otestuju dostupnost domoticz pokud neni pokracuju ve smyccse ----
        try:
           page = ur.urlopen(dzurl+"json.htm?")
        except ur.HTTPError as err:
           if err.code == 404:
               print("stranka nenalezena!")
           elif err.code == 403:
               print("pristup odepren!")
           else:
               print("Neco je spatne! Error code: ", err.code)
        except ur.URLError as err:
            print("Domoticz neni dostupny", err.reason)
            continue
#---- nactu data z domoticz --------------------------------------------
        TVsetTemp = load_dz_data(dzurl+'json.htm?type=devices&rid='+str(setTVidx),"SetPoint")
#        print (TVsetTemp)
        TUVsetTemp = load_dz_data(dzurl+'json.htm?type=devices&rid='+str(setTUVidx),"SetPoint")
#        print (TUVsetTemp)
        CerpStat = load_dz_data(dzurl+'json.htm?type=devices&rid='+str(cerpStatidx),"Level")
#        print (CerpStat)
# vytvorim zprávy ------------------------------------------------------
        CMDPARTUV = "028E"
        CMDPARTV = "01F6"
        CMDPARCerpStat = "0245"
        dataTUV = mess_for_send(CMDPARTUV,TUVsetTemp)
        dataTV = mess_for_send(CMDPARTV,TVsetTemp)
        dataCerp = mess_for_send(CMDPARCerpStat,CerpStat)
#        print (dataTUV)
#        print (dataTV)
#        print (dataCerp)
#        print (lastTV, TVsetTemp)
#        print (lastTUV, TUVsetTemp)
#        print (lastRezCer,CerpStat)
        if (lastTV != TVsetTemp):
            lastTV = TVsetTemp
            print ("odesilam data TV do kotle:", dataTV)
            seru.write(dataTV)
            #time.sleep(0.5)
        if (lastTUV != TUVsetTemp):
            lastTUV = TUVsetTemp
            print ("odesilam data TUV do kotle:", dataTUV)
            seru.write(dataTV)
            #time.sleep(0.5)
        if (lastRezCer != CerpStat):
            lastRezCer = CerpStat
            print ("odesilam data cerp do kotle:", dataCerp)
            seru.write(dataCerp)
            #time.sleep(0.5)
        #seru.write(data)
        #print("sent: ",data)
        #break
