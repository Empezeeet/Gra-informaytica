
from copy import Error
from types import ModuleType
from typing import Optional
from numpy import ERR_RAISE

from ursina import sequence


try:
    from ursina import *
    import math
    import random
    import time
    import threading
    from threading import Thread
    #import ginger #Testing for NoModuleFound Exception
    #import giinger
except ModuleNotFoundError as exception_err:
    raise ModuleNotFoundError(f"{exception_err}")


class Lights():
    light = None
    def __init__(self, position, shadows, parent):
        self.position = position
        self.shadows = shadows
        light = PointLight(parent=parent, position=position, shadows=shadows)
    
    def changePos(self, position: Vec3):
        self.light.position = position

    def changeShadows(self, shadows: bool):
        self.light.shadow = shadows
    def changeParent(self, parent):
        self.light.parent = parent
    
    

    
