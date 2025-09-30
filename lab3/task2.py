import re
import time
import math
from datetime import datetime
from task7 import DecoratorsTask

@DecoratorsTask
def RegexLogCleaner():
    with open("unvalidEmails.txt", "r") as file:
        invalidcontent = file.read()

    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    found_emails = re.findall(email_pattern, invalidcontent)
    unique_emails = list(set(found_emails))

    with open("valid_emails.txt", "w") as file:
        for email in unique_emails:
            file.write(email + "\n")
    
    t = len(unique_emails)
    print(f"Total unique emails : {t}")

    print("valid emails : ")
    with open("valid_emails.txt", "r") as file:
        print(file.read())