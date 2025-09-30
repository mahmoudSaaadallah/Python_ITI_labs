import math
import time
import re
from datetime import datetime
from task7 import DecoratorsTask
@DecoratorsTask
def MathAutomation():
    try:
        numbers_input = input("Enter multiple numbers (comma-separated): ")
        numbers = []
        for x in numbers_input.split(','):
            clean_number = x.strip()
            numbers.append(int(clean_number))  
            
        with open("MathAutomation.txt", "w") as file:
        
            for num in numbers:
                f = math.floor(num)
                c = math.ceil(num)
                r = math.sqrt(abs(num))
                a = 3.14 * num * num
                file.write(f"Number: {num}\n")
                file.write(f"Floor: {f}\n")
                file.write(f"Ceil: {c}\n")
                file.write(f"Square Root: {r}\n")
                file.write(f"Circle Area : {a}\n")
        
        print("File contents: ")
        with open("MathAutomation.txt", "r") as file:
            print(file.read())
            
    except Exception as e:
    print("un expected error: ", e)
    