# What controller.py gives to simulation.py
PDController.compute_torque(error: float, dt: float) -> float

# What dynamics.py gives to simulation.py  
RigidBody.apply_torque(torque: float, dt: float) -> tuple[float, float]
# returns (theta, omega) — angle and angular velocity

# What simulation.py gives to gui/app.py
Simulation.step() -> dict  {"time": float, "theta": float, "omega": float, "torque": float}
