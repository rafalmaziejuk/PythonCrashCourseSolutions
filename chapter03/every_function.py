list = ['America', 'Poland', 'Russia', 'Polish', 'English', 'Russian', 'Mount Everest']

print("Adding elements")
list.append('France')
list.insert(len(list), 'French')
print(list)
print("\n")

print("Deleting elements")
del list[1]
list.pop()
list.pop(2)
list.remove('English')
print(list)
print("\n")

print("Reversing")
list.reverse()
print(list)
list.reverse()
print(list)
print("\n")

print("Sorting")
print(list)
print(sorted(list))
print(list)
print(sorted(list, reverse = True))
print(list)
list.sort()
print(list)
list.sort(reverse = True)
print(list)