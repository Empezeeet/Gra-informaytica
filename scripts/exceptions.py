#This is file has some custom exceptions to make code & errors cleaner

class Error(Exception):
    """Base class for other exceptions"""
    pass

class WrongValue(Error):
    """Raised when variable has wrong value."""
    pass

class NoObject(Error):
    """Raised when program wants to relate to object that doesn't exist or object has no value (NONE)"""
    pass

class Unknown(Error):
    """Unknown Error. You should look at logs and traceback"""
    pass

class OutOfMemory(Error):
    """Out of memory."""
    pass

class UnknownModule(Error):
    """Raises when script wants to import package that is not installed."""
    pass    