favorite_numbers = {
    'jen' : [1, 2, 3],
    'sarah' : [4, 5, 6],
    'jane' : [7, 8, 9],
    'edward' : [10, 11, 12],
    'phil' : [13, 14, 15],
    }

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")

    for number in numbers:
        print(str(number))

    print("\n")