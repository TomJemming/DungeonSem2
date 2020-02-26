import arcade
import math


class Enemy(Sprite):

    def __init__(self):
        pass

    def damage(self):
        if self.enemy_life == 0:
            enemy.kill
