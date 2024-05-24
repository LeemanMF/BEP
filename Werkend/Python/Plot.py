import matplotlib.pyplot as plt
import time

def init_real_time_plot():
    fig, ax = plt.subplots(3, 1)  # Add a third subplot for raw vs filtered data
    line_theta, = ax[0].plot([], [], 'r-', label='Filtered Theta')
    line_thetadot, = ax[1].plot([], [], 'b-', label='Filtered Theta Dot')
    line_raw_theta, = ax[2].plot([], [], 'g-', label='Raw Theta')  # Raw theta data
    line_filtered_theta, = ax[2].plot([], [], 'r-', label='Filtered Theta')  # Filtered theta data

    plott = []
    plottheta = []
    plotthetadot = []
    plotrawtheta = []
    plotfilteredtheta = []

    for a in ax:
        a.legend()

    return fig, ax, line_theta, line_thetadot, line_raw_theta, line_filtered_theta, plott, plottheta, plotthetadot, plotrawtheta, plotfilteredtheta

def update_real_time_plot(fig, ax, line_theta, line_thetadot, line_raw_theta, line_filtered_theta, plott, plottheta, plotthetadot, plotrawtheta, plotfilteredtheta, theta, theta_dot, raw_theta, filtered_theta):
    # Append new data
    plott.append(time.time())
    plottheta.append(theta)
    plotthetadot.append(theta_dot)
    plotrawtheta.append(raw_theta)
    plotfilteredtheta.append(filtered_theta)

    # Update data for the plot
    line_theta.set_data(plott, plottheta)
    line_thetadot.set_data(plott, plotthetadot)
    line_raw_theta.set_data(plott, plotrawtheta)
    line_filtered_theta.set_data(plott, plotfilteredtheta)
    
    for a in ax:
        a.relim()
        a.autoscale_view()

    plt.draw()
    plt.pause(0.01)
