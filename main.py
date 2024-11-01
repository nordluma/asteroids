import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    updateable.add(player)
    drawable.add(player)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updateable.update(dt)
        drawable.draw(screen)

        pygame.display.flip()

        # tick returns elapsed time in ms by passing in 60 we will limit the
        # framerate to 60 FPS
        dt = game_clock.tick(60) / 1000  # convert from ms to sec


if __name__ == "__main__":
    main()
