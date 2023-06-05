user_names = ['admin', 'arm', 'warm', 'khawpun', 'khawtoo']

for user_name in user_names:
    if user_name == 'admin':
        print("Hello " + user_name + ", would you like to see a status report?")
    else:
        print("Hello " + user_name.title() + ", thank you for logging in again.")
else:
    print("We need to find some users!")

#Checking usernames

current_users = ['arm', 'earth', 'khawtoo', 'khawpun', 'warm']

new_users = ['guide', 'rew', 'home', 'bua', 'Arm']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user.title() + " has already been used.")
    else:
        print(new_user.title() + " is available.")

#Ordinal numbers

numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")

