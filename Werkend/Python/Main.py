#main file waarbij alle losse functies worden opgeroepen en uitgevoerd
#nog niet getest
#import serial
#from Data import data
#from Controller import LQR_control
#from Motoren import motor_drive
#from Plot import real_time_plot
#import time


#duration = 100
#start_time = time.time()
#while time.time() - start_time < duration:
#    theta,z,theta_dot,zdot = data()
#    Fmotor1 = LQR_control(theta, theta_dot)
#    print("F =", Fmotor1, flush=True)
#    speed = motor_drive(Fmotor1, theta_dot)
#    print("Speed = ", speed, flush=True)
#    #real_time_plot()

#Motor = serial.Serial('COM7',9600) #connectie met Arduino
#Motor.write(b'speed')

#main file waarbij alle losse functies worden opgeroepen en uitgevoerd
#nog niet getest wel gecheckt door bert
import serial
from Data import data
from Controller import LQR_control
from Motoren import motor_drive
import time

def check_port_availability(port):
    try:
        ser = serial.Serial(port)
        ser.close()
        return True
    except serial.SerialException as e:
        print(f"Port {port} is not available: {e}")
        return False

# Replace 'COM3' with the port you want to check
port_name = 'COM6'
available = check_port_availability(port_name)
print(f"Port {port_name} is available: {available}")


Leonardo = serial.Serial('COM6',230400) #connectie met Arduino
time.sleep(1)
duration = 100
start_time = time.time()
while time.time() - start_time < duration:
    print(Leonardo.readline().decode())
    theta,z,theta_dot,zdot = data(Leonardo)
    Fmotor1 = LQR_control(theta, theta_dot)
    pps = motor_drive(Fmotor1, theta_dot)
    print(pps)
    Leonardo.write(f"{pps}\n".encode())
    
