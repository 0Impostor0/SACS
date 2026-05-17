from sacs.visualization import plot_results
from sacs.simulation import run_mock_simulation

def main():
    time_data, theta_data, torque_data = run_mock_simulation()
    plot_results(time_data, theta_data, torque_data)

if __name__ == "__main__":
    main()