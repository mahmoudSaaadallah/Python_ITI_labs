import random
import csv

def RandomDataGenerator():

    while True:
        try:
            count = int(input("How many random numbers to generate? "))
            break
        except ValueError:
            print("Please enter a valid number.")

    random_numbers = []
    for i in range(count):
        random_number = random.randint(1, 100)
        random_numbers.append(random_number)

    with open("random_numbers.csv", "w", newline='') as file:
        
        writer = csv.writer(file)
        writer.writerow(["index", "value"])
        
        for i in range(len(random_numbers)):
            index = i
            value = random_numbers[i]
            writer.writerow([index, value])

    total_count = len(random_numbers)
    total_sum = sum(random_numbers)
    average = total_sum / total_count

    print(f"Total count: {total_count}")
    print(f"Average: {average}")
    