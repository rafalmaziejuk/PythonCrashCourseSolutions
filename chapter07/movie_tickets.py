active = True
age = 0

while active:
    age = int(input("\nWhat is your age (Enter -1 when you are finished)? "))

    if age == -1:
        active = False
    else:
        if age < 3:
            print("Your movie ticket is free.")
        elif age >= 3 and age <= 12:
            print("Your movie ticket costs $10.")
        elif age > 12:
            print("Your movie ticket costs $15.")