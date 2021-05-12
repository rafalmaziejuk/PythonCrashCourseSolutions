def city_country(name, country):
    """Return neatly formatted city's name and country it is in."""
    return f"{name.title()}, {country.title()}"

print(city_country('santiago', 'chile'))
print(city_country('warsaw', 'poland'))
print(city_country('berlin', 'germany'))