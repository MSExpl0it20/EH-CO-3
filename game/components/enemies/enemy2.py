import pygame
import random
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_2, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH


class Enemy2(Sprite):
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 2

    def __init__(self):
        self.image = pygame.transform.scale(ENEMY_2, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS    
        self.type = ENEMY_TYPE

        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y

        self.move_x = random.randint(30, 100)
        self.moving_index = 0
        self.zigzag_counter = 0
        self.shooting_time = random.randint(30, 50)

    def update(self, ships, game):
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)

        self.update_movement()
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)
    
    def update_movement(self):
        self.moving_index += 1
        if self.moving_index >= self.move_x:
            self.zigzag_counter += 1
            if self.zigzag_counter % 2 == 0:
                self.rect.x -= self.speed_x
                if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH:
                    self.speed_x = +self.speed_x 
            self.moving_index = 0

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30, 50)