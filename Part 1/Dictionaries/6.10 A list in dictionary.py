#store information about a pizza being ordered.

pizza = {
    'crust': 'thick',
    'topping': ['mushroom', 'extra cheese'],

}
#summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "withe the following toppings:")

for topping in pizza['topping']:
    print("\t"+ topping)

#

favorite_language = {
    'jen' : ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name,languages in favorite_language.items():
    if len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
    else:
        print("\n" + name.title() + "'s favorite language is:")

    for language in languages:
        print("\t" + language.title())

