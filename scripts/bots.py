#Simple Bots' AI Script
#Copyright 2021-2022, Empezeeet, All Rights Reserved


if __name__ == "__main__":
    print("Wrong file")
    raise RuntimeError("Run main.py not bots.py")
    exit()



try:
    from ursina import *
    import math
    import random
    import time
    import threading
    from threading import Thread
    import scripts.exceptions as __exceptions
    
    #import ginger #Testing for NoModuleFound Exception
    #import giinger
except ModuleNotFoundError as exception_err:
    raise ModuleNotFoundError(f"{exception_err}")

#SimpleBots' bot life time = 10 seconds

class SimpleBots:
    enemy_objVars = { }
    
    enemy_spawnAttributes = { }
    enemies_directions = { }
    enemies_health = { }
    enemies_spawnCoords = { }
    enemies_SpawnStatus = False #True - Spawned, False - Not Spawned
    lifeTimer = None

    def __init__(self, **kwargs):


        self.health = kwargs.get('health', 10)
        self.speed = kwargs.get('speed', 1)
        self.quantity = kwargs.get('howmuch')
        self.model = 'cube'
        self.color = color.rgb(255, 50, 50)
        self.enemy_CanMove = { }
        self.scale = 2.5
        self.enemy_spawnAttributes = {
            "model":'models/test3.obj',
            "scale":self.scale,
            "collider":'box',
            "texture":"textures/enemies/enemy2.png"
        }
        
        for i in range(self.quantity):
            self.enemies_health[f'enemy{i}'] = self.health
            
            
    def spawn(self, *args):
        self.lifeTimer = time.time()
        print(self.lifeTimer)
        if len(self.enemy_objVars) is 5:
            self.enemy_objVars.clear
        """spawn """
        self.enemies_SpawnStatus = True
        for i in range(self.quantity):

            xPos = random.randint(-24, 24)
            zPos = random.randint(-24, 24)
            if (xPos <= 5) and (xPos >= -5):
                while (xPos < 5) and (xPos > -5):
                    xPos = random.randint(-24, 24)
            if (zPos < 5) and (zPos > -5):
                while (zPos < 5) and (zPos > -5):
                    zPos = random.randint(-24, 24)
            


            self.enemy_objVars[f'enemy{i}'] = Entity(
                **self.enemy_spawnAttributes, 
                position=(xPos, 2, zPos),
                #color=color.rgb(255, 90, 90),
                name=f"Enemy{i}"
            )

            self.enemies_spawnCoords[f'enemy{i}'] = (xPos, 2, zPos)
            self.enemy_CanMove[f'enemy{i}'] = True
            time.sleep(.01)


    def kill(self):
        if self.quantity == self.enemy_objVars:
            for i in range(self.quantity):
                self.enemy_objVars[f'enemy{i}'].disable()


    def getDirection(self):
        for i in range(self.quantity):
            #print(self.enemy_objVars[f'enemy{i}'].position.x) #For testing purposes
            self.enemies_directions[f'enemy{i}_x'] = None
            self.enemies_directions[f'enemy{i}_z'] = None

            if self.enemy_objVars[f'enemy{i}'].position.x > 0:
                self.enemies_directions[f'enemy{i}_x'] = True
            if self.enemy_objVars[f'enemy{i}'].position.x < 0:
                self.enemies_directions[f'enemy{i}_x'] = False
            
            if self.enemy_objVars[f'enemy{i}'].position.z > 0:
                self.enemies_directions[f'enemy{i}_z'] = True
            if self.enemy_objVars[f'enemy{i}'].position.z < 0:
                self.enemies_directions[f'enemy{i}_z'] = False
            
            if self.enemy_objVars[f'enemy{i}'].position.x == 0:
                self.enemies_directions[f'enemy{i}_x'] = None
            if self.enemy_objVars[f'enemy{i}'].position.x == 0:
                self.enemies_directions[f'enemy{i}_z'] = None
            

        #     print(f"X: {self.enemies_directions[f'enemy{i}_x']}, Z: {self.enemies_directions[f'enemy{i}_z']}")
        #     print("- - - - POS - - - -\n")
        # print(self.enemies_directions)
    def goCloser(self, isThread=False, **kwargs):
     if len(self.enemy_objVars) is 5:
        for i in range(self.quantity):
    
            if (self.enemy_CanMove[f'enemy{i}'] == True) and (self.enemies_SpawnStatus == True):

                #Both are positive
                if (self.enemy_objVars[f'enemy{i}'].position.x > 0) and (self.enemy_objVars[f'enemy{i}'].position.z > 0):
                    self.enemy_objVars[f'enemy{i}'].position += (-1, 0, -1)
                #Both are negative
                if (self.enemy_objVars[f'enemy{i}'].position.x < 0) and (self.enemy_objVars[f'enemy{i}'].position.z < 0):
                    self.enemy_objVars[f'enemy{i}'].position += (1, 0, 1)
                #X is negative & Z is positive
                if (self.enemy_objVars[f'enemy{i}'].position.x < 0) and (self.enemy_objVars[f'enemy{i}'].position.z > 0):
                    self.enemy_objVars[f'enemy{i}'].position += (1, 0, -1)
                #X is positive & Z is negative
                if (self.enemy_objVars[f'enemy{i}'].position.x > 0) and (self.enemy_objVars[f'enemy{i}'].position.z < 0):
                    self.enemy_objVars[f'enemy{i}'].position += (-1, 0, 1)
                #X is 0 & Z is positive
                if (self.enemy_objVars[f'enemy{i}'].position.x == 0) and (self.enemy_objVars[f'enemy{i}'].position.z > 0):
                    self.enemy_objVars[f'enemy{i}'].position += (0, 0, -1)
                #X is 0 & Z is negatve
                if (self.enemy_objVars[f'enemy{i}'].position.x == 0) and (self.enemy_objVars[f'enemy{i}'].position.z < 0):
                    self.enemy_objVars[f'enemy{i}'].position += (0, 0, 1)
                #X is positive & Z is 0
                if (self.enemy_objVars[f'enemy{i}'].position.x > 0) and (self.enemy_objVars[f'enemy{i}'].position.z == 0):
                    self.enemy_objVars[f'enemy{i}'].position += (-1, 0, 0)
                #X is negative & Z is 0
                if (self.enemy_objVars[f'enemy{i}'].position.x < 0) and (self.enemy_objVars[f'enemy{i}'].position.z == 0):
                    self.enemy_objVars[f'enemy{i}'].position += (1, 0, 0)
                #If its called from thread, moves of bots can move not together
                if isThread == True:
                    time.sleep(round(random.uniform(0.1, 0.3), 1))
     else: 
         pass





        
#Differences between SimpleBots & AdvancedBot are:
#SimpleBots contols group of bots, AdvancedBot controls one bot per assignment to variable
#
#

class AdvancedBot(Entity):
    bot = None

    def __init__(self, **kwargs):
        """
        Acceptable arguments are health, speed and spawnPos:
        - speed is measured in moves per second(MPS) set by deafult to 1
        - health is measuerd in attack it can survive set by deafult to 10
        - spawnPos is Vec3 variable, leave None if you want to set position to random
        """
        self.health = kwargs.get('health', 10)
        self.speed = kwargs.get('speed', 1)
        self.spawnPos = kwargs.get('spawnPos', None)
        if self.spawnPos == None:
            xPos = random.randint(-24, 24)
            zPos = random.randint(-24, 24)
            if (xPos <= 5) and (xPos >= -5):
                while (xPos < 5) and (xPos > -5):
                    xPos = random.randint(-24, 24)
            if (zPos < 5) and (zPos > -5):
                while (zPos < 5) and (zPos > -5):
                    zPos = random.randint(-24, 24)
            self.spawnPos = (xPos, 2, zPos)
        

        
    def spawn(self):
        self.bot = Entity(model='cube', color=color.rgb(255, 50, 50), position=self.spawnPos, scale=2)
        
    def rtp(self):
        """Random teleport for bot"""
        #self.bot.position = (random.randint(-10, 10), 2, random.randint(-10, 10))
        xPos = random.randint(-24, 24)
        zPos = random.randint(-24, 24)
        if (xPos <= 5) and (xPos >= -5):
            while (xPos < 5) and(xPos > -5):
                xPos = random.randint(-24, 24)
        if (zPos < 5) and (zPos > -5):
            while (zPos < 5) and (zPos > -5):
                zPos = random.randint(-24, 24)
        self.bot.position = (xPos, 2, zPos)
    
    
    def attack_goCloser(self):
        print(self.bot)
        if (self.bot.position.x > 0) and (self.bot.position.z > 0): #Both Positive
            print(1)
            self.bot.position += (-1, 0, -1)
        if (self.bot.position.x < 0) and (self.bot.position.z < 0): #Both Negative
            print(2)
            self.bot.position += (1, 0, 1)
        if (self.bot.position.x > 0) and (self.bot.position.z < 0): #X - Positive, Z - Negative
            print(3)
            self.bot.position += (-1, 0, 1)
        if (self.bot.position.x < 0) and (self.bot.position.z > 0): #X - Negative, Z - Positive
            print(4)
            self.bot.position += (1, 0, -1)
        if (self.bot.position.x == 0) and (self.bot.position.z > 0): #X - None, Z - Positive
            print(5)
            self.bot.position += (0, 0, -1)
        if (self.bot.position.x == 0) and (self.bot.position.z < 0): #X - None, Z - Negative
            print(6)
            self.bot.position += (0, 0, 1)
        if (self.bot.position.x > 0) and (self.bot.position.z == 0): #X - Positive, Z - None
            print(7)
            self.bot.position += (-1, 0, 0)
        if (self.bot.position.x < 0) and (self.bot.position.z == 0): #X - Negative, Z - None
            print(8)
            self.bot.position += (1, 0, 0)
    