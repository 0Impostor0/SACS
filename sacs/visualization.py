import matplotlib.pyplot as plt

def plot_results(time_data, theta_data, torque_data):
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))


    axs[0].plot(time_data, theta_data, label='Theta (rad)')
    axs[0].set_title('Theta vs Time')
    axs[0].set_xlabel('Time (s)')
    axs[0].set_ylabel('Theta (rad)')
    axs[0].legend()
    axs[0].grid()


    axs[1].plot(time_data, torque_data, label='Torque (Nm)', color='orange')
    axs[1].set_title('Torque vs Time')
    axs[1].set_xlabel('Time (s)')
    axs[1].set_ylabel('Torque (Nm)')
    axs[1].legend()
    axs[1].grid()

    plt.tight_layout()
    plt.show()