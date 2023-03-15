import pygame

from settings import *


class Generic(pygame.sprite.Sprite):
    def __init__(self, position, surface, group, z=LAYERS['main']):
        super().__init__(group)
        self.image = surface
        self.rect = self.image.get_rect(topleft=position)
        self.z = z
