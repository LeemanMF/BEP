#main file waarbij alle losse functies worden opgeroepen en uitgevoerd
#nog niet getest
import serial
from Data import data
from Controller import LQR_control
from Motoren import motor_drive
from Plot import real_time_plot
import time

duration = 100
start_time = time.time()
while time.time() - start_time < duration:
    theta,z,theta_dot,zdot = data()
    Fmotor1 = LQR_control(theta, theta_dot)
    print("F =", Fmotor1)
    speed = motor_drive(Fmotor1, theta_dot)
    print("Speed = ", speed)
    real_time_plot()

#Motor = serial.Serial('COM7',9600) #connectie met Arduino
#Motor.write(b'speed')