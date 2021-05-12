def make_car(manufacturer, model_name, **arguments):
    new_car = {
        'manufacturer': manufacturer,
        'model_name': model_name,
        }

    for key, value in arguments.items():
        new_car[key] = value

    return new_car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)