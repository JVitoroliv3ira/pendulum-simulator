import pygame
from simulation.pendulum import Pendulum
from visualization.render import draw_pendulum
from visualization.config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    LINE_ORIGIN,
    LINE_LENGTH,
    LINE_ANGLE,
    GRAVITY,
    FPS
)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simulador de Pêndulo Simples")

pendulum = Pendulum(
    origin=LINE_ORIGIN,
    length=LINE_LENGTH,
    angle=LINE_ANGLE,
    gravity=GRAVITY
)

clock = pygame.time.Clock()
running = True

while running:
    delta_time = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pendulum.update(delta_time)
    draw_pendulum(screen, pendulum)

pygame.quit()