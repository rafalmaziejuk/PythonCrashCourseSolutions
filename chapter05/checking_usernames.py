current_users = ['admin', 'eric', 'amanda', 'thomas', 'john']
new_users = ['briaN', 'rebecca', 'AdmIn', 'Tiffany', 'JoHn']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("You entered '" + new_user + "' username which already exists! Please enter a new username.")
    else:
        print(new_user + " username is available.")