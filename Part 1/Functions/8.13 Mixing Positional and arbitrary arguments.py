#the parameter that accepts an arbitrary number of arguments must be placed last in the function definition
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')