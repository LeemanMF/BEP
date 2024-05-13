#main file waarbij alle losse functies worden opgeroepen en uitgevoerd
#nog niet getest

from Data import data
print(data())

from Controller import LQR_control
print(LQR_control())

from Motoren import motor_drive
print(motor_drive())
