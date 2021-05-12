def make_album(artist_name, album_title):
    """Return dictionary containing album info."""    
    return {
            'artist_name': artist_name,
            'album_title': album_title,
            }

while True:
    name = input("\nEnter artist's name ('q' ends): ")
    if name == 'q':
        break

    album = input("Enter album title ('q' ends): ")
    if album == 'q':
        break

    print(make_album(name, album))