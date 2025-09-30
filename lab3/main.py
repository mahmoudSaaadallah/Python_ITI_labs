from task1 import MathAutomation
from task2 import RegexLogCleaner
from task3 import DatetimeReminder
from task4 import ProductDataTransformer
from task5 import OSFileManager
from task6 import RandomDataGenerator
from task7 import DecoratorsTask
def main():
    
    ops = ["1- Math Automation","2- Regex Log Cleaner", "3- Datetime Reminder", "4- Product Data Transformer","5- OS File Manager","6- Random Data Generator"]
    
    print("Welcome To Our Tasks")
    for op in ops:
        print(op)
        
    userInput = int(input("Enter Your Input Please : "))
    
    if userInput == 1:
        MathAutomation()
    elif userInput == 2:
        RegexLogCleaner()
    elif userInput == 3:
        DatetimeReminder()
    elif userInput == 4:
        ProductDataTransformer()
    elif userInput == 5:
        OSFileManager()
    elif userInput == 6:
        RandomDataGenerator()
    else:
        print("Wrong Choice")


if __name__ == "__main__":
    main()