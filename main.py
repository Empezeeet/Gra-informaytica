from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from scripts.bots import *
import time
import threading


app = Ursina()
ground = Entity(model='cube', collider='mesh', scale=(100, 1, 100))
ground.color = color.rgb(98, 125, 47)
Sky()







player = FirstPersonController()
player.position = (0, 10, 0)
player_platform = Entity(model='cube', collider='mesh', color=color.rgb(255, 255, 255), position= (0, 6, 0), scale=(2, 0, 2))

player.jump_duration = 1
player.jump_height = 0
player.speed = 0







window.borderless = False


    



enemy_testor = Entity(model='sphere', collider='sphere', color=color.rgb(100, 255, 0), scale=(2.5, 2.5, 2.5))
enemy_testor.position = (10, 2, 10)



window.title = "TDfns" # wyglada jak losowe znaki ale to bedzie Tower defense
window.fullscreen = False



enemy1 = Bots(10, 2)
enemy1.spawn(position= (10, 2, 5))

def input(key):
    if key == 'b':
        player.position = (0, 7, 0)
    if key == 'f':
        player.speed += 2
    if key == 'g':
        player.speed -= 2
    if key == 'r':
        enemy1.rtp()
    if key == 'x':
        app.userExit()
    if key == 'e':
        print( 'X:' + str(player.position.x))
        print( 'Y:' + str(player.position.y))
        print( 'Z:' + str(player.position.z))
    if key == 'q':
        sat_thrd = threading.Thread(target=enemy1.start_attacking_tower())
        sat_thrd.start()
        
    if key == 'z':
        print( 'X:' + str(enemy1.bot.position.x))
        print( 'Z:' + str(enemy1.bot.position.z))
        
        
        

def update():
    pass




app.run()