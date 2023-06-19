# import random
# import pygame
# from game.components.powerups.shield import Shield
# from game.utils.constants import SPACESHIP_SHIELD

# class Manager:
#     def __init__(self):
#         self.power_ups = []
#         self.when_appears = random.randint(10000, 15000)
#         self.duration = random.randint(2, 3)

#     def generate_power_up(self):
#         shield = Shield()
#         self.when_appears += random.randint(10000, 15000)
#         self.power_ups.append(shield)

#     def update(self, game):
#         current_time = pygame.time.get_ticks()

#         if len(self.power_ups) == 0 and current_time >= self.when_appears:
#             self.generate_power_up()

#         for power_up in self.power_ups:
#             power_up.update(game.game_speed, self.power_ups)
#             if game.player.rect.colliderect(power_up):
#                 power_up.start_time = pygame.time.get_ticks()
#                 game.player.power_up_type = power_up.type
#                 game.player.has_power_up = True
#                 game.player.power_up_time = power_up.start_time + (self.duration*1000)
#                 game.player.set_image(SPACESHIP_SHIELD, (65, 75))
#                 self.power_ups.remove(power_up)

#     def draw(self, screen):
#         for power_up in self.power_ups:
#             power_up.draw(screen)

#     def reset(self):
#         now = pygame.time.get_ticks()
#         self.power_ups = []
#         self.when_appears = random.randint(now + 10000, now + 15000)
# ------------------------------------------------
import random
import pygame
from game.components.powerups.shield import Shield
from game.utils.constants import DEFAULT_TYPE, SPACESHIP, SPACESHIP_SHIELD

class Manager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(10000, 15000)
        self.duration = random.randint(3, 5)

    def generate_power_up(self):
        shield = Shield()
        self.when_appears += random.randint(10000, 15000)
        self.power_ups.append(shield)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.power_up_time = power_up.start_time + (self.duration*1000)
                game.player.set_image((65, 75), SPACESHIP_SHIELD)
                self.power_ups.remove(power_up)

        if game.player.has_power_up and current_time >= game.player.power_up_time:
            game.player.has_power_up = False
            game.player.power_up_type = DEFAULT_TYPE
            game.player.set_image((40, 60), SPACESHIP)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears = random.randint(now + 10000, now + 15000)
