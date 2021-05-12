active = True
topping = ""

while active:
    topping = input("\nEnter a series of toppings (enter 'quit' when you are finished): ")

    if topping == 'quit':
        active = False
    else:
        print(f"I will add {topping} to you your pizza.")