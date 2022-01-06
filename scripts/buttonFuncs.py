#Functions for buttons for game.

try:
    import ursina as engine
    import random
    import threading
    import time

    import scripts.exceptions as __exceptions
except:
    raise Exception("Module Not Found!")


class Functions:
    def __init__(self) -> None:
        pass

    class AppExit:
        def __init__(self) -> None:
            engine.application.quit()
    class showCredits:
        def __init__(self) -> None:
            pass
        
