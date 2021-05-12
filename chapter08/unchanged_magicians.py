def make_great(magicians):
    """Modify each magician name in a list."""
    great_magicians = []

    while magicians:
        great_magicians.append(magicians.pop() + " the Great")

    return great_magicians

def show_magicians(magicians):
    """Display list of magicians."""
    for magician in magicians:
        print(magician.title())

unchanged_magicians = ['houdini', 'dynamo', 'copperfield']
changed_magicians = make_great(unchanged_magicians[:])

show_magicians(unchanged_magicians)
print("\n")
show_magicians(changed_magicians)