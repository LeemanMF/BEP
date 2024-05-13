#main file waarbij alle losse functies worden opgeroepen en uitgevoerd
#nog niet getest

from Data import data
from Controller import LQR_control
from Motoren import motor_drive


theta,z,theta_dot,zdot = data()
Fmotor1 = LQR_control(theta, theta_dot)
speed = motor_drive(Fmotor1, theta_dot)
