import random

from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    BIRD_HEIGHTS = [250, 290, 320]

    def __init__(self, image):
        self.index = 0
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice(self.BIRD_HEIGHTS)

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        self.image = BIRD[0] if self.index // 5 else BIRD[1]
        screen.blit(self.image, self.rect)
        self.index += 1