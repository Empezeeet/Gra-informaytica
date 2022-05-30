#Logging module.

if __name__ == "__main__":
    raise RuntimeError("This file should be imported")



sr = True

try:
    import scripts.exceptions
    from datetime import datetime
    import time
    import os
    import threading
    import platform
    import cpuinfo
except ModuleNotFoundError as err:
    raise ModuleNotFoundError(err)

class Logger(threading.Thread):
    
    def __init__(self, filename, allowSysInfo, runID):
        self.sr = True
        self.filename = filename
        file = open(file=str(filename), mode='a')
        file.close()
        if allowSysInfo == 1:
            self.DEBUG("- - - - - - - SYSTEM INFO - - - - - - -")
            self.DEBUG(f"System: {platform.platform()}")
            self.DEBUG(f"Processor: {cpuinfo.get_cpu_info()['brand_raw']}")
            self.DEBUG(f"Node: {platform.node()}")
            self.DEBUG(f"Version: {platform.version()}")
            self.DEBUG(f"RunID: {runID}")
            self.DEBUG("- - - - - - - SYSTEM INFO - - - - - - -\n")

    
        
    def DEBUG(self, message):
        self.write_message("DEBUG", message + "\n")
    def INFO(self, message):
        self.write_message("INFO", message + "\n")
    def WARN(self, message):
        self.write_message("WARN", message + "\n")
    def ERROR(self, message):
        self.write_message("ERROR", message + "\n")
    def FATAL(self, message):
        self.write_message("FATAL", message + "\n")
    def COSMETIC(self, message):
        self.write_message("COSM ", message + "\n")
    
    def write_message(self, level, message):
        file = open(file=self.filename, mode='a+')

        file.write(f'{level} @ {datetime.now().strftime("%H:%M:%S")} - {message}')
        file.close()

    def update():
        pass