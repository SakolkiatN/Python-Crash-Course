#Pizza toppings


toppings = ''
while toppings != 'quit':
    toppings = input("Choose your pizza toppings: " )
    print("I will add " + toppings + " to your pizza.")
else:
    print('Your will get your pizza soon!')

###movie ticket
print('Enter > 100 to quit')
age = 0
while True:
    age = int(input('Enter your age: '))
    if age < 3:
        print('Your ticket is free.')
    elif age  < 12:
        print('Your ticket will be $10.')
    elif age  < 100:
        print('Your ticket will be $15.')
    else:
        break


### Three exits
#topping Variables and Simple Data Types
print("enter 'quit' to finish!")
active = True
while active:
    toppings = input("Choose your pizza toppings: " )
    if toppings != 'quit':
        print("I will add " + toppings + " to your pizza.")
    else:
        print('You will get your pizza soon!')
        active = False

#topping Introducing Lists

prompt = "Choose your topping:\n"

while True:
    topping = input(prompt)
    if topping.lower() == 'quit':
        print('Your pizza is finished!')
        break
    else:
        print("I will add " + topping.title() + " to your pizza.")




















