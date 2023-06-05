#slices

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

print("The first three items in the list are:")
print(list[:3])
for x in list[:3]:
    print(x)

print("Three items in the middle of the list are:")
print(list[3:6])
for x in list[3:6]:
    print(x)

print("The last three items in the list are:")
print(list[-3:])
for x in list[-3:]:
    print(x)

#My pizzas, Your Pizzas:
my_pizzas = [
    "Neapolitan Pizza",
    "Chicago Pizza",
    "New York-Style Pizza"
]
friend_pizzas = my_pizzas[:]
my_pizzas.append("Pepperoni Pizza")

print("My favourite Pizzas are:,")
for me in my_pizzas:
    print(me)

print("\nMy friend's favourite pizzas are:,")
for friend in friend_pizzas:
    print(friend)
