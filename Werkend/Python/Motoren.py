#Functie met kracht uit de LQR functie erin en een setmotorspeed eruit. 
#De setmotorspeed moet gecheckt worden met de encoder en gecorrigeerd worden.
#Wellicht omschrijven naar Voltage outputs
#ToDO: Maximale kracht op touw inbouwen
straal_motor = 1.0 #cm 
ts_ratio = 0.2 #torque speed ratio

#Functie om de motor kracht te laten uitoefenen
def motor_control(Fmotor1):
    torque_needed = Fmotor1 / straal_motor
    if torque_needed > 0.2 : #kg/cm, als hoger dan de rated torque (maximale werktorque), zet gelijk aan rated torque
        torque_needed = 0.2 * straal_motor 
    force_motor_speed = ts_ratio * torque_needed 
    return force_motor_speed

#Functie om de motor zonder krachtuitoefening de load te laten volgen
def motor_follow(theta_dot): 
    follow_motor_speed = theta_dot / straal_motor
    return follow_motor_speed


#Beide functies samengevoegd om totale motorsnelheid te krijgen, motor control alleen aanroepen op een tijdstip. 
def motor_drive(Fmotor1, theta_dot):
    motor_speed = motor_control(Fmotor1) + motor_follow(theta_dot)
    return motor_speed

#Functie om draaisnelheid van de motor om te zetten naar motorcommmando voor arduino
