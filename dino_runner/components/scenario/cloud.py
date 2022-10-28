import random
import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH
from dino_runner.utils.constants import CLOUD


class Cloud(Sprite):
    def __init__(self):
        pass

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(screen):
        screen.blit(CLOUD, (random.randint(0, 1000), random.randint(50, 100)))
