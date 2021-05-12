def show_magicians(magicians):
    """Display list of magicians."""
    for magician in magicians:
        print(magician.title())

magicians = ['houdini', 'dynamo', 'copperfield']

show_magicians(magicians)