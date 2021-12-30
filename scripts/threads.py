#Threads for Simple Tower Defense game.
#Copyright 2021-2022, Empezeeet, All Rights Reserved

import time
startTimer = time.time()
try:
    import threading
    
    from datetime import datetime
    import os
    import random
    import scripts.exceptions as __exceptions
    import math
except ModuleNotFoundError as err:
    raise ModuleNotFoundError(err)



