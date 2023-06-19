
# from game.components.enemies.enemy import Enemy

# class EnemyManager:
#     def __init__(self):
#         self.enemies: list[Enemy] = []
    
#     def update(self, game):
#         if not self.enemies:
#             self.enemies.append(Enemy(variant=1))

#         for enemy in self.enemies:
#             enemy.update(self.enemies, game) 
         
       
#     def draw(self, Screen):
#         for enemy in self.enemies:
#             enemy.draw(Screen)
        
from game.components.enemies.enemy import Enemy
# from game.utils.constants import ENEMY_2
# from game.components.enemies.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] = []

    def update(self, game):
        if not self.enemies:
            self.enemies.append(Enemy())
            # self.enemies.append(ENEMY_2())


        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def reset(self):
        self.enemies = []
