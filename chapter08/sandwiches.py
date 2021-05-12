def show_sandwich_toppings(*toppings):
    """Display sandwich toppings."""
    print("\nSandwich toppings:")

    for topping in toppings:
        print(topping)

show_sandwich_toppings('tomato')
show_sandwich_toppings('tomato', 'onion')
show_sandwich_toppings('tomato', 'onion', 'pickle')