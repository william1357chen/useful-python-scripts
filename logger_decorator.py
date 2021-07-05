import logging
import inspect
import os

LOGFILENAME = 'my_log.log'
logging.basicConfig(filename=LOGFILENAME, format='%(asctime)s %(message)s',
                        level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p')

DEBUG_LINE = "The function '{}()' in script '{}.py' is called by function '{}()'"

# In the programs you intend to log, do the following
# from logger_decorator import log_func

# Above the function you want to log, add the decorator
# @log_func

def log_func(func):
    def log_wrapper(*args, **kwargs):
        logging.debug(DEBUG_LINE.format(func.__name__, func.__module__, inspect.stack()[1][3]))
        return func(*args, **kwargs)
    return log_wrapper
