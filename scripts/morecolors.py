#More Colors for UrsinaEngine Color class!
#Copyright 2022, Empezeeet, All Rights Reserved


#!WORK IN PROGRESS
#!In 100% of cases this script won't work
try:
    from ursina.color import Color
    import random
    import colorsys
    import threading
    import time
    from panda3d.core import Vec4
    from math import floor
    #import scripts.exceptions as __exceptions
except ModuleNotFoundError as err:
    raise ModuleNotFoundError(err)

def hsv(h, s, v, a=1):
    return Color(colorsys.hsv_to_rgb((h / 360) - floor(h / 360), s, v) + (a,))

color = hsv

class MoreColors:
    def __init__(self, **kwargs):
        pass

    class rainbow(threading.Thread):
        def __init__(self):
            self.r = 0
            self.g = 0
            self.b = 0
            for i in range(255):
                self.r += i
                color = Color(self.r, self.g, self.b, a=255)
            for i in range(255):
                self.r -= i
                self.g += i
                color = Color(self.r, self.g, self.b, a=255)
            for i in range(255):
                self.g -= i
                self.b += i
                color = Color(self.r, self.g, self.b, a=255)
            
