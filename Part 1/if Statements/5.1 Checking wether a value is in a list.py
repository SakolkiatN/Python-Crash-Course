#use keyword 'in' to check

requested_toppings = ['mushroom', 'onion', 'pineapple']
print('mushroom' in requested_toppings)
print('pepperoni' in requested_toppings)

#checking whether a value is not in a list

banned_user = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_user:
    print(user.title() + ", You can post a response if you wish")
