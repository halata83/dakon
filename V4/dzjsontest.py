from function import *
import configparser
import os
parametr = "Z"
if parametr in ("Y","S","K","L" ):
    print (parametr)
dirname = os.path.dirname(__file__)
configfile = os.path.join(dirname, 'config.ini') 
print (configfile)
config = configparser.ConfigParser()
config.read(configfile)
#domoticz = "http://192.168.1.107:1080/"
domoticz = "http://127.0.0.1:1080/"
DomoticzUrl = config["DEFAULT"]["domoticzurl"]
useDZhttp = str2bool(config["DEFAULT"]["useDomoticzHttpApi"])
#HWIdx = searchHWIdx(domoticz)
#LastIdx = LastIdxInDomoticz(domoticz)
#print (LastIdx)
ifidx = searchIdx(domoticz,639)
#createDomoticzDevice(domoticz,"DKM teplota","temp")
idx = createDomoticzDevice(domoticz,"DKM podavac","selswitch")