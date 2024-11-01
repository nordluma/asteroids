import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shoot(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            width=SHOT_RADIUS,
            center=self.position,
            radius=self.radius,
        )

    def update(self, dt: int):
        self.position += self.velocity * dt
