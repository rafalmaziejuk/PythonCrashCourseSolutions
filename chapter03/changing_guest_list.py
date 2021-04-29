message = "I invite you to my dinner, "
guest_list = ['Albert Einstein', 'Bruce Lee', 'Adam West']

missing_guest = guest_list.pop(1)
guest_list.insert(1, 'Michael Jackson')

print(message + guest_list[0] + ".")
print(message + guest_list[1] + ".")
print(message + guest_list[2] + ".")
print("I am deeply saddened that " + missing_guest + " could not make it in time.")