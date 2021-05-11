cities = {
    'warsaw' : {
        'country' : 'poland',
        'population' : 1765000
        },

    'amsterdam' : {
        'country' : 'netherlands',
        'population' : 821752
        },

    'berlin' : {
        'country' : 'germany',
        'population' : 3645000
        },
    }

for city, facts in cities.items():
    print(f"Facts about {city.title()}")
    print(f"Country: {facts['country'].title()}")
    print(f"Population: {facts['population']}\n")