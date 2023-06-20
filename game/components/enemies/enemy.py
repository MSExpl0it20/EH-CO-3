# import random
# from typing import Any
# import pygame
# from pygame.sprite import Sprite
# from game.components.bullets import balletManager
# from game.components.bullets.bullet import Bullet


# from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH


# LEFT = "left"
# RIGHT = "right"
# IMAGE = "image"
# SPEED_X = "speed_x"
# SPEED_Y = "speed_y"
# MOVE_X = "move_x"

# class Enemy(Sprite):
#     MOVEMENTS = [LEFT, RIGHT]
#     X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
#     Y_POS = 20
#     SPEED_X = 5
#     SPEED_Y = 1
#     VARIANTS = {
#         1:{
#             IMAGE: ENEMY_1,
#             SPEED_X: 4,
#             SPEED_Y: 2,
#             MOVE_X: (40, 100)
#         },
#         2:{
#             IMAGE: ENEMY_2,
#             SPEED_X: 4,
#             SPEED_Y: 2,
#             MOVE_X: (50, 100)
#         }
#     }

#     def __init__(self, variant):
#         enemy_variant = self.VARIANTS[variant]
#         self.image = pygame.transform.scale(enemy_variant[IMAGE], (50, 40))
#         self.shooting_time = pygame.time.get_ticks() + random.randint(30, 50)
#         self.rect = self.image.get_rect()
#         self.rect.x = random.choice(self.X_POS_LIST)
#         self.rect.y = self.Y_POS
#         self.type = ENEMY_TYPE

#         if 'speed_x' in enemy_variant:
#             self.speed_x = enemy_variant['speed_x']
#         else:
#             self.speed_x = 0

#         enemy_variant = {
#             'speed_x': 2,
#             'speed_y': -1
#         }
#         enemy = Enemy(variant=enemy_variant)
#         # self.speed_x = variant.get('speed_x', 0)
#         # self.speed_y = variant.get('speed_y', 0)

#         # self.speed_x = enemy_variant[SPEED_X]
#         # self.speed_y = enemy_variant[SPEED_Y]

#         self.movement = random.choice(self.MOVEMENTS)
#         lower_limit, upper_limit = enemy_variant[MOVE_X]
#         self.move_x = random.randint(lower_limit, upper_limit)
#         self.moving_index = 0
#         # self.shooting_time = random.randint(30, 50)
    

#     def update(self, ships, game):
#         # self.rect.y += self.speed_y
#         # self.rect1.y += self.speed_y
#         self.shoot(game.balletManager)
#         current_time = pygame.time.get_ticks()
#         if self.shooting_time <= current_time:
#             bullet = Bullet(self)
#             balletManager.add_bullet(bullet)
#             self.shooting_time += random.randint(30, 50)

#         if self.movement == LEFT:
#             self.rect.x -= self.speed_x
#         else:
#             self.rect.x += self.speed_x
            

#         # if self.movement == LEFT:
#         #     self.rect1.x += self.speed_x
#         # else:
#         #     self.rect1.x -= self.speed_x

#         self.update_movement()

#         if self.rect.y >= SCREEN_HEIGHT or self.rect1.y >= SCREEN_HEIGHT:
#             ships.remove(self)

#         if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH - self.rect.width:
#             self.speed_x *= -1

#         if self.rect1.x <= 0 or self.rect1.x >= SCREEN_WIDTH - self.rect1.width:
#             self.speed_x *= -1
#         # if self.rect.x <= 0:
#         #     self.rect.x = 0
#         # elif self.rect.x >= SCREEN_WIDTH - self.rect.width:
#         #     self.rect.x = SCREEN_WIDTH - self.rect.width

#         # if self.rect1.x <= 0:
#         #     self.rect1.x = 0
#         # elif self.rect1.x >= SCREEN_WIDTH - self.rect1.width:
#         #     self.rect1.x = SCREEN_WIDTH - self.rect1.width

#         # if self.rect1.y >= SCREEN_HEIGHT:
#         #     ships.remove(self)
            
        
#     def update_movement(self):
#         self.moving_index += 1
#         if self.rect.x >= SCREEN_WIDTH - 50:
#             self.movement = LEFT
#         elif self.rect.x <= 0:
#             self.movement = RIGHT
        
#         if self.moving_index >= self.move_x:
#             self.moving_index = 0
#             self.movement = LEFT if self.movement == RIGHT else RIGHT
            

#     def draw(self, screen):
#         screen.blit(self.image, (self.rect.x, self.rect.y))
#         screen.blit(self.image1, (self.rect1.x, self.rect.y))

#     def shoot(self, bulletManager):
#         current_time = pygame.time.get_ticks()
#         if self.shooting_time <= current_time:
#             bullet = Bullet(self)
#             bulletManager.add_bullet(bullet)
#             self.shooting_time += random.randint(30, 50)
# --------------------------------------------
# import random
# from typing import Any
# import pygame
# from pygame.sprite import Sprite

# from game.components.bullets import balletManager
# from game.components.bullets.bullet import Bullet
# from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH


# LEFT = "left"
# RIGHT = "right"
# IMAGE = "image"
# SPEED_X = "speed_x"
# SPEED_Y = "speed_y"
# MOVE_X = "move_x"

# class Enemy(Sprite):
#     MOVEMENTS = [LEFT, RIGHT]
#     X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
#     Y_POS = 20
#     VARIANTS = {
#         1: {
#             IMAGE: ENEMY_1,
#             SPEED_X: 4,
#             SPEED_Y: 2,
#             MOVE_X: (40, 100)
#         },
#         2: {
#             IMAGE: ENEMY_2,
#             SPEED_X: 4,
#             SPEED_Y: 2,
#             MOVE_X: (50, 100)
#         }
#     }

#     def __init__(self, variant):
#         enemy_variant = self.VARIANTS[variant]
#         self.image = pygame.transform.scale(enemy_variant[IMAGE], (50, 40))
#         self.shooting_time = pygame.time.get_ticks() + random.randint(30, 50)
#         self.rect = self.image.get_rect()
#         self.rect.x = random.choice(self.X_POS_LIST)
#         self.rect.y = self.Y_POS
#         self.type = ENEMY_TYPE
#         self.speed_x = enemy_variant.get(SPEED_X, 0)

#         self.movement = random.choice(self.MOVEMENTS)
#         lower_limit, upper_limit = enemy_variant[MOVE_X]
#         self.move_x = random.randint(lower_limit, upper_limit)
#         self.moving_index = 0

#     def update(self, ships, game):
#         self.shoot(game.balletManager)
#         current_time = pygame.time.get_ticks()

#         if self.shooting_time <= current_time:
#             bullet = Bullet(self)
#             balletManager.add_bullet(bullet)
#             self.shooting_time += random.randint(30, 50)

#         if self.movement == LEFT:
#             self.rect.x -= self.speed_x
#         else:
#             self.rect.x += self.speed_x

#         self.update_movement()

#         if self.rect.y >= SCREEN_HEIGHT:
#             ships.remove(self)

#         if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH - self.rect.width:
#             self.speed_x *= -1

#     def update_movement(self):
#         self.moving_index += 1

#         if self.rect.x >= SCREEN_WIDTH - 50:
#             self.movement = LEFT
#         elif self.rect.x <= 0:
#             self.movement = RIGHT

#         if self.moving_index >= self.move_x:
#             self.moving_index = 0
#             self.movement = LEFT if self.movement == RIGHT else RIGHT

#     def draw(self, screen):
#         screen.blit(self.image, (self.rect.x, self.rect.y))

#     def shoot(self, bulletManager):
#         current_time = pygame.time.get_ticks()

#         if self.shooting_time <= current_time:
#             bullet = Bullet(self)
#             bulletManager.add_bullet(bullet)
#             self.shooting_time += random.randint(30, 50)
import pygame
import random
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
<<<<<<< HEAD
from game.components.bullets.bullet_manager import BulletManager
=======
from game.components.bullets.balletManager import BalletManager
>>>>>>> ace02a7f1cb42439456c3080b17de4c781006881
from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH


LEFT ='left'
RIGHT ='right'
IMAGE = 'image'
SPEED_X = 'speed_x'
SPEED_Y = 'speed_y'
MOVE_X = 'move_x'

class Enemy(Sprite):
    MOVEMENTS = [LEFT, RIGHT]
    X_POS_LIST = [50, 100, 150, 200, 250, 350, 400, 450, 500, 550]
    Y_POS = 20
    VARIANTS = {
        1:{
            IMAGE: ENEMY_1,
            SPEED_X: 5,
            SPEED_Y: 1,
            MOVE_X: (30, 100)
        },
        2: {
            IMAGE: ENEMY_2,
            SPEED_X: 5,
            SPEED_Y: 2,
            MOVE_X: (67, 150)
        }
    }
    
    def __init__(self, variant):
        enemy_variant = self.VARIANTS[variant]
        self.image = pygame.transform.scale(enemy_variant[IMAGE], (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.type = ENEMY_TYPE
        
        self.speed_x = enemy_variant[SPEED_X]
        self.speed_y = enemy_variant[SPEED_Y]
        
        self.movement = random.choice(self.MOVEMENTS)
        lower_limit, upper_limit = enemy_variant[MOVE_X]
        self.move_x = random.randint(lower_limit, upper_limit)
        self.moving_index = 0
        self.shooting_time = random.randint(30, 50)
    
    def update(self, ships, game):
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager, game.enemy_manager)
        if self.movement == LEFT:
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
            
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)
            
        self.update_movement()
            
            
    def update_movement(self):
        self.moving_index += 1
        if  self.rect.x >= SCREEN_WIDTH - 50:
            self.movement = LEFT
        elif self.rect.x <= 0:
            self.movement = RIGHT
            
        if self.moving_index >= self.move_x:
            self.moving_index = 0
            self.movement = LEFT if self.movement == RIGHT else RIGHT
        
        
    def draw(self, screen):
        screen.blit (self.image,(self.rect.x, self.rect.y))
        
    def shoot(self, bullet_manager, enemy_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            for bullet in enemy_manager.enemies: 
                bullet = Bullet(self)
                bullet_manager.add_bullet(bullet)
                self.shooting_time += random.randint(30, 50)