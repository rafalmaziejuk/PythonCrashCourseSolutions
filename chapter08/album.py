def make_album(artist_name, album_title, tracks_number=""):
    """Return dictionary containing album info."""
    if tracks_number:
        return {
            'artist_name': artist_name,
            'album_title': album_title,
            'tracks_number': tracks_number,
            }
    
    return {
            'artist_name': artist_name,
            'album_title': album_title,
            }

print(make_album('Gojira', 'Fortitude'))
print(make_album(artist_name='Nirvana', album_title='Nevermind'))
print(make_album(album_title='Bright Green Field', artist_name='Squid'))
print(make_album('Ariana Grande', 'Positions', 24))