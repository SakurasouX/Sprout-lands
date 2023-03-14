import pygame

import sys
import time

from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Sprout lands')
        self.clock = pygame.time.Clock()

        self.level = Level(self.screen)

        # Time
        self.previous_frame_time = time.time()

    def run(self):
        while True:
            dt = time.time() - self.previous_frame_time
            self.previous_frame_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.level.run(dt)
            pygame.display.flip()
            self.clock.tick(165)


if __name__ == '__main__':
    game = Game()
    game.run()
