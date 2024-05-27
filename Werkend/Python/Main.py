import serial
from Data import data, initialize_data_buffers
from Controller import LQR_control
from Motoren import motor_drive
import time
from Plot import update_real_time_plot 
from Plot import init_real_time_plot
import matplotlib.pyplot as plt

def check_port_availability(port):
    try:
        ser = serial.Serial(port)
        ser.close()
        return True
    except serial.SerialException as e:
        print(f"Port {port} is not available: {e}")
        return False

# Replace 'COM3' with the port you want to check
port_name = 'COM9'
available = check_port_availability(port_name)
print(f"Port {port_name} is available: {available}")

# if available:
#     cutoff_freq = 10
#     fs = 100
#     order = 5
def plot():
    Leonardo = serial.Serial('COM9',230400) #connectie met Arduino
    fig, ax, line_theta, line_thetadot, plott, plottheta, plotthetadot = init_real_time_plot()

    time.sleep(1)
    duration = 100
    start_time = time.time()
    while time.time() - start_time < duration:
        print(Leonardo.readline().decode())
        theta,z,theta_dot,zdot = data(Leonardo)
        Fmotor1 = LQR_control(theta, theta_dot)
        pps = motor_drive(Fmotor1, theta, theta_dot)
        print(pps)
        Leonardo.write(f"{pps}\n".encode())
        #update the plot
        update_real_time_plot(line_theta, line_thetadot, plott, plottheta, plotthetadot, Leonardo)
        plt.pause(0.1)
    plt.show(block=True)

print("Finished")
Leonardo.write(f"{0}\n".encode())
    # Leonardo = serial.Serial(port_name, 230400)  # Connect to Arduino
    # fig, ax, line_theta, line_thetadot, line_raw_theta, line_filtered_theta, plott, plottheta, plotthetadot, plotrawtheta, plotfilteredtheta = init_real_time_plot()
    # time.sleep(1)

#     # Initialize buffers for data
#     # buffer_size = 50
#     # theta_buffer, z_buffer, theta_dot_buffer, z_dot_buffer = initialize_data_buffers(buffer_size)

#     duration = 50
#     start_time = time.time()
#     while time.time() - start_time < duration:
#         print(Leonardo.readline().decode())
#         raw_theta, raw_z, raw_theta_dot, raw_z_dot, filtered_theta, filtered_z, filtered_theta_dot, filtered_z_dot = data(Leonardo, theta_buffer, z_buffer, theta_dot_buffer, z_dot_buffer, cutoff_freq, fs, order)
        
#         Fmotor1 = LQR_control(filtered_theta, filtered_theta_dot)
#         pps = motor_drive(Fmotor1, filtered_theta, filtered_theta_dot)
#         print(pps)
#         Leonardo.write(f"{pps}\n".encode())
        
#         # Update the plot
#         update_real_time_plot(fig, ax, line_theta, line_thetadot, line_raw_theta, line_filtered_theta, plott, plottheta, plotthetadot, plotrawtheta, plotfilteredtheta, filtered_theta, filtered_theta_dot, raw_theta, filtered_theta)
#         time.sleep(0.1)
    
#     print("Finished")
#     Leonardo.write(f"{0}\n".encode())
# else:
#     print("Port not available. Please check the port connection.")
