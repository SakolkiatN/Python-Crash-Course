#Deli

sandwich_orders =['sandwich1', 'sandwich2', 'sandwich3']
finished_sandwiches = []

while sandwich_orders:
    for sandwich in sandwich_orders:
        finish = sandwich_orders.pop()
        finished_sandwiches.append(finish)
        print("I made you " + finish.title() + ".")

#No pastrami
sandwich_orders  =['sandwich1', 'sandwich2', 'sandwich3','pastrami','pastrami','pastrami','pastrami','sandwich4']

finished_sandwiches = []

print("The Pastrami is out of stock.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    for sandwich in sandwich_orders:
        finish = sandwich_orders.pop()
        finished_sandwiches.append(finish)
        print("I made you " + finish.title() + ".")


#Dream vacations

poll = {}

polling_active = True

while polling_active:
    name = input("What's your name?\n\t")
    place = input("Where is your dream vacation? \n\t")
    poll[name] = place

    cont = input("Would you let other take the poll? (yes/no)\n\t")
    if cont.lower() == 'no':
        polling_active = False

print("---Poll results---")
for key,name in poll.items():
    print(key.title() + "'s dream vacation is " + name.title() + ".")







