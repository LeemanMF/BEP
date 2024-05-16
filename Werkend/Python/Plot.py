import numpy as np
import matplotlib.pyplot as plt
from Data import data
import time

def real_time_plot():
    #Maak lege lijst aan voor de plots
    plott = []
    plottheta = []

    #Interactieve grafiek
    plt.ion()
    ax = plt.subplot()
    line, = ax.plot(plott, plottheta)

    plt.xlabel('Tijd')
    plt.ylabel('Theta')
    plt.title('Real-Time Measured Theta')

    while True:
        new_t = time.time()
        theta, z, theta_dot, zdot = data()
        new_theta = theta

        plott.append(new_t)
        plottheta.append(new_theta)

        line.set_xdata(plott)
        line.set_ydata(plottheta)

        ax.relim()
        ax.autoscale_view()

        plt.draw
        plt.pause(0.1)
        break