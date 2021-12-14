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

player_origin = player.world_position
player_hitInfo = raycast(player_origin,direction=(1, 1, 1), ignore=(player,), distance=5, debug=True)






window.borderless = False
cursor = Cursor()
cursor.visible = False


    



enemy_testor = Entity(model='sphere', collider='sphere', color=color.rgb(166, 255, 27), scale=(2.5, 2.5, 2.5))
enemy_testor.position = (10, 2, 10)



window.title = "TDfns" # wyglada jak losowe znaki ale to bedzie Tower defense
#audio = Audio("audio/Lo")

#audio.play()
#audio.volume = 0.5
window.fullscreen = False



enemy1 = Bots(10, 2)
enemy1.spawn(position= (10, 2, 5))




enable_enemyAI = True
def enemy_walkingAI(): #Ta funkcja jest dodawana do nowego wątku procesora. 
    while enable_enemyAI:
        Bots.bot.position = Bots.bot.position - (1, 0, 1)
        time.sleep(1)

def enable_enemyWalkingAI():
    try:
        enemy1_Ai = threading.Thread(target=enemy_walkingAI)
        enemy1_Ai.start()
    except:
        print('ERROR enemy1_AI exception')
        app.getExitErrorCode()
    



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
    if key == 'q':
        enable_enemyWalkingAI()
        

def update():
    pass




app.run()