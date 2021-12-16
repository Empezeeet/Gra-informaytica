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
        
    def start_attacking_tower(self):
        if Bots.bot != None:
            #Settings Move direction
            spawnPoint = self.bot.position
            spawnPoint_xStatus = None #True = +x | False = -x
            spawnPoint_zStatus = None #True = +x | False = -x
                
            if (spawnPoint.x < 0):
                spawnPoint_xStatus = False
            if (spawnPoint.x > 0):
                spawnPoint_xStatus = True
            if (spawnPoint.z < 0):
                spawnPoint_zStatus = False
            if (spawnPoint.z > 0):
                spawnPoint_zStatus = True
                    
            isInTower = False
            while not(isInTower):
                #Checking is enemy on tower
                if (self.bot.position == (0, 2, 0)):
                    self.bot.visible = False
                    self.bot.disable()
                    isInTower = True
                
                if (spawnPoint_xStatus == False) and (spawnPoint_zStatus == False): #X is on (-) & Z is on (-)
                    while self.bot.position != (0, 2, 0):
                            self.bot.position += (1, 0, 1)
                if (spawnPoint_xStatus == True) and (spawnPoint_zStatus == True): #X is on (+) & Z is on (+)
                    while self.bot.position != (0, 2, 0):
                            self.bot.position -= (1, 0, 1)
                if (spawnPoint_xStatus == True) and (spawnPoint_zStatus == False): #X is on (+) & Z is on (-)
                    while self.bot.position != (0, 2, 0):
                            self.bot.position += (-1, 0, 1)
                if (spawnPoint_xStatus == False) and (spawnPoint_zStatus == True): #X is on (-) & Z is on (+)
                    while self.bot.position != (0, 2, 0):
                            self.bot.position += (1, 0, -1)
                time.sleep(1)