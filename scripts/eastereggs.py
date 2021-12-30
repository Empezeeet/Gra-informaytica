#Easter egg classes
#Copyright 2021-2022, Empezeeet, All rights reserved

#*----PROGRAMMER NOTES:
#NOTE 1: 
#*----PROGRAMMER NOTES


#Importing packages
try:
    import scripts.exceptions as __except
    
    import time
    import threading
    import math
    import random
except ModuleNotFoundError as err:
    raise __except.UnknownModule(err)
    
