import pygame

from settings import *
from player import Player
from ui import UI
from sprites import Generic


class Level:
    def __init__(self, surface):
        self.display_surface = surface
        self.all_sprites = CameraGroup()
        self.setup()
        self.ui = UI(self.player)

    def setup(self):
        self.player = Player((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), self.all_sprites)
        Generic((0, 0),
                pygame.image.load('../graphics/world/ground.png').convert_alpha(),
                self.all_sprites,
                LAYERS['ground'])

    def run(self, dt):
        self.display_surface.fill('white')
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)
        self.ui.display()


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)
