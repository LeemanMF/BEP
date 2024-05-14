#Functie met kracht uit de LQR functie erin en een setmotorspeed eruit. 
#De setmotorspeed moet gecheckt worden met de encoder en gecorrigeerd worden.
#Wellicht omschrijven naar Voltage outputs

#ToDO: Maximale kracht op touw inbouwen, failsafe inbouwen als motor sneller moet draaien dan hij kan
straal_motor = 1.0 #cm 
ts_ratio = 0.2 #torque speed ratio
no_load_speed = 160 #rpm zonder load
stall_torque = 0.8 #kg/cm

#Functie om de motor kracht te laten uitoefenen
def motor_control(Fmotor1):
    torque_needed = Fmotor1 / straal_motor
    if torque_needed > 0.2 : #kg/cm, als hoger dan de rated torque (maximale werktorque), zet gelijk aan rated torque
        torque_needed = 0.2 * straal_motor 
    force_motor_speed = no_load_speed - (no_load_speed * (1 - torque_needed / stall_torque)) 
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


#test
Fmotor1example = 0.001 #N
theta_dotexample = 5 #
print("Motor follow",motor_follow(theta_dotexample));
print("Motor kracht",motor_control(Fmotor1example));
print(motor_drive(Fmotor1example, theta_dotexample)); 
