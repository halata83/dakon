
import time
import serial
import binascii
import urllib.request

url_json = "http://192.168.1.107:1080/json.htm?type=command&param=udevice&idx="
url_json2 = "http://192.168.1.107:1080/json.htm?type=command&param=switchlight&idx="

print ("RS reading started...")

seru = serial.Serial('/dev/ttyS0', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS, timeout = 1)

while True:
        i = seru.readline()
        a = i.hex()
        print(a)
            
        if( a.find('1681',8,-8) > -1):
            tempOutsideActualHex =  a[a.find('1681',8,-8)+4:a.find('1681',8,-8)+8]
            tempOutsideActualDec  = int(tempOutsideActualHex,16)   
            print(" -----------  tempOutsideActualDec ---------------------")
            print(tempOutsideActualDec)
            if (tempOutsideActualDec/10 > -50 and tempOutsideActualDec/10 < 50):
                # use Domoticz JSON url to update
                cmd = url_json  + str(16) + "&nvalue=0&svalue=" + str(tempOutsideActualDec/10)       
                urllib.request.urlopen(cmd)
                print(cmd)
                print("-------------------------------------------------------")
                
        if( a.find('157e',8,-8) > -1):
            tempCoSetpHex =  a[a.find('157e',8,-8)+4:a.find('157e',8,-8)+8]
            tempCoSetpDec = int(tempCoSetpHex,16)
            print("------------------  tempCoSetpDec--------------------------")
            print(tempCoSetpDec)
            # use Domoticz JSON url to update
            cmd = url_json  + str(36) + "&nvalue=0&svalue=" + str(tempCoSetpDec)       
            urllib.request.urlopen(cmd)
            print(cmd)
            print("-------------------------------------------------------")
            
        if( a.find('157d',8,-8) > -1):
            tempCoActualHex =  a[a.find('157d',8,-8)+4:a.find('157d',8,-8)+8]
            tempCoActualDec = int(tempCoActualHex,16)
            print("-------------  tempCoActualDec --------------------------")
            print(tempCoActualDec)
            # use Domoticz JSON url to update
            cmd = url_json  + str(11) + "&nvalue=0&svalue=" + str(tempCoActualDec/10)       
            urllib.request.urlopen(cmd)
            print(cmd)
            print("-------------------------------------------------------")
            
        if( a.find('1616',8,-8) > -1):
            tempCwuSetpHex =  a[a.find('1616',8,-8)+4:a.find('1616',8,-8)+8]
            tempCwuSetpDec = int(tempCwuSetpHex,16)
            print("-------------- tempCwuSetpDec ----------------------------")
            print(tempCwuSetpDec)
            # use Domoticz JSON url to update
            cmd = url_json  + str(37) + "&nvalue=0&svalue=" + str(tempCwuSetpDec)       
            urllib.request.urlopen(cmd)
            print(cmd)
            print("-------------------------------------------------------")
            
        if( a.find('167f',8,-8) > -1):
            tempZaworuSetpHex =  a[a.find('167f',8,-8)+4:a.find('167f',8,-8)+8]
            tempZaworuSetpDec = int(tempZaworuSetpHex,16)
            print("-----------  tempCwuSetpDec ---------------------------")
            print(tempZaworuSetpDec)
            # use Domoticz JSON url to update
            cmd = url_json  + str(39) + "&nvalue=0&svalue=" + str(tempZaworuSetpDec)       
            urllib.request.urlopen(cmd)
            print(cmd)
            print("-------------------------------------------------------")
            
        if( a.find('166e',8,-8) > -1):
            tempCwuActualHex =  a[a.find('166e',8,-8)+4:a.find('166e',8,-8)+8]
            tempCwuActualDec = int(tempCwuActualHex,16)
            print("-----------  tempCwuActualDec -------------------------")
            print(tempCwuActualDec)
            # use Domoticz JSON url to update
            cmd = url_json  + str(12) + "&nvalue=0&svalue=" + str(tempCwuActualDec/10)       
            urllib.request.urlopen(cmd)
            print(cmd)
            print("-------------------------------------------------------")
            
        if( a.find('1614') >-1):
            tempZaworuActualHex =  a[a.find('1614')+4:a.find('1614')+8]
            tempZaworuActualDec = int(tempZaworuActualHex,16)
            print("----------  tempZaworuActualDec -----------------------")
            print(tempZaworuActualDec)
            # use Domoticz JSON url to update
            cmd = url_json  + str(13) + "&nvalue=0&svalue=" + str(tempZaworuActualDec/10)       
            urllib.request.urlopen(cmd)
            print(cmd)
            print("-------------------------------------------------------")
            
        if( a.find('16c1',8,-8) > -1):
            tempPowrotuActualHex =  a[a.find('16c1',8,-8)+4:a.find('16c1',8,-8)+8]
            tempPowrotuActualDec = int(tempPowrotuActualHex,16)
            print("---------  tempPowrotuActualDec -----------------------")
            print(tempPowrotuActualDec)
            # use Domoticz JSON url to update
            cmd = url_json  + str(14) + "&nvalue=0&svalue=" + str(tempPowrotuActualDec/10)       
            urllib.request.urlopen(cmd)
            print(cmd)
            print("-------------------------------------------------------")
            
        if( a.find('16f2',8,-8) > -1):
            poziomPaliwaActualHex =  a[a.find('16f2',8,-8)+4:a.find('16f2',8,-8)+8]
            poziomPaliwaActualDec = int(poziomPaliwaActualHex,16)
            print("---------  poziomPaliwaActualDec  ---------------------")
            print(poziomPaliwaActualDec)
             # use Domoticz JSON url to update
            cmd = url_json  + str(15) + "&nvalue=0&svalue=" + str(poziomPaliwaActualDec)       
            urllib.request.urlopen(cmd)
            print(cmd)
            print("-------------------------------------------------------")
            
        if( a.find('1588') > -1):
            wentHex =  a[a.find('1588')+4:a.find('1588')+8]
            wentDec = int(wentHex,16)
            print(" --------  wentDec ------------------------------------")
            print(wentDec)
            # use Domoticz JSON url to update
            if (wentDec == 1):
                cmd = url_json2  + str(30) + "&switchcmd=On"
            else:
                cmd = url_json2  + str(30) + "&switchcmd=Off"
            urllib.request.urlopen(cmd)
            print(cmd)
            print("-------------------------------------------------------")
            
        if( a.find('158b') > -1):
            pompaCwuHex =  a[a.find('158b')+4:a.find('158b')+8]
            pompaCwuDec = int(pompaCwuHex,16)
            print("---------  pompaCwuDec  -------------------------------")
            print(pompaCwuDec)
            # use Domoticz JSON url to update
            if (pompaCwuDec == 1):
                cmd = url_json2  + str(21) + "&switchcmd=On"
            else:
                cmd = url_json2  + str(21) + "&switchcmd=Off"
            urllib.request.urlopen(cmd)
            print(cmd)
            print("-------------------------------------------------------")
            
        if( a.find('1589') > -1):
            pompaCoHex =  a[a.find('1589')+4:a.find('1589')+8]
            pompaCoDec = int(pompaCoHex,16)
            print("---------  pompaCoDec  --------------------------------")
            print(pompaCoDec)
             # use Domoticz JSON url to update
            if (pompaCoDec == 1):
                cmd = url_json2  + str(18) + "&switchcmd=On"
            else:
                cmd = url_json2  + str(18) + "&switchcmd=Off"      
            urllib.request.urlopen(cmd)
            print(cmd)
            print("-------------------------------------------------------")
            
        if( a.find('1587') > -1):
            podajnikCoHex =  a[a.find('1587')+4:a.find('1587')+8]
            podajnikCoDec = int(podajnikCoHex,16)
            print("----------  podajnikCoDec  ----------------------------")
            print(podajnikCoDec)
             # use Domoticz JSON url to update
            if (podajnikCoDec == 1):
                cmd = url_json2  + str(29) + "&switchcmd=On"
            else:
                cmd = url_json2  + str(29) + "&switchcmd=Off"      
            urllib.request.urlopen(cmd)
            print(cmd)
            print("-------------------------------------------------------")
            
        if( a.find('159b',8,-8) > -1):
            wentHex =  a[a.find('159b',8,-8)+4:a.find('159b',8,-8)+8]
            wentDec = int(wentHex,16)
            print("---------  wentDec  -----------------------------------")
            print(wentDec)
             # use Domoticz JSON url to update
            cmd = url_json  + str(17) + "&nvalue=0&svalue=" + str(wentDec)       
            urllib.request.urlopen(cmd)
            print(cmd)
            print("-------------------------------------------------------")
                            
        if( a.find('15aa') > -1):
            pompaCyrHex =  a[a.find('15aa')+4:a.find('15aa')+8]
            pompaCyrDec = int(pompaCyrHex,16)
            print("---------  pompaCyrDec  -------------------------------")
            print(pompaCyrDec)
             # use Domoticz JSON url to update
            if (pompaCyrDec == 1):
                cmd = url_json2  + str(22) + "&switchcmd=On"
            else:
                cmd = url_json2  + str(22) + "&switchcmd=Off"     
            urllib.request.urlopen(cmd)
            print(cmd)
            print("-------------------------------------------------------")
                                           
        if( a.find('157c') > -1):
            statHex =  a[a.find('157c')+4:a.find('157c')+8]
            print("--------  statHex  ------------------------------------")
            print(statHex)
            if (statHex == '0002'): 
                cmd = url_json  + str(23) + "&nvalue=0&svalue=" + "Praca"     
                urllib.request.urlopen(cmd)
                print(cmd)
            elif(statHex == '0082'):
                cmd = url_json  + str(23) + "&nvalue=0&svalue=" + "Nadzor"     
                urllib.request.urlopen(cmd)
                print(cmd)
            elif(statHex == '0050'):
                cmd = url_json  + str(23) + "&nvalue=0&svalue=" + "Podtrzymanie"     
                urllib.request.urlopen(cmd)
                print(cmd)
            elif(statHex == '0052'):
                cmd = url_json  + str(23) + "&nvalue=0&svalue=" + "Nadzor"     
                urllib.request.urlopen(cmd)
                print(cmd)
            print("-------------------------------------------------------")     
        if( a.find('15cd') > -1):
            statPompHex =  a[a.find('15cd')+4:a.find('15cd')+8]
            statPompDec = int(statPompHex,16)
            print("-------  statPompDec ----------------------------------")
            print(statPompDec)
            if (statPompDec == 3): 
                cmd = url_json  + str(38) + "&nvalue=0&svalue=" + "Letni"     
                urllib.request.urlopen(cmd)
                print(cmd)
            elif(statPompDec == 2):
                cmd = url_json  + str(38) + "&nvalue=0&svalue=" + "PompyRownolegle"     
                urllib.request.urlopen(cmd)
                print(cmd)
            elif(statPompDec == 1):
                cmd = url_json  + str(38) + "&nvalue=0&svalue=" + "PriorytetBojlera"     
                urllib.request.urlopen(cmd)
                print(cmd)
            elif(statPompDec == 0):
                cmd = url_json  + str(38) + "&nvalue=0&svalue=" + "OgrzewanieDomu"     
                urllib.request.urlopen(cmd)
                print(cmd)
            print("-------------------------------------------------------")     
        if( a.find('15ac',8,-8) > -1):
            otwarcieZaworuHex =  a[a.find('15ac',8,-8)+4:a.find('15ac',8,-8)+8]
            otwarcieZaworuDec = int(otwarcieZaworuHex,16)
            print("-------  OtwarciezavoruDec  ---------------------------")
            print(OtwarciezavoruDec)
             # use Domoticz JSON url to update
            cmd = url_json  + str(24) + "&nvalue=0&svalue=" + str(otwarcieZaworuDec)       
            urllib.request.urlopen(cmd)
            print(cmd)
            print("-------------------------------------------------------")
            
        if( a.find('16f1') > -1):
            poziomPaliwa2ActualHex =  a[a.find('16f1')+4:a.find('16f1')+8]
            poziomPaliwa2ActualDec = int(poziomPaliwa2ActualHex,16)
            print("------  poziomPaliwa2ActualDec ------------------------")
            print(poziomPaliwa2ActualDec)
             # use Domoticz JSON url to update
            cmd = url_json  + str(25) + "&nvalue=0&svalue=" + str(poziomPaliwa2ActualDec/512)       
            urllib.request.urlopen(cmd)
            print(cmd)
            print("-------------------------------------------------------")
            
                        
        if( a.find('0370',8,-8) > -1):
            tempPodajnikaHex =  a[a.find('0370',8,-8)+4:a.find('0370',8,-8)+8]
            tempPodajnikaDec = int(tempPodajnikaHex,16)
            print("-----  tempPodajnikaDec  ------------------------------")
            print(tempPodajnikaDec)
             # use Domoticz JSON url to update
            cmd = url_json  + str(26) + "&nvalue=0&svalue=" + str(tempPodajnikaDec/10)       
            urllib.request.urlopen(cmd)
            print(cmd)
            print("-------------------------------------------------------")
            
        #if( a.find('16f8') > -1):
          #  tempPodajnika2Hex =  a[a.find('16f8')+4:a.find('16f8')+8]
           # tempPodajnika2Dec = int(tempPodajnika2Hex,16)
             # use Domoticz JSON url to update
           # cmd = url_json  + str(27) + "&nvalue=0&svalue=" + str(tempPodajnika2Dec/10)       
          #  urllib.request.urlopen(cmd)
            
        if( a.find('0370',8,-8) > -1):
            tempPodajnika3Hex =  a[a.find('0370',8,-8)+4:a.find('0370',8,-8)+8]
            tempPodajnika3Dec = int(tempPodajnika3Hex,16)
            print("------  tempPodajnika3Dec  ----------------------------")
            print(tempPodajnika3Dec)
             # use Domoticz JSON url to update
            cmd = url_json  + str(28) + "&nvalue=0&svalue=" + str(tempPodajnika3Dec/10)       
            urllib.request.urlopen(cmd)
            print(cmd)
            print("-------------------------------------------------------")
