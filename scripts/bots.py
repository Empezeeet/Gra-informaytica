#Simple Bots' AI Script
#Copyright 2021-2022, Empezeeet, All Rights Reserved






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

class SimpleBots:
    enemy_objVars = { }
    enemy_spawnAttributes = { }
    enemies_directions = { }
    def __init__(self, **kwargs):
        self.health = kwargs.get('health')
        self.speed = kwargs.get('speed', 1)
        self.quantity = kwargs.get('howmuch')
        self.model = 'cube'
        self.color = color.rgb(255, 50, 50)
        self.scale = 2.5
        self.enemy_spawnAttributes = {
            "model":self.model,
            "scale":self.scale,
        }
    def spawn(self, dictPosition):
        """dictPosition (best logic name) - you need to type positions of bots in dict """
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
                position=(xPos, 1, zPos),
                color=color.random_color()
            )
    def testing(self):
        print(str(self.getDirection()) + "\n")
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
    def goCloser(self):
        for i in range(self.quantity):
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








        
    
class AdvancedBots():
    bot = Entity()
    bot_health = None

    def __init__(self, **kwargs):
        """
        Acceptable arguments are health, speed and spawnPos:
        - speed is measured in moves per second(MPS) set by deafult to 1
        - health is measuerd in attack it can survive set by deafult to 10
        - spawnPos is Vec3 variable, leave None if you want to set position to random"""
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

        
    def spawn(self, **kwargs):
        bot = Entity(model='cube', collider='box', color=color.red, position=self.spawnPos)
             
    
    def takeDamage(self, howMuch=1):
        print(f"Wow! dat hurts! {self.health}")
        self.health -= howMuch
        self.bot_health = self.health
        if self.health <= 0:
            self.bot.color = color.rgb(255, 100, 150)
        
    def rtp(self):
        """Random teleport for bot"""
        self.bot.position = (random.randint(-10, 10), 2, random.randint(-10, 10))
    
    def get_direction(self, wichone: str):
        
        x_direction = None # True = (+) False = (-) None = 0 (In This case its just for creating variable)
        z_direction = None # True = (+) False = (-) None = 0 (In This case its just for creating variable)

        if self.bot.position.x > 0:
            x_direction = True
        if self.bot.position.x < 0:
            x_direction = False
        if self.bot.position.z > 0:
            z_direction = True
        if self.bot.position.z < 0:
            z_direction = False
        
        if self.bot.position.x == 0:
            x_direction = None
        if self.bot.position.z == 0:
            z_direction = None
        
        try:
            if wichone == 'x':
                return x_direction
            if wichone == 'z':
                return z_direction
            if wichone == 'xz':
                xz = [x_direction, z_direction]
                return(xz)
            if (wichone == None) or (wichone != "x") or (wichone != "z") or (wichone != "xz"):
                raise ValueError()
        except ValueError:
            raise __exceptions.WrongValue("Value 'wichone' is not defined properly!\n Accepted values are:\n-x,\n-xz,\n-xz")

    def attack_goCloser(self):
        x = self.get_direction('x')
        z = self.get_direction('z')

        if (x == True) and (z == True): #All positive
            self.bot.position -= (1, 0, 1)
        if (x == False) and (z == False): #All negative
            self.bot.position += (1, 0, 1)
        if (x == True) and (z == False): # X is positive and Z is negative
            self.bot.position += (-1, 0, 1)
        if (x == False) and (z == True): # X is negative and Z is positive
            self.bot.position += (1, 0, -1)
        if (x == None) and (z == True):
            self.bot.position -= (0, 0, 1)
        if (x == None) and (z == False):
            self.bot.position += (0, 0, 1)
        if (x == True) and (z == None):
            self.bot.position -= (1, 0, 0)
        if (x == False) and (z == None):
            self.bot.position += (1, 0, 0)
