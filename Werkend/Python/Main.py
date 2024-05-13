#main file waarbij alle losse functies worden opgeroepen en uitgevoerd
#nog niet getest

from data import data
print(data())

from controller import LQR_control
print(LQR_control())

from Motoren import motor_control
print(motor_control())
