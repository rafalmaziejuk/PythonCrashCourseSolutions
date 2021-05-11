person1 = {
    'first_name' : 'Asa',
    'last_name' : 'Butterfield',
    'age' : 24,
    'city' : 'London',
    }

person2 = {
    'first_name' : 'Emma',
    'last_name' : 'Mackey',
    'age' : 25,
    'city' : 'Le Mans',
    }

person3 = {
    'first_name' : 'Ncuti',
    'last_name' : 'Gatwa',
    'age' : 28,
    'city' : 'Kigali',
    }

people = [person1, person2, person3]

for person in people:
    print("First name: " + person['first_name'])
    print("Last name: " + person['last_name'])
    print("Age: " + str(person['age']))
    print("City: " + person['city'] + "\n")