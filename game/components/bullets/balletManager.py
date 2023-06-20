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
from pygame.sprite import Sprite
from game.components import bullets

from game.utils.constants import BULLET, BULLET_ENEMY, ENEMY_TYPE, PLAYER_TYPE, SCREEN_HEIGHT

class Bullet(Sprite):
    SPEED = 20
    ENEMY_BULLET_IMG = pygame.transform.scale(BULLET_ENEMY, (9, 32))
    PLAYER_BULLET_IMG = pygame.transform.scale(BULLET, (9, 32))
    BULLETS = {ENEMY_TYPE: ENEMY_BULLET_IMG, PLAYER_TYPE: PLAYER_BULLET_IMG}

    def __init__(self, spaceship):
        self.image = self.BULLETS[spaceship.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type

        self.shot_sound = pygame.mixer.Sound("game/assets/sound/blaster-2-81267.mp3")
        self.enemy_death_sound = pygame.mixer.Sound("game/assets/sound/hq-explosion-6288.mp3")

    def update(self, bullets, enemies):
        if self.owner == ENEMY_TYPE:
            self.rect.y += self.SPEED 
            if self.rect.y >= SCREEN_HEIGHT:
                bullets.remove(self)
        elif self.owner == PLAYER_TYPE:
            self.rect.y -= self.SPEED
            if self.rect.y < 0:
                self.shot_sound.play()
                bullets.remove(self) 

            # Verificar colisiones con naves enemigas
            for enemy in enemies:
                if pygame.sprite.collide_rect(self, enemy):
                    self.destroy()
                    enemy.destroy()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def destroy(self):
        if self.owner == PLAYER_TYPE:
            self.enemy_death_sound.play()
            bullets.remove(self)
