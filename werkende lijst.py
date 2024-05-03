# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
import serial
import re
arduinoData=serial.Serial('com7',115200)
time.sleep(1)
while (True):
    while (arduinoData.inWaiting()==0):
        pass
    dataPacket = arduinoData.readline() #reply
    dataPacket=str(dataPacket,'utf-8')
    print(dataPacket)
    splitPacket=dataPacket.split(",")
    print(type (splitPacket))
    time.sleep(10)
    #X=float(splitPacket[0])
    #Y=float(splitPacket[1])
    #Z=float(splitPacket[2])
    #print ("X=",X," Y=",Y," Z=",Z)
    