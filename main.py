#Simple tower defense game. Packages that you need:
#Copyright 2021-2022, Empezeeet, All rights reserved.

#If you dont have some of this packages game will crash with error saying you dont have specific package()
#*----PROGRAMMER NOTES:
#NOTE 1: 'app = Ursina()' must be one of the first declarations. Longer time from start to declaration means more gliched game.
#NOTE 2: NEVER put these keys in IF in input(key) function:
#NOTE 2.1: ['meta', 'meta up', 'control', 'control up', 'alt', 'alt up']
#NOTE 3: SimpleBots should be used as ClassicEnemy while AdvancedBots should be as Bosses
# TODO: After randomDeathTime is over, new spawned enemies are not moving (#7)
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
        import scripts.logger as __logger
        import scripts.bots as __bots
        import scripts.exceptions as __exceptions
    #UrsinaEngine Packages
        print("prze import")
        from ursina import *
        from ursina.prefabs.first_person_controller import FirstPersonController
        import ursina.prefabs.memory_counter as EngineMC
        import ursina.prefabs.editor_camera as EngineECAM
    #Other Packages
        import threading 
        from datetime import datetime
        import os
        import random
        

except ModuleNotFoundError as error:
    raise Exception(str(error) + " was found")

print("po import")
window.forced_aspect_ratio = 16/9
camera.fov = 90


if __name__ == "__main__":
    app = Ursina(vsync=True, borderless=False, fullscreen=False) #VSync must be set to True else Game would use More (unnecessary) RAM, CPU, GPU
                         #VSync sets maxFramerate to your monitor Hz Value
                         # 60Hz == max 60FPS
                         # 75Hz == max 75FPS
                         # 144Hz == max 144FPS
else:
    exit()
print("po deklaracji")
player = FirstPersonController(position= (0, 50.02, 0), jump_height=0, speed=0)


run_date = datetime.now().strftime("%d\%m\%Y-%H:%M:%S")
runID = random.randint(10000, 99999)
#Reading Saves - LogData

with open("saves/_logdata.olVar", mode="r+") as olvFile:
    data = olvFile.readlines()
    for i in range(len(data)):
        if data[i] == runID:
            while data[i] != runID:
                runID = random.randint(10000, 99999)
    runID_str = str(runID) + "\n"
    olvFile.write(runID_str)
del data, runID_str, olvFile


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

logger = __logger.Logger(f"logs/#{runID}-test-run.log", gamedata_Settings['app_allow_log_sysInfo'], runID)

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

try:
    #Logging App Settings
        logger.INFO(f"Time: {run_date}\n")
        logger.DEBUG("- - -  - - - - APP SETTINGS - - - - - - -")
        logger.DEBUG(f"App Window Text: {gamedata_Settings['app_window_text']}")
        logger.DEBUG(f"App Allow Log SysInfo: {gamedata_Settings['app_allow_log_sysInfo']}")
        logger.DEBUG(f"App Max Framerate: {gamedata_Settings['app_max_framerate']}")
        logger.DEBUG(f"App Fullscreen: {gamedata_Settings['app_fullscreen']}")
        logger.DEBUG("- - - - - - - APP SETTINGS - - - - - - -\n\n")
        del run_date, runID
except:
    pass





logger.COSMETIC("- - - - - - - - - - - LOG - - - - - - - - - - -")
logger.INFO("Loaded all packages successfully. Starting App...")

logger.DEBUG(f"Time from start to end of loading essentials: {time.time()-start}s")


logger.INFO("Created window")

#*----World:
ground = Entity(name="GroundEntity-XDAP", model='cube', collider='mesh', scale=(50, 1, 50), color = color.rgb(98, 125, 47))
Sky = Sky()
logger.DEBUG("Sky and ground has been created.")
#*----World


#*----User Interface:
coordinates_Text = Text (parent=camera.ui,position= (-0.5, -0.4, 0.5),scale= 3,text=None)
memoryUsage_Text = Text(parent=camera.ui, position= (0.2, -0.4, 0.5), scale=3, text=None)
gameStatus_Text = Text (text="", parent=camera.ui, color=color.red, scale=4, position=(-0.25, 0, 0))
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

logger.DEBUG("Player created.")
#*----Player Settings

#editorCamera = EngineECAM.EditorCamera(rotation_smoothing=2, enabled=0, rotation=(30, 30, 0))






#*----Window Settings:
window.title = gamedata_Settings['app_window_text'] # wyglada jak losowe znaki ale to bedzie Tower defense


window.exit_button.visible = False

logger.INFO("Window parameters has been updated.")
#*----Window Settings


#*----Enemies' Settings:
enemy_testor = Entity(
    model='sphere',
    color=color.rgb(10, 255, 100),
    scale=1
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

canMoveCamera = False


logger.DEBUG("AdvancedEnemy Entity has been assigned")
def input(key):
    logger.DEBUG(f"User pressed key: {key}")
    if key == "escape":
        UIPanelEnableDisable()
    if key == 'l':
        logger.INFO("Exited app as application.quit())")
        application.quit()
    if key == '[':
        breakpoint()
    if key == "f3":
        collidersStatus = False
        #Show Debug Info
        if enemies.enemies_SpawnStatus == True:
            for i in range(enemies.quantity):
                enemies.enemy_objVars[f'enemy{i}'].collider.visible = not collidersStatus
            collidersStatus = not collidersStatus
        memoryUsage_Text.enabled = not memoryUsage_Text.enabled
        coordinates_Text.enabled = not coordinates_Text.enabled
    if key == "j":
        player.speed = 5

SBK_threadRunning = False
ETAI_threadRunnning = False
#Thread Classes


randomDeathTime = random.randint(5, 15)

class enemiesTestingAI(threading.Thread):
    def run(self):
        global ETAI_threadRunnning
        global gameStatus_Text
        global enemiesSpawned
        global randomDeathTime
        ETAI_threadRunnning = True
        try:
            randomDeathTime = random.randint(5, 15)
            print("RandomDeathTime: ", randomDeathTime)
        except:
            randomDeathTime = 10
        while enemies.enemies_SpawnStatus:
            enemies.goCloser(True)
            if (time.time() - enemies.lifeTimer) >= randomDeathTime:
                logger.DEBUG("Killing Enemies")
                enemiesSpawned = False
                enemies.enemies_SpawnStatus = False
                enemies.kill()
            
    def terminate(self):
        self._running = False



class SimpleBotsKiller(threading.Thread):
    def run(self):
        global SBK_threadRunning
        global GameOver
        SBK_threadRunning = True
        # Działa Nie Dotykać pod żadnym pozorem
        #                           - Empezeeet
        # v2 po czyszczeniu
        while True:
            if (enemies.enemies_SpawnStatus == True) and (mouse.hovered_entity is not None):
                for i in range(enemies.quantity):
                    if mouse.hovered_entity.name == f"Enemy{i}":
                        enemies.enemy_CanMove[f'enemy{i}'] = False
                    else:
                        enemies.enemy_CanMove[f'enemy{i}'] = True
            time.sleep(0.01)
    def terminate(self):
        self._running = False



class gameMaster(threading.Thread):
    SBKThread = SimpleBotsKiller(name="SBK-Thread")
    ENAIThread = enemiesTestingAI(name="ENAI-Thread")

    def run(self):
        global gameStatus_Text
        global randomDeathTime
        global enemiesSpawned
        gameWon = False
        # Countdown Timer
        for i in range(5):
            gameStatus_Text.text = f"Starting in {5-i} seconds!"
            time.sleep(1)

        gameStatus_Text.text = ""
        for i in range(gamedata_Settings['game_max_waves']):
            self.wave()
            if GameOver:
                gameOver_func()
                break
            time.sleep(randomDeathTime)
            enemies.kill()
            enemiesSpawned = False
            enemies.enemies_SpawnStatus = False
            if i == gamedata_Settings['game_max_waves']:
                gameWon = True
            time.sleep(.2)
        if GameOver is True:
            gameOver_func()
        elif gameWon:
            self.SBKThread.terminate()
            self.ENAIThread.terminate()
            gameWon_func()

            


    def wave(self):
        global enemiesSpawned
        if enemies.enemies_SpawnStatus == False:
                enemies.spawn()
                enemiesSpawned = True
                enemies.enemies_SpawnStatus = True
        if SBK_threadRunning is False:
            try:
                self.SBKThread.start()
            except:
                logger.FATAL("Cannot Run SBKThread!")
                breakpoint()
        if ETAI_threadRunnning is False:
            try:
                self.ENAIThread.start()
            except:
                logger.FATAL("Cannot Run ETAIThread!")
                breakpoint()
    
       
    
        

            


MC = EngineMC.MemoryCounter()


def gameWon_func():
    gameStatus_Text.text = "You Won!"
    enemies.kill()
    enemiesSpawned = False
    enemies.enemies_SpawnStatus = False
    


def gameOver_func():
    global enemiesSpawned
    gameStatus_Text.text = 'Game Over'
    enemies.kill()
    enemiesSpawned = False
    enemies.enemies_SpawnStatus = False




def update():
    coordinates_Text.text = f"X{round(player.position.x, 2)} Y{round(player.position.y, 2)} Z{round(player.position.z, 2)}"
    global GameOver
    global enemiesSpawned
    if enemiesSpawned:
        if len(enemies.enemy_objVars) is enemies.quantity:
            for i in range(enemies.quantity):
                if enemies.enemy_objVars[f'enemy{i}'].position.xz == (0, 0):
                    enemies.enemy_objVars[f'enemy{i}'].scale = 0
                    GameOver = True
                    break
            if GameOver:
                gameOver_func()

def startGame():
    logger.INFO("Player started game via UIPanel")
    UIPanelEnableDisable()
    gameStatus_Text.color = color.red
    gameStatus_Text.text = ""
    logger.DEBUG("GameMaster-Thread has been started")
    gameMaster(name="GameMaster-Thread").start()

def userExit():
    logger.INFO("User exited the game")
    application.quit()

UIPanel = WindowPanel(
    enabled=False,
    popup=True,
    title="Menu",
    content=[
        Button(text="Start Game", on_click=startGame, color=color.rgb(50, 200, 100)),
        Button(text='Exit Game', on_click=userExit, color=color.rgb(255, 100, 100))
    ]
)



def UIPanelEnableDisable():
    player.enabled = not player.enabled
    UIPanel.enabled = not UIPanel.enabled

UIPanel.bg.on_click = UIPanelEnableDisable

logger.INFO(f"Loading done in {time.time() - start}s")
logger.COSMETIC("- - - - End of Loading LOG    \n\n ")

del start
app.run()

logger.FATAL("This shouldn't show up. If you can see this in logs you should check for gliches")
