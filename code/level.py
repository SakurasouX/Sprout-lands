import pygame
from pytmx.util_pygame import load_pygame


from settings import *
from player import Player
from ui import UI
from sprites import Generic, Water, WildFlower, Tree
from support import *


class Level:
    def __init__(self, surface):
        self.display_surface = surface
        self.all_sprites = CameraGroup()
        self.setup()
        self.ui = UI(self.player)

    def setup(self):
        tmx_data = load_pygame('../levels/level_data/main.tmx')

        # Water
        water_frames = import_folder('../levels/level_graphics/water_frames')
        for x, y, surface in tmx_data.get_layer_by_name('water').tiles():
            Water((x * TILE_SIZE, y * TILE_SIZE), water_frames, self.all_sprites)

        # Ground
        for x, y, surface in tmx_data.get_layer_by_name('ground').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surface, self.all_sprites, LAYERS['ground'])

        # Hills
        for x, y, surface in tmx_data.get_layer_by_name('hills').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surface, self.all_sprites, LAYERS['hills'])

        # Tall hills
        for x, y, surface in tmx_data.get_layer_by_name('tall_hills').tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), surface, self.all_sprites, LAYERS['hills'])

        # House
        for layer in ['house_floor', 'house_furniture_bottom']:
            for x, y, surface in tmx_data.get_layer_by_name(layer).tiles():
                Generic((x * TILE_SIZE, y * TILE_SIZE), surface, self.all_sprites, LAYERS['house_bottom'])

        for layer in ['house_walls', 'house_furniture_top']:
            for x, y, surface in tmx_data.get_layer_by_name(layer).tiles():
                Generic((x * TILE_SIZE, y * TILE_SIZE), surface, self.all_sprites)

        # Fences
        for layer in ['fences']:
            for x, y, surface in tmx_data.get_layer_by_name(layer).tiles():
                Generic((x * TILE_SIZE, y * TILE_SIZE), surface, self.all_sprites)

        # Trees
        for obj in tmx_data.get_layer_by_name('trees'):
            Tree((obj.x, obj.y), obj.image, self.all_sprites, obj.name)

        # WildFlower
        for obj in tmx_data.get_layer_by_name('decorations'):
            WildFlower((obj.x, obj.y), obj.image, self.all_sprites)

        self.player = Player((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), self.all_sprites)

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
            for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)
