import time
import math
import re
from datetime import datetime

def DecoratorsTask(func):
    def wrapper(*args):
        
        start = time.time()
        result = func(*args)
        end = time.time()
        line = f"\n{func.__name__} Run in time: {end - start}"
        print(line)
        with open("execution_log.txt", "a") as file:
            file.write(line)
            
        return result

    return wrapper