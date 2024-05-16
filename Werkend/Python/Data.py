#script met...
#in: arduino data
#out: y, ydot, z, zdot (hoek en hoeksnelheid in 2 vlakken)

import time
import serial #import van programma om arduino uit te lezen

def data():
    arduinoData=serial.Serial('COM3',115200) # juiste arduino selecteren
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
            theta=float(splitPacket[0]) #los variabel oproepen als float
            z=float(splitPacket[1])
            theta_dot=float(splitPacket[2])
            zdot=float(splitPacket[3])
            print ("theta=",theta," theta_dot=",theta_dot) # print variabelen
        return theta,z,theta_dot,zdot

