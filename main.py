#Simple tower defense game.
#Copyright 2021-2022, Empezeeet, All rights reserved.

#If you dont have some of this packages game will crash with error saying you dont have specific package()
#*----PROGRAMMER NOTES:
#NOTE 1: 'app = Ursina()' must be one of the first declarations. Longer time from start to declaration means more gliched game.
#NOTE 2: NEVER put these keys in IF in input(key) function:
#NOTE 2.1: ['meta', 'meta up', 'control', 'control up', 'alt', 'alt up']
#NOTE 3: SimpleBots should be used as ClassicEnemy while AdvancedBots should be as Bosses
#*----PROGRAMMER NOTES


import time
import json
start = time.time()
gamedata_Settings = None
FATAL_dataToLog = {} # Only FATAL
#Reading Saves - Gamedata
try:
    with open("saves/_gamedata.json") as gamedata_f:
        gamedata = gamedata_f.read()

    gamedata_Settings = json.loads(gamedata)
    del gamedata, gamedata_f
except:
    FATAL_dataToLog['msg1'] = "GameSettings cannot be imported! Game may not work properly!"
    gamedata_Settings = None

try:
    #Own Scripts
   # import scripts.lights as __lights
    import scripts.logger as __logger
    import scripts.bots as __bots
    import scripts.exceptions as __exceptions
    import scripts.threads as __threads
    #Other  
    from ursina import *
    from ursina.prefabs.first_person_controller import FirstPersonController
    import ursina.prefabs.memory_counter as EngineMC
    import threading 
    from datetime import datetime
    import os
    import random
except ModuleNotFoundError as error:
    raise Exception(str(error) + " was found")

if __logger.sr is True:
    app = Ursina(vsync=True, show_ursina_splash=False) #VSync must be set to True else Game would use More (unnecessary) RAM, CPU, GPU
                         #VSync sets maxFramerate to your monitor Hz Value
                         # 60Hz == max 60FPS
                         # 75Hz == max 75FPS
                         # 144Hz == max 144FPS




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
if gamedata_Settings == None:
    gamedata_Settings = {
        "app_allow_log_sysInfo":0
    }
logger = __logger.Logger(f"logs/#{runID}-test-run-{run_date}.log", gamedata_Settings['app_allow_log_sysInfo'], runID)

if len(FATAL_dataToLog) > 0:
    for i in FATAL_dataToLog:
        logger.FATAL(FATAL_dataToLog[i])
del FATAL_dataToLog


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
player_platform = Entity(model='cube', collider='box', color=color.rgb(255, 255, 255), scale=(0.01, 0.01, 0.01))

if gamedata_Settings['app_debug_mode'] == "True":
    player_platform.position = (0, 50, 0)
elif gamedata_Settings['app_debug_mode'] == "False":
    player_platform.position = (0, 20, 0)
else:
    logger.FATAL("Pobieranie danych gry przebiegło nieprawidłowo.")
    raise __exceptions.ImportingError("Game settings not loaded properly!")

player = FirstPersonController(position= (0, 50.02, 0), jump_height=gamedata_Settings['player_jump_height'], speed=gamedata_Settings['player_speed'])
player_health = gamedata_Settings['player_health']
logger.DEBUG("Player created.")
#*----Player Settings



#*----Window Settings:
window.title = gamedata_Settings['app_window_text'] # wyglada jak losowe znaki ale to bedzie Tower defense
window.fullscreen = gamedata_Settings['app_fullscreen']
window.exit_button.visible = False

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

#*----Enemies' Settings
memoryUsage_Text.disable()
coordinates_Text.disable()
logger.INFO("DebugMode UI Labels has been Disabled")



GameOver = False

GameScore = 0

   
gameStatus_Text.color = color.black
gameStatus_Text.text = "Press R to start game"

logger.DEBUG("AdvancedEnemy Entity has been assigned")
def input(key):
    logger.DEBUG(f"User pressed key: {key}")

    if key == 'r':
        gameStatus_Text.color = color.red
        gameStatus_Text.text = ""
        gameMaster(name="GameMaster-Thread").start()



    if key == 'b':
        player.position = (0, 50.05, 0)
    if key == 'f':
        player.speed += 2
    if key == 'g':
        player.speed -= 2
    if key == 'x':
        logger.INFO("Exited app as userExit()")
        app.userExit()
    if key == 'e':
        enemiesTestingAI().start()
        
    if key == '9':
        if SBK_threadRunning is not True:
            SimpleBots_Killer(name="SBKiller-Thread").start()
    if key == 'q':
        
        enemies.spawn(None)
    if key == '[':
        breakpoint()
    if key == "o":
        Sky.color = color.white
    if key == "p":
        Sky.color = color.black
    if key == "f3":
        collidersStatus = False
        #Show Debug Info
        if enemies.enemies_SpawnStatus == True:
            for i in range(enemies.quantity):
                enemies.enemy_objVars[f'enemy{i}'].collider.visible = not collidersStatus
            collidersStatus = not collidersStatus
        memoryUsage_Text.enabled = not memoryUsage_Text.enabled
        coordinates_Text.enabled = not coordinates_Text.enabled

SBK_threadRunning = False

#Thread Classes
        
class enemiesTestingAI(threading.Thread):
    def run(self):
        randomDeathTime = random.randint(11, 16)
        while True:
            enemies.goCloser(True)
            print(randomDeathTime)
            if time.time() - enemies.lifeTimer >= randomDeathTime:
                print("wow")
                for i in range(enemies.quantity):
                    enemies.enemy_objVars[f'enemy{i}'].collider = None
                    enemies.enemy_objVars[f'enemy{i}'].scale = 0
                    enemies.enemy_objVars[f'enemy{i}'].disable()
                    
                enemies.enemies_SpawnStatus = False
                break

class SimpleBots_Killer(threading.Thread):
    def run(self):
        SBK_threadRunning = True
        try:
            while True:
                if enemies.enemies_SpawnStatus == True:
                    print("Enemies are spawned!")
                    if mouse.hovered_entity is not None:
                        print("MouseHoveredEntity is not None!")
                        for i in range(enemies.quantity):
                                if mouse.hovered_entity.name == f"Enemy{i}":
                                    print("MouseHoveredEntity is Enemy!") 
                                    while mouse.hovered_entity.name == f"Enemy{i}":
                                        enemies.enemy_CanMove[f'enemy{i}'] = False
                                        print("Enemy's canMove Parameter set to False!")
                                        time.sleep(.75)
                                if mouse.hovered_entity.name != f'Enemy{i}':
                                    enemies.enemy_CanMove[f'enemy{i}'] = True
                time.sleep(.75)
        except:
            logger.ERROR("Exception Occured! in 99% of cases this is AttributeError. If it really is you don't need to worry!")

class gameMaster(threading.Thread):
    def run(self):
        pass

class NewUpdate(threading.Thread):
    def run(self):
        while True:
            time.sleep(1)

MC = EngineMC.MemoryCounter()


def update():
    coordinates_Text.text = f"X{round(player.position.x, 2)} Y{round(player.position.y, 2)} Z{round(player.position.z, 2)}"

end = time.time()
logger.INFO(f"Loading done in {end - start}s")
logger.COSMETIC("- - - - End of Loading LOG     ")







del start, end
app.run()
logger.FATAL("This shouldn't show up. If you can see this in logs you should check for gliches")


