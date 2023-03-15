import pygame

from settings import *
from support import *


class Player(pygame.sprite.Sprite):
    def __init__(self, position, group):

        pygame.sprite.Sprite.__init__(self, group)

        self.import_assets()
        self.status = 'right'
        self.frame_index = 0
        self.animation_speed = 0.15

        # General setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=position)

        # Movement
        self.speed = 200
        self.direction = pygame.math.Vector2()
        self.position = pygame.math.Vector2(self.rect.center)

    def import_assets(self):
        self.animations = {
            'down': [], 'up': [], 'left': [], 'right': [],
        }

        for animation in self.animations.keys():
            full_path = '../graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)

    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def player_movement(self, dt):
        # Normalizing a vector
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # Horizontal movement
        self.position.x += self.direction.x * self.speed * dt
        self.rect.centerx = round(self.position.x)

        # Vertical movement
        self.position.y += self.direction.y * self.speed * dt
        self.rect.centery = round(self.position.y)

    def update(self, dt):
        self.player_input()
        self.player_movement(dt)
