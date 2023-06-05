#rental car
user_pref = input("What kind of rental car that you would like ?\n")

print("Lemme see if I can find you a " + user_pref.title())

#restaurant seating

group = int(input('How many people are in your group?\n'))
if group > 8 :
    print('You have to wait for a table.')
else:
    print('The table is ready!')

#multiple of ten
num = int(input('Enter a number: '))
if num % 10 == 0 :
    print('The number ' + str(num) + ' is a multiple of ten.')
else:
    print('The number ' + str(num) + ' is not a multiple of ten.')