import pygame
from simulation.pendulum import Pendulum
from visualization.config import (
    BACKGROUND_COLOR,
    LINE_COLOR,
    LINE_WIDTH,
    PENDULUM_COLOR,
    PENDULUM_MASS
)

def draw_pendulum(screen: pygame.Surface, pendulum: Pendulum) -> None:
    screen.fill(BACKGROUND_COLOR)
    
    x, y = pendulum.position()
    
    pygame.draw.line(
        screen,
        LINE_COLOR,
        pendulum.origin,
        (int(x), int(y)),
        LINE_WIDTH
    )
    pygame.draw.circle(
        screen,
        PENDULUM_COLOR,
        (int(x), int(y)),
        PENDULUM_MASS
    )
    
    pygame.display.flip()
    