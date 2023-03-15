import pygame

from settings import *

class UI:
    def __init__(self, player):

        # General setup
        self.display_surface = pygame.display.get_surface()
        self.player = player

        # Imports
        ui_path = '../graphics/ui/'
        self.tools_surface = {tool: pygame.image.load(f"{ui_path}/{tool}.png").convert_alpha() for tool in player.tools}
        self.seeds_surface = {seed: pygame.image.load(f"{ui_path}/{seed}.png").convert_alpha() for seed in player.seeds}

    def display(self):

        # Tools display
        tool_surface = self.tools_surface[self.player.selected_tool]
        tool_rect = tool_surface.get_rect(topleft=TOOLS_UI_POSITION)
        self.display_surface.blit(tool_surface, tool_rect)

        # Seeds display
        seed_surface =self.seeds_surface[self.player.selected_seed]
        seed_rect = seed_surface.get_rect(midbottom=SEEDS_UI_POSITION)
        self.display_surface.blit(seed_surface, seed_rect)
