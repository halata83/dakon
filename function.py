from logging import exception
from tridy import *

def porovnej_crc(input):
   import crcmod
   import crcmod.predefined
   if ( input == ""):
      return
   if ( input == " "):
      return
   # zkratim rezetec o konec vysilani a crc
   remotecrc = input[len(input)-4:len(input)]
   input2 =  input.split("0218")
   input =input[0:len(input)-8]
   STX = bytes.fromhex('0226')
   ETX = bytes.fromhex('0218')
   data = bytes.fromhex(input)
   message = data 
   crc16 = crcmod.predefined.Crc('crc-16-mcrf4xx')
   crc16.update(message)
   calcrc = crc16.hexdigest()
   if ( int(remotecrc,16) == int(calcrc,16)):
         return True
   else: 
         return False


def cal_crc(hexdata):
   import crcmod
   import crcmod.predefined
   if ( hexdata == ""):
      return
   if ( hexdata == " "):
      return
   # zkratim rezetec o konec vysilani a crc
   STX = bytes.fromhex('0226')
   ETX = bytes.fromhex('0218')
   tempdata = hexdata.split("0218")
   hexdata = tempdata[0]
   data = bytes.fromhex(hexdata)
   message = data
   crc16 = crcmod.predefined.Crc('crc-16-mcrf4xx')
   crc16.update(message)
   calcrc = crc16.hexdigest()
   #print ("calcrc: ",calcrc)
   return calcrc


def mess_for_send(CMDPAR,VALPAR):
        PARVALDEC = int(VALPAR)
        PARVALBYT = PARVALDEC.to_bytes(2,'big')
        STX = "0226"
        ETX = "0218"
        FOR = "FFF4"
        PARVAL = PARVALBYT.hex()
        PARVAL = PARVAL.upper()
        CRC = ""
        message = STX + FOR + CMDPAR + PARVAL + ETX + CRC
        CRC = cal_crc(message)
        data = message + CRC
        data = bytes.fromhex(data)
        return data

def load_dz_data(urlcmd,parametr):
         import urllib.request as ur
         import urllib.parse as par
         import json
         html = ur.urlopen(urlcmd).read()
         dzdata = json.loads(html.decode('utf-8'))
        # print ("dzdata: ", dzdata)
         resultData = dzdata["result"][0][parametr]
         if (parametr == "SetPoint"):
            resultData = resultData.split(".")
            resultData =resultData[0]
         if (parametr == "Level"):
            if (resultData == 0):
               resultData = 3
            if (resultData == 10):
               resultData = 2
            if (resultData == 20):
               resultData = 1
            if (resultData == 30):
               resultData = 0

        # print ("TV temp:",resultData)
         return resultData

def send_data_to_domoticz(cmdurl):
           import urllib.request as ur
           import urllib.parse as par
           cmd = cmdurl
           print ("posilam data do domoticz", cmd)
           try:
                page = ur.urlopen(cmd)
           except ur.HTTPError as err:
                if err.code == 404:
                    print ("Page not found!")
                elif err.code == 403:
                    print ("Access denied!")
                else:
                    print("Neco se pokazilo! Error code:", err.code)
           except ur.URLError as err:
                  print ("chyba v pristupu k Domoticz", err.reason)
                  return

def LoadDataFromString(streamdata, pozice,seznam):
   #nactu zarizeni z dat z kotle
   _para = streamdata[pozice:pozice+4]
   dt = seznam[streamdata[pozice:pozice+4]]
   dt = dt.split(",")
   _pop = dt[0]
   _typ = dt[1]
   _idx = dt[2]
   _sndTo = dt[3]
   _dzload = ""
   return (_para,_pop,_typ,_idx,_sndTo,_dzload)

#def (streamdata, pozice):
   #nactu zarizeni z dat z kotle
#   _para = streamdata[pozice:pozice+4]
#   dt = seznam[streamdata[pozice:pozice+4]]
#   dt = dt.split(",")
#   _pop = dt[0]
#   _typ = dt[1]
#   _idx = dt[2]
#   _sndTo = dt[3]
#   return (_para,_pop,_typ,_idx,_sndTo)

def writeFile(filepatch,data):
   f = open(filepatch, "a")
   f.write(data)
   f.close()

def loadSetupFile(filepatch):
   try: 
      f = open(filepatch,"r")
   except:
      print("soubor:",filepatch,"nelze otevrit")
      exit()
   return f.read()

def zobrazData(odkud):
  for i in odkud:
      fi = i.dzCmdUrl()
      val = str(i.value)
      lastval = str(i.LastValue)
      print (i.para,"-value-",val.ljust(7),"-Last Value-",lastval.ljust(7),"-", i.popis,)

def posliDataPriZmene(co):
   for i in co:
      if (i.send == "True"):
         if (i.LastValue != i.value):
            tmpdata = i.dzCmdUrl()
            #print ("posilam data:", tmpdata)
            send_data_to_domoticz(tmpdata)
            i.LastValue = i.value

def upravData(odkud,datahex,hexpara):
   for i in odkud:
      if (i.para == hexpara):
         if (i.para == "157C"):
            data_ven = int(datahex,16)
         elif (i.para == "15A7"):
            if (datahex == "0016"):
               data_ven = "ST-730zPID / ST-755 zPid / ST-450 STALMARK? bez PID? / ST-500"
            elif (datahex == "0007"):
               data_ven = "AG LUX (bez PID) / K1PRv4PZ / ST-755 / K1PRv2"
            elif (datahex == "0013"):
               data_ven = "ST-450zPID"
            elif (datahex == "0015"):
               data_ven = "ST-480"
            elif (datahex == "0009"):
               data_ven = "ST-37rs"
            elif (datahex == "0008"):
               data_ven = "ST-709"
            elif (datahex == "0020"):
               data_ven = "ST-402"
            elif (datahex == "002C"):
               data_ven = "ST?"
            elif (datahex == "0005"):
               data_ven = "ST-48"
            elif (datahex == "0006"):
               data_ven = "TECH / AG LUX"
            elif (datahex == "000A"):
               data_ven = "TECH i3"
         elif (i.para == "159B"):
            data_ven = int(datahex,16)   
         elif (i.para == "16F8" or i.para == "15B7" or i.para == "157D" or i.para == "166E") :
            dataDec = int(datahex,16)
            data_ven = dataDec/10
         elif (i.type != "stav"):
            data_ven = int(datahex,16)
         else:
            data_ven = int(datahex,16)
         i.value = data_ven
         #return ()
         #print (i.para,"-",i.popis,"-",i.value,"-",i.send,"-",i.LastValue,"-", i.idx)

def posli_data_5m(akt_time,last_send_time,time_send,co):
   time_diff = int(akt_time) - int(last_send_time)
   if (time_diff >= time_send):
      for i in co:
         if (i.send == "True"):
            tmpdata = i.dzCmdUrl()
            print ("posilam data:", tmpdata)
            #send_data_to_domoticz(tmpdata)
            i.LastValue = i.value
      last_send_time = akt_time
   return last_send_time

def dz_online(dzurl):
   import urllib.request as ur
   dzonline = True
   try:
      page = ur.urlopen(dzurl+"json.htm?username=bHVrYXM==&password=QWRtaW5hODMz=")
   except ur.HTTPError as err:
      if err.code == 404:
         print("stranka nenalezena!")
         dzonline = False
      elif err.code == 403:
         print("pristup odepren!")
         dzonline = False
      elif err.code == 401:
         print("neopravneny pristup!")
         dzonline = False
      else:
         print("Neco je spatne! Error code: ", err.code)
         dzonline = False
   except ur.URLError as err:
      print("Domoticz neni dostupny", err.reason)
      dzonline = False
   return dzonline
      
        
