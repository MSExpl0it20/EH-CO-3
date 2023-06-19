# import pygame
# from game.components.bullets.bullet import Bullet
# from game.utils.constants import ENEMY_TYPE


# class ballerManager:
#     def __init__(self):
#         # self.bullets: list[Bullet] = []
#         self.enemy_bullets: list[Bullet] = []

#     def update(self, game, input_state, enemies):
#         # self.events()
#         # self.player.update()
#         # self.enemy_manager.update(self)
#         # self.balletManager.update(self.input)

#         for bullet in self.enemy_bullets:
#             bullet.update(self.enemy_bullets, input_state, enemies)
#             if bullet.rect.colliderect(game.player.rect):
#                 self.enemy_bullets.remove(bullet)
#                 game.playing = False
#                 pygame.time.delay(1000)
#                 break

#     def draw(self, screen):
#         for bullet in self.enemy_bullets:
#             bullet.draw(screen)

#     def add_bullet(self, bullet):
#         if bullet.owner == ENEMY_TYPE and not self.enemy_bullets:
#             self.enemy_bullets.append(bullet)
import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE, SHIELD_TYPE


class BalletManager:
    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets: list[Bullet] = []

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_type != SHIELD_TYPE:
                    game.playing = False
                    game.death_count += 1
                    pygame.time.delay(1000)
                    break

        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)
            
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    game.enemy_manager.enemies.remove(enemy)
                    game.score += 1
                    self.player_bullets.remove(bullet)
                    

    def draw(self, screen):
        for bullet in self.enemy_bullets + self.player_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(bullet)