sandwich_orders = ['pastrami', 'american sub', 'pastrami', 'bagel toast', 'pastrami', 'ice cream']
finished_sandwiches = []

print("Deli has run out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = sandwich_orders[:]

print("\nFinished sandwiches: ")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} sandwich")