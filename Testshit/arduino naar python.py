# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
import serial

arduinoData=serial.Serial('com7',115200)
time.sleep(1)
while (True):
    with arduinoData:
        while (arduinoData.inWaiting()==0):
            pass
        dataPacket = arduinoData.readline() #reply
        #dataPacket=str(dataPacket,'utf-8')
        dataPacket = dataPacket.decode('utf-8').strip()
        #print(dataPacket)
        splitPacket=dataPacket.split(",")
        #print(splitPacket)
        #print(type (splitPacket))
        #time.sleep(.2)
        y=float(splitPacket[0])
        z=float(splitPacket[1])
        ydot=float(splitPacket[2])
        zdot=float(splitPacket[3])
        print ("y=",y," z=",z," ydot=",ydot, "zdot=",zdot)
       