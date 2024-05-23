import numpy as np
import matplotlib.pyplot as plt
from Data import data
import time

# def real_time_plot():
#     #Maak lege lijst aan voor de plots
#     plott = []
#     plottheta = []

#     #Interactieve grafiek
#     plt.ion()
#     ax = plt.subplot()
#     line, = ax.plot(plott, plottheta)

#     plt.xlabel('Tijd')
#     plt.ylabel('Theta')
#     plt.title('Real-Time Measured Theta')

#     while True:
#         new_t = time.time()
#         theta, z, theta_dot, zdot = data()
#         new_theta = theta

#         plott.append(new_t)
#         plottheta.append(new_theta)

#         line.set_xdata(plott)
#         line.set_ydata(plottheta)

#         ax.relim()
#         ax.autoscale_view()

#         plt.draw()
#         plt.pause(0.1)
#         break

import matplotlib.pyplot as plt
import time

def init_real_time_plot():
    # Create empty lists for the plots
    plott = []
    plottheta = []
    plotthetadot = []

    # Interactive plot
    plt.ion()
    fig, ax = plt.subplots()
    line_theta, = ax.plot(plott, plottheta, label='Theta', color='blue')
    line_thetadot, = ax.plot(plott, plotthetadot, label = 'Theta_dot', color='red')

    plt.xlabel('Tijd')
    plt.ylabel('Theta, Thetadot')
    plt.title('Real-Time Measured Theta')
    plt.legend()

    return fig, ax, line_theta, line_thetadot, plott, plottheta, plotthetadot


def update_real_time_plot(fig, ax, line_theta, line_thetadot, plott, plottheta, plotthetadot, connectie):
    new_t = time.time()
    theta, z, theta_dot, zdot = data(connectie)
    new_theta = theta
    new_thetadot = theta_dot

    plott.append(new_t)
    plottheta.append(new_theta)
    plotthetadot.append(new_thetadot)

    line_theta.set_xdata(plott)
    line_theta.set_ydata(plottheta)

    line_thetadot.set_xdata(plott)
    line_thetadot.set_ydata(plotthetadot)

    ax.relim()
    ax.autoscale_view()

    fig.canvas.draw()
    fig.canvas.flush_events()
