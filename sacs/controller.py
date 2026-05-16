class PDController:
    def __init__(self, kp: float, kd: float):
        self.kp = kp
        self.kd = kd
        self._prev_error = 0.0

    def compute_torque(self, error: float, dt: float) -> float:
        derivative = (error - self._prev_error) / dt
        self._prev_error = error
        return self.kp * error + self.kd * derivative

    def reset(self):
        self._prev_error = 0.0