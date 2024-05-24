import serial
import time
from Filter import butter_lowpass_filter
import numpy as np

def initialize_data_buffers(buffer_size):
    return np.zeros(buffer_size), np.zeros(buffer_size), np.zeros(buffer_size), np.zeros(buffer_size)

def data(connectie, theta_buffer, z_buffer, theta_dot_buffer, z_dot_buffer, cutoff_freq, fs, order=5):
    arduinoData = connectie
    while arduinoData.inWaiting() == 0:
        pass
    data_packet = arduinoData.readline().decode('utf-8').strip()
    split_packet = data_packet.split(",")
    
    # Extract raw sensor data
    raw_theta = float(split_packet[0])
    raw_z = float(split_packet[1])
    raw_theta_dot = float(split_packet[2])
    raw_z_dot = float(split_packet[3])
    
    # Append raw data to buffers
    theta_buffer = np.append(theta_buffer[1:], raw_theta)
    z_buffer = np.append(z_buffer[1:], raw_z)
    theta_dot_buffer = np.append(theta_dot_buffer[1:], raw_theta_dot)
    z_dot_buffer = np.append(z_dot_buffer[1:], raw_z_dot)
    
    # Apply low-pass filter to the raw sensor data
    filtered_theta = butter_lowpass_filter(theta_buffer, cutoff_freq, fs, order)[-1]
    filtered_z = butter_lowpass_filter(z_buffer, cutoff_freq, fs, order)[-1]
    filtered_theta_dot = butter_lowpass_filter(theta_dot_buffer, cutoff_freq, fs, order)[-1]
    filtered_z_dot = butter_lowpass_filter(z_dot_buffer, cutoff_freq, fs, order)[-1]
    
    return raw_theta, raw_z, raw_theta_dot, raw_z_dot, filtered_theta, filtered_z, filtered_theta_dot, filtered_z_dot
