sandwich_orders = ['american sub', 'bagel toast', 'ice cream']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich.title()} sandwich")

print("\nFinished sandwiches: ")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} sandwich")