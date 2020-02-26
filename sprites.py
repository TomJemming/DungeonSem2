import arcade
import math


class Enemy(Sprite):

    def __init__(self, name, hp, move, evasion_x, evasion_y, evasion_cooldown):
        self.hp = 1
        self.name = name
        if self.name = "spider":
            self.move = 2
        else:
            self.move = 1
        self.evasion_x = 0          #replace global values x2 and x4 to get local values
        self.evasion_y = 0
        self.evasion_cooldown = 0


    def damage(self):
        if self.hp == 0:
            enemy.kill
