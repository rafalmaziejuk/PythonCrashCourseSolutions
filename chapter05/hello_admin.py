usernames = ['admin', 'eric', 'amanda', 'thomas', 'john']

for username in usernames:
    if username != 'admin':
        print("Hello " + username.title() + ", thank you for logging in again.")
    else:
        print("Hello admin, would you like to see a status report?")

usernames.clear()

if not usernames:
    print("\nWe need to find some users!")