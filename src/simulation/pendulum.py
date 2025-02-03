from typing import Tuple
from math import sin, cos

class Pendulum:
    def __init__(
        self,
        origin: Tuple[int, int],
        length: float,
        angle: float,
        gravity: float = 9.81,
    ) -> None:
        self.origin: Tuple[int, int] = origin
        self.length: float = length
        self.angle: float = angle
        self.gravity: float = gravity
        
        self.angular_velocity: float = 0
        self.angular_acceleration: float = 0
        self.damping: float = 0.999
    
    def update(self, delta_time: float) -> None:
        self.angular_acceleration = -(self.gravity / self.length) * sin(self.angle)
        self.angular_velocity = self.angular_velocity + (self.angular_acceleration * delta_time)
        self.angular_velocity *= self.damping
        self.angle = self.angle + (self.angular_velocity * delta_time)
    
    def position(self) -> Tuple[float, float]:
        x0, y0 = self.origin
        
        x: float = x0 + self.length * sin(self.angle)
        y: float = y0 + self.length * cos(self.angle)
        
        return x, y