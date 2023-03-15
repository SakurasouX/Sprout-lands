import pygame

from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, position, group):

        # General setup
        pygame.sprite.Sprite.__init__(self, group)
        self.image = pygame.Surface((32, 64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center=position)

        # Movement
        self.speed = 200
        self.direction = pygame.math.Vector2()
        self.position = pygame.math.Vector2(self.rect.center)

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
