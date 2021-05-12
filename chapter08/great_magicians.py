def make_great(magicians):
    """Modify each magician name in a list."""
    for i in range(0, len(magicians)):
        magicians[i] =  magicians[i].title() + " the Great"

def show_magicians(magicians):
    """Display list of magicians."""
    for magician in magicians:
        print(magician.title())

magicians = ['houdini', 'dynamo', 'copperfield']

show_magicians(magicians)
print("\n")

make_great(magicians)
show_magicians(magicians)