# import pygame
# from pygame.sprite import Sprite
# from game.components import bullets

# from game.utils.constants import BULLET, BULLET_ENEMY, ENEMY_TYPE, SCREEN_HEIGHT


# class Bullet(Sprite):
#     SPEED = 20
#     ENEMY_BULLET_IMG = pygame.transform.scale(BULLET_ENEMY, (9, 32))
#     PLAYER_BULLET_IMG = pygame.transform.scale(BULLET, (9, 32))
#     BULLETS = { ENEMY_TYPE: ENEMY_BULLET_IMG, BULLET: PLAYER_BULLET_IMG }                            
#     def __init__(self, spaceship):   
#         super().__init__()            
#         self.image = self.BULLETS[spaceship.type]
#         self.rect = self.image.get_rect()
#         self.rect.center = spaceship.rect.center
#         self.rect.bottom = spaceship.rect.top
#         self.owner = spaceship.type

#     def update(self, bullets, input_status, enemies):
#         # if input[pygame.K_SPACE]:
#         #     if self.owner == BULLET:
#         #         self.rect.y -= self.SPEED
#         #         if self.rect.bottom <= 0:
#         #             bullets.remove(self)
#         #         else:
#         #             self.check_collision(enemies)

#         if self.owner == ENEMY_TYPE:
#             self.rect.y += self.SPEED
#             if self.rect.y >= SCREEN_HEIGHT:
#                 bullets.remove(self)

#     def draw(self, screen):
#         screen.blit(self.image, (self.rect.x, self.rect.y))

#     def check_collision(self, enemies):
#         for enemy in enemies:
#             if self.rect.colliderect(enemy.rect):
#                 enemies.remove(enemy)
#                 bullets.remove(self)

import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET, BULLET_ENEMY,SPACESHIP_TYPE, ENEMY_TYPE, SCREEN_HEIGHT

class Bullet(Sprite):

    SPEED = 20
    ENEMY_BULLET_IMG = pygame.transform.scale(BULLET_ENEMY,(9, 32))
    SPACESHIP_BULLET = pygame.transform.scale(BULLET,(9, 32))

    BULLETS = { ENEMY_TYPE : ENEMY_BULLET_IMG,
                SPACESHIP_TYPE :SPACESHIP_BULLET,
               }

    def __init__(self,spaceship):

        self.image = self.BULLETS[spaceship.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type

    def update(self, bullets):
        
        if self.owner == ENEMY_TYPE:
            self.rect.y += self.SPEED 
            if self.rect.y >= SCREEN_HEIGHT:
                bullets.remove(self)
                
        elif self.owner == SPACESHIP_TYPE:
            self.rect.y -= self.SPEED
            if self.rect.y <= 0:
                bullets.remove(self)
                

    def draw(self,screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

        
