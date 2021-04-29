message = "You are still invited to my dinner, "
apology = "I am sorry I could not invite you to my dinner "
guest_list = ['Albert Einstein', 'Bruce Lee', 'Adam West']

guest_list.insert(0, 'Michael Jackson')
guest_list.insert(2, 'Michael Jordan')
guest_list.append('Nina Simone')

print(apology + guest_list.pop() + '.')
print(apology + guest_list.pop() + '.')
print(apology + guest_list.pop() + '.')
print(apology + guest_list.pop() + '.')

print(message + guest_list[0] + ".")
print(message + guest_list[1] + ".")
print("I am sorry, I needed to shrink my guest list to only two guests.")
print("I am inviting " + str(len(guest_list)) + " people to my dinner.")