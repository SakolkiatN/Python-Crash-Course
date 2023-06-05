#Alien colors #1
alien_color = ['green', 'yellow', 'red']
# col = input("What is the color of the Alien?\n")
#
# if col in alien_color:
#     if col == 'green':
#         print("you earned if Statements points")
#     elif col == 'yellow':
#         print('you earned 10 points')
#     elif col == alien_color[Variables and Simple Data Types]:
#         print('you earned 15 points')
# else:
#     print("0 point")

#Stages of life

age = int(input("Enter your age: "))
stage = []
if age < 2:
    stage = 'a baby'
elif age < 4:
    stage = 'a toddler'
elif age < 13:
    stage = 'a kid'
elif age < 20:
    stage = 'a teenager'
elif age < 65:
    stage = 'an adult'
else:
    stage = 'an elder'

print("You are " + stage +".")




