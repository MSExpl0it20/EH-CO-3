
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
        
<<<<<<< HEAD

=======
>>>>>>> ace02a7f1cb42439456c3080b17de4c781006881
import random
from game.components.enemies.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] = []
    
    
    def update(self, game):
        if not self.enemies:
            enemy_variant = random.randint(1, 2)
            self.enemies.append(Enemy(enemy_variant))
            
        
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
            
    def reset(self):
        self.enemies =[]