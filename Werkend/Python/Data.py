import serial
import time
from Filter import butter_lowpass_filter
import numpy as np

# def initialize_data_buffers(buffer_size):
# return np.zeros(buffer_size), np.zeros(buffer_size), np.zeros(buffer_size), np.zeros(buffer_size)
#Leonardo = serial.Serial('COM9',230400)

def data():
    arduinoData = serial.Serial('COM9', 230400)
    while arduinoData.inWaiting() == 0:
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
theta, z, theta_dot, z_dot = data()     
print(theta, z, theta_dot, z_dot)
