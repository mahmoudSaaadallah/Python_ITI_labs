def sortNumbers():
    while True:
        list1 = []
        
        while True:
            print("Enter The Number Or Done To Get The Result")
            n = input()
            if n.isdigit() == False:
                if n == "done":
                    break
                print("Invalid Number")
                continue
            n = int(n)
            list1.append(n)
            
        list1.sort()
        print(f"Sort In Ascending Order : {list1}")
        list1.sort(reverse = True)
        print(f"Sort In descending Order : {list1}")
        try_again = input("Try Again ? Press y or Any To Exit : ")
        print()
        if try_again == "y":
            continue
        
        return


def printSequence():
    while True:
        l , s = 0 , 0 
        while True:
            l = input("Enter The Length : ")
            if l.isdigit() == False:
                print("Invalid Number ")
                continue
            l = int(l)
            break
        
        while True:
            s = input("Enter The Start : ")
            if s.isdigit() == False:
                print("Invalid Number ")
                continue
            s = int(s)
            break
        
        print("The Sequence is :")
        for i in range(s,s+l):
            print(i , end = " ")
        print()
        
        try_again = input("Try Again ? Press y or Any To Exit : ")
        print()
        if try_again == "y":
            continue
        
        return
    

def AverageNumber():
    while True:
        print("I Will Accept Numbers Until You Enter (done) : ")
        list1 = []
        total, cnt , avg, num = 0, 0, 0, 0
        
        
        while num != "done":
            num = input("Enter The Number : ")
            if num == "done":
                break
            if num.isdigit() == False:
                print("Invalid Number")
                total += 1
                continue
            else :
                total += 1
                cnt += 1
            num = int(num)
            list1.append(num)
        
        print(f"The Total Number Of Inputs : {total}")
        print(f"The Count Of Valid Inputs : {cnt}")
        TotalSum = sum(list1)
        if len(list1) == 0:
            avg = 0
        else :
            avg = TotalSum / len(list1)
        print(f"The Avg Is : {avg}")
        
        try_again = input("Try Again ? Press y or Any To Exit : ")
        print()
        if try_again == "y":
            continue
        
        return


def removeDublicate():
    while True:
        list1 = []
        
        while True:
            print("Enter The Number Or Done To Get The Result")
            n = input()
            if n.isdigit() == False:
                if n == "done":
                    break
                print("Invalid Number")
                continue
            n = int(n)
            list1.append(n)
        list1 = list(set(list1))
        list1.sort()
        print(f"The Sorted Array is : {list1}")
        
        try_again = input("Try Again ? Press y or Any To Exit : ")
        print()
        if try_again == "y":
            continue
        
        return
    
def countWords():
    while True:
        
        while True:
            s = input("Enter The String Please : ")
            if s.isdigit() == True or s == "":
                print("Invalid String")
                continue
            break
        
        d = {}
        list1 = s.split()
        for i in list1:
            if i not in d:
                d[i] = 1
            else :
                d[i] += 1
        
        print("The Words Is : ")
        for key,value in d.items():
            print(f"{key=} : {value=}")
        
        try_again = input("Try Again ? Press y or Any To Exit : ")
        print()
        if try_again == "y":
            continue
        
        return

def gradeBook():
    while True:
        print("Enter The Grade Of 5 Strudents Only")
        students = []
        grades = []
        s , g= "" , 0
        for i in range(5):
            
            while True:
                s = input("The Student Name : ")
                if s.isdigit() == True or s == "":
                    print("Invalid Name")
                    continue
                break
            
            while True:
                g = input("The Grade Is : ")
                if g.isdigit() == False:
                    print("Invalid Grade")
                    continue
                g = int(g)
                break
                
            students.append(s)
            grades.append(g)
        
        mn = min(grades)
        mx = max(grades)
        avg = sum(grades) / len(grades)
        
        print(f"The Smallest Grade Is : {mn}")
        print(f"The Highest Grade Is : {mx}")
        print(f"The Avg Is : {avg}")
        
        try_again = input("Try Again ? Press y or Any To Exit : ")
        print()
        if try_again == "y":
            continue
        
        return

def shopping_cart():
    cart = {}
    while True:
        print("1 add item")
        print("2 remove item")
        print("3 view All items")
        print("4 Checkout")
        c = 0
        while True:
            c = input("Choose: ")
            if c.isdigit() == False:
                print("Invalid Choice")
                continue
            c = int(c)
            break

        if c == 1:
            
            while True:
                name = input("Item name: ")
                if name.isdigit() == True or name == "":
                    print("Invalid Name")
                    continue
                break
            
            while True:
                price = input("Item price: ")
                if price.isdigit() == False:
                    print("Invalid Price")
                    continue
                price = int(price)
                break
                
            cart[name] = price

        elif c == 2:
            
            while True:
                name = input("Item to remove : ")
                if name.isdigit() == True or name == "":
                    print("Invalid Name")
                    continue
                break
            
            if name not in cart:
                print("Not in The Cart")
            else :
                cart.pop(name)

        elif c == 3:
            if not cart:
                print("Cart is empty.")
            else:
                for item, price in cart.items():
                    print(f"{item}: {price}")

        elif c == 4:
            total = sum(cart.values())
            print(f"Total cost: ${total}")
            break
        


import random
def guessing_game():
    number = random.randint(1, 20)
    attempts = 0

    while True:
        while True:
            guess = input("Guess a number between 1 and 20: ")
            if guess.isdigit() == False:
                print("Invalid Number")
                continue
            guess = int(guess)
            break
            
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

def mainList():
    print("The Functions : ")
    print("1- Sort Numbers")
    print("2- Print Sequence Numbers")
    print("3- Average Of Numbers")
    print("4- Remove Dublicates And Sort")
    print("5- Count Words in String")
    print("6- GradeBook System")
    print("7- Shopping Cart")
    print("8- guessing_game")
    
    user_input = int(input("Choose The Function To Run : "))
    if user_input == 1:
        sortNumbers()
    elif user_input == 2:
        printSequence()
    elif user_input == 3:
        AverageNumber()
    elif user_input == 4:
        removeDublicate()
    elif user_input == 5:
        countWords()
    elif user_input == 6:
        gradeBook()
    elif user_input == 7:
        shopping_cart()
    elif user_input == 8:
        guessing_game()    
        
        
    mainList()
    exit()
        
mainList()
    
    
    
    
    
    