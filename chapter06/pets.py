pet1 = {
    'name' : 'addie',
    'kind' : 'hamster',
    'owner' : 'bob',
    }

pet2 = {
    'name' : 'ace',
    'kind' : 'dog',
    'owner' : 'abigail',
    }

pet3 = {
    'name' : 'alf',
    'kind' : 'cat',
    'owner' : 'alex',
    }

pet4 = {
    'name' : 'ajax',
    'kind' : 'fish',
    'owner' : 'robin',
    }

pets = [pet1, pet2, pet3, pet4]

for pet in pets:
    print(f"{pet['owner'].title()} owns a {pet['kind']} named {pet['name'].title()}.")