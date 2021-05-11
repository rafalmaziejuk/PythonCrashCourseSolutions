users = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princeton',
        'favorite_numbers' : [1, 2, 3, 4],
        },

    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris',
        'favorite_numbers' : [5, 6, 7, 8],
        },

    'mjordan' : {
        'first' : 'michael',
        'last' : 'jordan',
        'location' : 'chicago',
        'favorite_numbers' : [9, 10, 11, 12],
        },
    }

for username, infos in users.items():
    print(f"\n{username}'s info")
    
    for key, value in infos.items():
        if key != 'favorite_numbers':
            print(f"{key} : {value}")
        else:
            print("favorite_numbers:")

            for number in value:
                print(str(number))