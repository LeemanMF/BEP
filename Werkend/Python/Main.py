#main file waarbij alle losse functies worden opgeroepen en uitgevoerd
#nog niet getest
import serial
from Data import data
from Controller import LQR_control
from Motoren import motor_drive


theta,z,theta_dot,zdot = data()
Fmotor1 = LQR_control(theta, theta_dot)
speed = motor_drive(Fmotor1, theta_dot)

Motor = serial.Serial('COM7',9600) #connectie met Arduino
Motor.write(b'speed')