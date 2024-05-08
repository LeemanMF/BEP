#script met...
#in: arduino data
#out: y, ydot, z, zdot (hoek en hoeksnelheid in 2 vlakken)

import time
import serial #import van programma om arduino uit te lezen

arduinoData=serial.Serial('com7',115200) # juiste arduino selecteren
time.sleep(1)
while (True):   #zorgen dat python info blijft ophalen
    with arduinoData:
        while (arduinoData.inWaiting()==0): #combineert python en arduino op de arduino, voorkomt afsluiten
            pass
        dataPacket = arduinoData.readline() #uitlezen van data
        #dataPacket=str(dataPacket,'utf-8')
        dataPacket = dataPacket.decode('utf-8').strip() #data is vorm zetten zonder 'b en 'n/r
        #print(dataPacket)
        splitPacket=dataPacket.split(",") #losse variabelen selecteren
        #print(splitPacket)
        #print(type (splitPacket))
        #time.sleep(.2)
        y=float(splitPacket[0]) #los variabel oproepen als float
        z=float(splitPacket[1])
        ydot=float(splitPacket[2])
        zdot=float(splitPacket[3])
        print ("y=",y," z=",z," ydot=",ydot, "zdot=",zdot) # print variabelen
