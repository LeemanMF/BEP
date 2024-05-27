#Functie met kracht uit de LQR functie erin en een setmotorspeed eruit. 
#De setmotorspeed moet gecheckt worden met de encoder en gecorrigeerd worden.
#Wellicht omschrijven naar Voltage outputs

#ToDO: Maximale kracht op touw inbouwen, failsafe inbouwen als motor sneller moet draaien dan hij kan
#Check: Wellicht moet motor_drive soms + en soms - elkaar!
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d


#Motorkarakteristiek uit Excel !! AANPASSEN 2 MOTOREN !!
excel_naam = r"C:\Users\jikke\Downloads\Motoren.xlsx"
motorA_naam = 'MotorA'
df = pd.read_excel(excel_naam, motorA_naam, usecols=['PWM', 'RPM'])

pwm_values = df['PWM'].values
rpm_values = df['RPM'].values

interp_func = interp1d(rpm_values, pwm_values, kind='nearest', fill_value='extrapolate')

#PWM corresponderend met RPM
def find_motor_pwm(rpm):
    return int(interp_func(rpm))

#Variabelen
straal_motor = 0.01 #m 
ts_ratio = 0.2 #torque speed ratio
no_load_speed = 160 * 2 * np.pi / 60 #rad/s zonder load
stall_torque = 0.8 * 9.81 * 0.01 #N/m
rated_torque = 0.2 * 9.81 * 0.01 #N/m
lengte_pendulum = 0.5 #in meter

#Functie om de motor kracht te laten uitoefenen
def motor_control(Fmotor1):
    torque_needed = Fmotor1 / straal_motor
    if torque_needed > rated_torque : #N/m, als hoger dan de rated torque (maximale werktorque), zet gelijk aan rated torque
        torque_needed = rated_torque 
    force_motor_speed =  (no_load_speed - (no_load_speed * (1 - torque_needed / stall_torque))) * 60 / (2*np.pi) 
    return float(force_motor_speed) #RPM

#Functie om de motor zonder krachtuitoefening de load te laten volgen
def motor_follow(theta, theta_dot): 
    if abs(theta) < 5 and abs(theta_dot) < 0.2:
        theta_dot = 0
        follow_motor_speed = 0
    else :
        follow_motor_speed = (theta_dot) / straal_motor #Lengte pendulum is vgm niet nodig gezien de sensor op de massa hangt
    return float(follow_motor_speed * 60 / (2 * np.pi)) #RPM

#Beide functies samengevoegd om totale motorsnelheid te krijgen, motor control alleen aanroepen op een tijdstip. 
def motor_drive(Fmotor1, theta, theta_dot):
    motor_speed = find_motor_pwm((motor_follow(theta, theta_dot))) #+ motor_control(Fmotor1)))
    return motor_speed