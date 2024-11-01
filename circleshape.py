import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: int):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collision(self, other) -> bool:
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt: int):
        # sub-classes must override
        pass
