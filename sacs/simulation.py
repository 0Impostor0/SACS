from .controller import PDController

def run_mock_simulation():

    controller = PDController(kp=2.0, kd=0.5)

    time_history = []
    theta_history = []
    torque_history = []
    dt = 0.01

    theta = 0.0
    target_theta = 1.0
    current_time = 0.0

    for i in range(100):
        error = target_theta - theta
        torque = controller.compute_torque(error, dt)

    
        theta += torque * dt 

        time_history.append(current_time)
        theta_history.append(theta)
        torque_history.append(torque)

        current_time += dt

    return time_history, theta_history, torque_history