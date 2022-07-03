# dakonDomoticz
Program pro Čteni dat z kotle dakon FB2 automat s jednotkou ST-480zPID a posílani vybranych dat do Domoticz.
vycházel jsem z tohohle fora: https://www.elektroda.pl/rtvforum/topic2689981-270.html a upravil jsem program jednoho z clenu.


Používáni:
   - stahnout tohle uloziste
   - nainstalovat python3, pip, 
   - nainstalovat crcmod, serial, knihovny pro python
   - pripojit kotel pres RS linku k pc
   - pokud chcete upravte dict.py 3 mistne cisla znamenaji idx pro domoticz. nebudou se muset zadávat pozdeji v setup.dat
   - struktura dict.py je: {"rs parametr": "popis,typ,idx,posilat do domoticz"}
                           - popis je popis jake mame zarizeni
                           - typ: temp, stav, podle toho se zpracovavaji data
                           - idx: idx v domoticz
                           - posilat do domoticz True/False Ano/Ne
   - spustit setup.py projede prijimana data a uloži všechna objevena zarizeni do setup.dat
   - struktura setup.dat je: parametr,popis,typ, posilat do domoticz, posilat do kotle
                            - parametr: rs parametr z kotle
                            - popis je popis jake mame zarizeni
                            - typ: temp, stav, podle toho se zpracovavaji data
                            - idx: idx v domoticz
                            - posilat do domoticz True/False Ano/Ne
                            - posilat do kotle True/False - paramtry umoznujici ovladani kotle
   
   - v ServiceDakon.py upravime promenou dzurl na sdresu na ktere nam bezi domoticz
   - spustime ServiceDakon.py. Pokud program najde setup.dat nacte dostupna zarízeni, overi dostupnost domoticz a zacne cist data z domoticz, posila do kotle
   -  a prijima data po RS lince a posilat do domoticz


# TODO  
       - dodelat schema zapojeni
       - mozna podpora MQTT
       - config.dat
