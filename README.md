# SACS: Satellite Attitude Control System

SACS is a Python-based simulation environment designed to model and visualize a 3D satellite attitude Determination and Control System (ADCS). The project implements a lightweight dynamic simulation coupled with a Proportional-Derivative (PD) controller to manage satellite attitude.

---

# Project Structure

```plaintext
SACS/
│
├── src/
│   ├── gui/
│   │   ├── __init__.py
│   │   └── app.py                # Graphical interface entry point
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── pd_control.py         # Contains PDController logic
│   │   ├── visualization.py      # Real-time PyOpenGL rendering engine
│   │   ├── simulation.py         # Rigid-body satellite dynamics
│   │   └── attitude.py           # Quaternion math engine
│   │
│   ├── docs/
│   │   └── architecture.md       # Theoretical & technical documentation
│   │
│   ├── tests/
│   │   └── test_controller.py    # Unit tests for verification
│   │
│   └── utils/
│       ├── __init__.py
│       ├── math.py               # Physics utility pack
│       └── requirements.txt      # Project dependencies
│
└── README.md
```

---

# Features

- **PD Control Loop:** Dedicated PDController class computing torque adjustments based on orientation error.

- **Dynamic Simulation:** Tracks time-series data for attitude (θ), angular velocity (ω), and control effort (torque).

- **Data Visualization:** Dual-plot outputs via matplotlib showing Theta vs Time and Torque vs Time alongside real-time PyOpenGL rendering.

- **Modular Design:** Complete decoupling between controller physics, hardware simulation, and GUI layers.

---

# Mathematical Overview

The controller uses standard Proportional-Derivative feedback to determine the necessary torque output:

\[
u(t) = -K_p \, e(t) + K_d \frac{de(t)}{dt}
\]

Where:

- \( e(t) = \theta_{current} - \theta_{desired} \)
- \( \frac{de(t)}{dt} = \omega \)

---

# Installation & Setup

## Prerequisites

Make sure you have Python 3.8+ installed on your system.

---

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SACS.git
cd SACS
```

---

## 2. Install Dependencies

Install the required application libraries listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

Alternatively, using pip:

```bash
pip install matplotlib numpy PyOpenGL pygame
```

---

# Usage

To execute the mock simulation environment and view the performance plots, run the top-level launcher:

```bash
python main.py
```

---

# Future Improvements

- Quaternion-based 6DOF simulation
- Kalman filtering for sensor fusion
- Reaction wheel actuator modeling
- Star tracker emulation
- Real telemetry logging support
- GPU-accelerated visualization

---

# License

This project is licensed under the MIT License.

---

