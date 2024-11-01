import sys
import pygame
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from shoot import Shoot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    asteroids = pygame.sprite.Group()
    shootable = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    Shoot.containers = (shootable, updateable, drawable)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updateable:
            obj.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        for obj in asteroids:
            if obj.collision(player):
                print("Game over!")
                sys.exit()
            for shot in shootable:
                if shot.collision(obj):
                    obj.kill()
                    shot.kill()

        pygame.display.flip()

        # tick returns elapsed time in ms by passing in 60 we will limit the
        # framerate to 60 FPS
        dt = game_clock.tick(60) / 1000  # convert from ms to sec


if __name__ == "__main__":
    main()
