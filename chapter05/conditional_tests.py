print("Is 5 == 5? I predict True.")
print(5 == 5)

print("\nIs 5 > 1? I predict True.")
print(5 > 1)

print("\nIs 5 < 6? I predict True.")
print(5 < 6)

print("\nIs 5 <= 5? I predict True.")
print(5 <= 5)

print("\nIs 5 >= 1 I predict True.")
print(5 >= 1)

print("\nIs 5 != 5? I predict False.")
print(5 != 5)

print("\nIs 5 < 1? I predict False.")
print(5 < 1)

print("\nIs 5 > 6? I predict False.")
print(5 > 6)

print("\nIs 5 >= 6? I predict False.")
print(5 >= 6)

print("\nIs 5 <= 1? I predict False.")
print(5 <= 1)

print("\nIs 'subaru' == 'subaru'? I predict True.")
print('subaru' == 'subaru')

print("\nIs 'car' != 'subaru'? I predict True.")
print('car' != 'subaru')

print("\nIs 'car' == ('CAR').lower()? I predict True.")
print('car' == ('CAR').lower())

print("\nIs 'car' == ('CAR').lower() and 'subaru' == 'SUBARU'? I predict False.")
print('car' == ('CAR').lower() and 'subaru' == 'SUBARU')

print("\nIs 'car' == ('CAR').lower() or 'subaru' == 'SUBARU'? I predict True.")
print('car' == ('CAR').lower() or 'subaru' == 'SUBARU')

foods = ['apple', 'lemon', 'orange', 'grapefruit']

print("\nfoods list:")
for food in foods:
    print(food)

print("\nIs 'apple' in foods? I predict True.")
print('apple' in foods)

print("\nIs 'potato' not in foods? I predict True.")
print('potato' not in foods)