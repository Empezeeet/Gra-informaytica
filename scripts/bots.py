from ursina import *
import math
import random
import time
import threading
from threading import Thread



class Bots():
    bot = None
    
    def __init__(self, hp, speed):
        self.health = hp
        self.speed = speed
        
        
    def spawn(self, position):
        Bots.bot = Entity(model='sphere', collider='sphere', color=color.rgb(166, 36, 27), scale=(2.5, 2.5, 2.5))
        Bots.bot.position = position
        
    def rtp(self):
        Bots.bot.position = (random.randint(-10, 10), 5, random.randint(-10, 10))
        
    def start_attacking_tower(self):
        
        #Settings Move direction
        spawnPoint_xStatus = None #True = +x | False = -x
        spawnPoint_zStatus = None #True = +x | False = -x
        print("[ OK ] SPAWNPOINT STATUS VAR ADD")
            
        if (self.bot.position.x < 0):
            spawnPoint_xStatus = False
            print("X" + str(self.bot.position.x) + " | " + str(spawnPoint_xStatus))
        if (self.bot.position.x > 0):
            spawnPoint_xStatus = True
            print("X" + str(self.bot.position.x) + " | " + str(spawnPoint_xStatus))
# 
        if (self.bot.position.z < 0):
            spawnPoint_zStatus = False
            print("Z" + str(self.bot.position.z) + " | " + str(spawnPoint_zStatus))
        if (self.bot.position.z > 0):
            spawnPoint_zStatus = True
            print("Z" + str(self.bot.position.z) + " | " + str(spawnPoint_zStatus))
        
        print("[ OK ] SPAWNPOINT DIRECTION TO GO STATUS")
#       