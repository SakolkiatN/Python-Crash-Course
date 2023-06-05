def make_pizza(*toppings):  # *value is when you don't know specific value
    """Print the list of toppings that have been requested"""
    print(toppings)
#*toppings this parameter collects as many arguments as provided
make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')

def made_pizza(*toppings):
    '''Summarize the pizza we are able to make'''
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

made_pizza('peperoni')
made_pizza('mushroom', 'green peppers', 'extra cheese')