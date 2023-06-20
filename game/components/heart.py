import random
import pygame
from game.components.heart import Powerup
from game.utils.constants import SPACESHIP, SPACESHIP_HEART


class PowerupManager:
    def __init__(self):
        self.powerups = []
        self.when_appears = random.randint(10000, 15000)
        self.duration = 5000

    def generate_powerup(self):
        heart = Powerup(SPACESHIP_HEART)
        self.when_appears += random.randint(10000, 15000)
        self.powerups.append(heart)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.powerups) == 0 and current_time >= self.when_appears:
            self.generate_powerup()

        for powerup in self.powerups:
            powerup.update(game.game_speed, self.powerups)
            if game.player.rect.colliderect(powerup):
                game.player.lives += 1  
                self.powerups.remove(powerup)

        self.draw(game.screen)

    def draw(self, screen):
        for powerup in self.powerups:
            powerup.draw(screen)

    def reset(self):
        now = pygame.time.get_ticks()
        self.powerups = []
        self.when_appears = random.randint(now + 10000, now + 15000)