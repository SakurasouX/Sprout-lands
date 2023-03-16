import pygame

from settings import *


class Generic(pygame.sprite.Sprite):
    def __init__(self, position, surface, group, z=LAYERS['main']):
        super().__init__(group)
        self.image = surface
        self.rect = self.image.get_rect(topleft=position)
        self.z = z


class Water(Generic):
    def __init__(self, position, frames, group):
        self.frames = frames
        self.frame_index = 0
        self.animation_speed = 3
        super().__init__(
            position=position,
            surface=frames[self.frame_index],
            group=group,
            z=LAYERS['water']
        )

    def animate(self, dt) -> None:
        self.frame_index += self.animation_speed * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, dt) -> None:
        self.animate(dt)


class WildFlower(Generic):
    def __init__(self, position, surface, group):
        super().__init__(position, surface, group)


class Tree(Generic):
    def __init__(self, position, surface, group, name):
        super().__init__(position, surface, group)
