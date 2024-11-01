import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: int):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            width=2,
            center=self.position,
            radius=self.radius,
        )

    def update(self, dt: int):
        self.position += self.velocity * dt
