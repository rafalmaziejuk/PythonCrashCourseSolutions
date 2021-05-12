dream_vacation = {}
place = ""
active = True

while active:
    place = input("If you could visit one place in the world, where would you go? ")
    
    if place == 'quit':
        active = False
    else:
        if place not in dream_vacation.keys():
            dream_vacation[place] = 1
        else:
            dream_vacation[place] += 1

print("\nPOLL RESULTS")
for place, times_mentioned in dream_vacation.items():
    print(f"{place.title()} : {times_mentioned}")