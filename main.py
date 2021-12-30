#Simple tower defense game.
#Copyright 2021-2022, Empezeeet, All rights reserved.

#If you dont have some of this packages game will crash with error saying you dont have specific package
#*----PROGRAMMER NOTES:
#NOTE 1: 'app = Ursina()' must be one of the first declarations. Longer time from start to declaration means more gliched game.
#NOTE 2: NEVER put these keys in IF in input(key) function:
#NOTE 2.1: ['meta', 'meta up', 'control', 'control up', 'alt', 'alt up']
#NOTE 3:
#*----PROGRAMMER NOTES

import time
import json
start = time.time()

#Reading Saves - Gamedata
with open("saves/_gamedata.json") as gamedata_f:
    gamedata = gamedata_f.read()

gamedata_Settings = json.loads(gamedata)
del gamedata, gamedata_f


try:
    import scripts.lights as __lights
    import scripts.logger as __logger
    import scripts.bots as __bots
    import scripts.exceptions as __exceptions
    import scripts.threads as __threads

    from ursina import *
    from ursina.prefabs.first_person_controller import FirstPersonController
    import threading 
    from datetime import datetime
    import os
    import random
    
    #DEBUG
    import platform
    import cpuinfo
    import psutil
except ModuleNotFoundError as error:
    raise Exception(str(error) + " was found")

app = Ursina()
app_process = psutil.Process(os.getpid())

run_date = datetime.now().strftime("%d\%m\%Y-%H:%M:%S")
runID = random.randint(10000, 99999)
#Reading Saves - LogData
with open("saves/__logdata.json") as logdata_f:
    logdata = logdata_f.read()
    logdata_IDs = json.loads(logdata)
    for i in logdata_IDs['used_IDs']:
        while runID != i:
            runID = random.randint(10000, 99999)
del logdata_f, logdata, logdata_IDs
            







#Reading Saves - Playerdata
with open("saves/playerdata.json") as playerdata_f:
    playerdata = playerdata_f.read()

player_data = json.loads(playerdata)
del playerdata, playerdata_f


#Archiving Logs
logs_folder = os.listdir("logs")
if (len(logs_folder) > 3):
    filename = None
    for i in logs_folder:
        print(i)
        if i.startswith("#"):
            filename = i
            break
    if filename != None:
        os.rename(("logs/" + str(filename)), ("logs/archived-logs/" + str(filename)))


del logs_folder
logger = __logger.Logger(f"logs/#{runID}-test-run-{run_date}.log", gamedata_Settings['app_allow_log_sysInfo'], runID)

try:
    if filename != None:
        del filename
except NameError:
    logger.FATAL("Zmienna 'filename' nie została zdefiniowana, co onznacza że archwizowanie plików .log zostało zakończone błędem")     
    raise __exceptions.NoObject("Zmienna 'filename' nie została zdefiniowana. Sprawdź logi aby dowiedzieć się dlaczego.")



logger.DEBUG("- - -  - - - - APP SETTINGS - - - - - - -")
logger.DEBUG(f"App Window Text: {gamedata_Settings['app_window_text']}")
logger.DEBUG(f"App Allow Log SysInfo: {gamedata_Settings['app_allow_log_sysInfo']}")
logger.DEBUG(f"App Max Framerate: {gamedata_Settings['app_max_framerate']}")
logger.DEBUG(f"App Fullscreen: {gamedata_Settings['app_fullscreen']}")
logger.DEBUG("- - - - - - - APP SETTINGS - - - - - - -\n\n")
del run_date, runID





logger.COSMETIC("- - - - - - - - - - - LOG - - - - - - - - - - -")
logger.INFO("Loaded all packages successfully. Starting App...")

logger.DEBUG(f"Time from start to end of loading essentials: {time.time()-start}s")


logger.INFO("Created window")

#*----World:
ground = Entity(model='cube', collider='mesh', scale=(50, 1, 50), color = color.rgb(98, 125, 47))
Sky = Sky()
logger.DEBUG("Sky and ground has been created.")
#*----World


#*----User Interface:
coordinates_Text = Text (parent=camera.ui,position= (-0.5, -0.4, 0.5),scale= 3,text=None)
memoryUsage_Text = Text(parent=camera.ui, position= (0.2, -0.4, 0.5), scale=3, text=None)
gameStatus_Text = Text (text=None, parent=camera.ui, color= color.red, scale=4, position=(-0.25, 0, 0))
logger.INFO("User Interface has been created")
#*----User Interface


#*----Player Settings:
player_platform = Entity(model='cube', collider='mesh', color=color.rgba(255, 255, 255, 0), position= (0, 50, 0), scale=(1, 0.01, 1))

player = FirstPersonController(position= (0, 50.02, 0), jump_height=gamedata_Settings['player_jump_height'], speed=gamedata_Settings['player_speed'])
player_health = gamedata_Settings['player_health']
logger.DEBUG("Player created.")
#*----Player Settings


#*----Window Settings:
window.title = gamedata_Settings['app_window_text'] # wyglada jak losowe znaki ale to bedzie Tower defense
window.fullscreen = gamedata_Settings['app_fullscreen']
logger.INFO("Window parameters has been updated.")
#*----Window Settings


#*----Enemies' Settings:
enemy_testor = Entity(
    model='sphere', collider='sphere',
    color=color.rgb(100, 255, 0), scale=(2.5, 2.5, 2.5)
)
enemy_testor.position = (10, 20, 10)
logger.DEBUG("Enemy tester entity has been created")

enemies = __bots.SimpleBots(health=10, speed=1, howmuch=5)

enemiesSpawned = False
advancedEnemy = __bots.AdvancedBots(speed=1, health=10, spawnPos=None)
#*----Enemies' Settings
memoryUsage_Text.disable()
coordinates_Text.disable()

def input(key):
    logger.DEBUG(f"User pressed key: {key}")
    if key == 'b':
        player.position = (0, 7, 0)
    if key == 'f':
        player.speed += 2
    if key == 'g':
        player.speed -= 2
    if key == 'r':
        advancedEnemy.attack_goCloser()
    if key == 'x':
        logger.INFO("Exited app as userExit()")
        app.userExit()
    if key == 'e':
        enemies.goCloser()
        
    if key == 'q':
        enemiesSpawned = True
        enemies.spawn(None)
        
    if key == '[':
        enemies_spawnTest(name="EnemiesSpawnTest").start()
    if key == "o":
        Sky.color = color.white
    if key == "p":
        Sky.color = color.black
    if key == "v":
        advancedEnemy.spawn()
    if key == "b":
        pass
    if key == "f3":
        #Show Debug Info
        memoryUsage_Text.enabled = not memoryUsage_Text.enabled
        coordinates_Text.enabled = not coordinates_Text.enable

        

        

def update():
    coordinates_Text.text = f"X{round(player.position.x, 2)} Y{round(player.position.y, 2)} Z{round(player.position.z, 2)}"
    ram_usage = int(app_process.memory_info().rss) * 0.000001
    memoryUsage_Text.text = f"RAM: {str(round(ram_usage, 0))}MB"
    if enemiesSpawned:
        for i in enemies.enemy_objVars:
            if enemies.enemy_objVars[i].position.xz == (0, 0):
                enemies.enemy_objVars[i].disable()
                del enemies.enemy_objVars[i]
                # gameOver()
                # break
def gameOver():
    logger.INFO("[- - - - - - GAME OVER - - - - -]")
    gameStatus_Text.text = "Game Over!"

class enemies_spawnTest(threading.Thread):
    def run(self):
        for i in range(1000):
            enemies.spawn(None)
            gameStatus_Text.text = f"Iteration no. {i}"
            time.sleep(.1)




# class enemy1_AI(Thread):
#     def run(self):
#         while True:
#             #this function should update once a second
#             enemy1.attack_goCloser()
#             logger.INFO("Enemy1 moved closer.")
#             print(enemy1.bot.position)
#             if enemy1.bot.position.xz == (0, 0):
#                 gameStatus_Text.text = "Game Over!"
#                 break
#             time.sleep(1)
class enemiesAI(threading.Thread):
    pass    

class updateAfterSecond(threading.Thread):
    def run(self):
        #enemy1.bot.color = color.random_color()
        time.sleep(1)


end = time.time()
logger.INFO(f"Loading done in {end - start}s")
logger.COSMETIC("- - - - End of Loading LOG     ")

del start, end

app.run()
logger.FATAL("This shouldn't show up. If you can see this in logs you should check for gliches")