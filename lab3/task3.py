from datetime import datetime, date

def DatetimeReminder():
    
    user_date = input("Enter a date (YYYY-MM-DD): ")
    
    try:
        
        year, month, day = user_date.split('-')
        target_date = date(int(year), int(month), int(day))
        
        today = date.today()
            
        difference = target_date - today
        days_left = difference.days
        
        if days_left < 0:
            print("This date has already passed.")
        elif days_left == 0:
            print("This date is today!")
        else:
            reminder_text = f"{target_date} -> {days_left} days left"
            
            with open("reminders.txt", "a") as file:
                file.write(reminder_text + "\n")
            
            print("Current reminders : ")
            try:
                with open("reminders.txt", "r") as file:
                    print(file.read())
            except FileNotFoundError:
                print("no reminders file found.")

    except ValueError:
        print("Error: Please enter date in correct format (YYYY-MM-DD)")