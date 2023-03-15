import pygame

from settings import *
from support import *
from timer import Timer


class Player(pygame.sprite.Sprite):
    def __init__(self, position, group):

        pygame.sprite.Sprite.__init__(self, group)

        self.import_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 3

        # General setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=position)

        # Movement
        self.speed = 300
        self.direction = pygame.math.Vector2()
        self.position = pygame.math.Vector2(self.rect.center)

        # Timers
        self.timers = {
            'tool_use': Timer(350, self.use_tool),
            'tool_switch': Timer(200),
            'seed_use': Timer(350, self.use_seed),
            'seed_switch': Timer(200),
        }

        # Tools
        self.tools = ['hoe', 'axe', 'water']
        self.tool_index = 0
        self.selected_tool = self.tools[self.tool_index]

        # Seeds
        self.seeds = ['corn', 'tomato']
        self.seed_index = 0
        self.selected_seed = self.seeds[self.seed_index]

    def use_tool(self):
        pass

    def use_seed(self):
        pass

    def import_assets(self):

        self.animations = {
            'down': [], 'up': [], 'left': [], 'right': [],
            'down_idle': [], 'up_idle': [], 'left_idle': [], 'right_idle': [],
            'down_axe': [], 'up_axe': [], 'left_axe': [], 'right_axe': [],
            'down_hoe': [], 'up_hoe': [], 'left_hoe': [], 'right_hoe': [],
            'down_water': [], 'up_water': [], 'left_water': [], 'right_water': [],
        }

        for animation in self.animations.keys():
            full_path = '../graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self, dt):
        self.frame_index += self.animation_speed * dt

        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]

    def player_input(self):
        keys = pygame.key.get_pressed()

        if not self.timers['tool_use'].active:
            # Directions
            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0

            if keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = 'left'
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = 'right'
            else:
                self.direction.x = 0

            # Tools use
            if keys[pygame.K_SPACE]:
                self.timers['tool_use'].activate()
                self.direction = pygame.math.Vector2()
                self.frame_index = 0

            # Tools switching
            if keys[pygame.K_q] and not self.timers['tool_switch'].active:
                self.timers['tool_switch'].activate()
                self.tool_index += 1
                if self.tool_index >= len(self.tools):
                    self.tool_index = 0
                self.selected_tool = self.tools[self.tool_index]

            # Seed use
            if keys[pygame.K_LCTRL]:
                self.timers['seed_use'].activate()
                self.direction = pygame.math.Vector2()
                self.frame_index = 0
                print('used seed')

            # Seeds switching
            if keys[pygame.K_e] and not self.timers['seed_switch'].active:
                self.timers['seed_switch'].activate()
                self.seed_index += 1
                if self.seed_index >= len(self.seeds):
                    self.seed_index = 0
                self.selected_seed = self.seeds[self.seed_index]
                print(self.selected_seed)

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def get_status(self):

        # Idle status
        if not self.direction.magnitude():
            self.status = self.status.split('_')[0] + '_idle'

        # Tool status
        if self.timers['tool_use'].active:
            self.status = self.status.split('_')[0] + '_' + self.selected_tool

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
        self.get_status()
        self.update_timers()
        self.player_movement(dt)
        self.animate(dt)
