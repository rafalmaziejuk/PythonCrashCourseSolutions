favorite_places = {
    'alex' : ['hawaii', 'mount everest', 'warsaw'],
    'michael' : ['baltic sea', 'bahamas', 'berlin'],
    'john' : ['black sea', 'crete', 'amsterdam'],
    }

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")

    for place in places:
        print(f"{place.title()}")

    print("\n")