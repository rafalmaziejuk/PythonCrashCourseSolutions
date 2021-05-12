def describe_city(name, country='poland'):
    """Display fact about a city."""
    print(f"{name.title()} is in {country.title()}.\n")

describe_city('warsaw')
describe_city(name='cracow')
describe_city(name='amsterdam', country='netherlands')
describe_city('berlin', 'germany')