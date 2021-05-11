favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people = ['jen', 'george', 'sarah', 'michael']

for name, language in favorite_languages.items():
    if name in people:
        print("Thank you " + name.title() + " for your respond!")
    else:
        print("Please " + name.title() + ", take our poll.")