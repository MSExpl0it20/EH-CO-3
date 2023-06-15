from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE


class ballerManager:
    def __init__(self):
        # self.bullets: list[Bullet] = []
        self.enemy_bullets: list[Bullet] = []

    def update(self, game, player):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(self)
                game.playing = False
                break
            
    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(bullet)