import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0

    while True:
        screen.fill(color="black")
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        elapsed_time_ms = game_clock.tick(60)
        dt = elapsed_time_ms / 1000  # convert from ms to sec


if __name__ == "__main__":
    main()
