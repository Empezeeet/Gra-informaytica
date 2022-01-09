#Mistrz gry, czyli skrypt który odpowiada za gre i jej przebieg




try:
    import random
    import math
    import threading
    from ursina import *
    
    from scripts.logger import Logger as __log
    import scripts.exceptions as __exceptions
except:
    raise ModuleNotFoundError("Module not found! (gameMaster.py)")

class GameMaster(threading.Thread):
    def __init__(self, **kwargs) -> None:
        pass