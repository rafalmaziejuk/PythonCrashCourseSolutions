pizzas = ['hawaiian', 'pepperoni', 'margherita']
friend_pizzas = pizzas[:]

pizzas.append('marinara')
friend_pizzas.append('vegetariana')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)