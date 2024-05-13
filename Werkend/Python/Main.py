#main file waarbij alle losse functies worden opgeroepen en uitgevoerd
#nog niet getest

from data import data
from controller import LQR_control
from Motoren import motor_control


theta,z,theta_dot,zdot = data()
Fmotor1 = LQR_control(theta, theta_dot)
speed = motor_control(Fmotor1)
