from ursina import *
import math
import random
import time


class Bots():
    bot = None
    
    def __init__(self, hp, speed):
        self.health = hp
        self.speed = speed
        
        
    def spawn(self, position):
        Bots.bot = Entity(model='sphere', collider='sphere', color=color.rgb(166, 36, 27), scale=(2.5, 2.5, 2.5))
        Bots.bot.position = position
        
    def rtp(self):
        Bots.bot.position = (random.randint(0, 10), 5, random.randint(0, 10))
    
        