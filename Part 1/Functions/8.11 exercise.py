# magicians = ['david blaine', 'houdini', 'teller']
#
# def show_magicians(magicians):
#     while magicians:
#         show_mage = magicians.pop()
#         print(show_mage.title())
#
# show_magicians(magicians[:])
# print(magicians)

#Great magicians
# magicians = ['david blaine', 'houdini', 'teller']
# great_magicians =[]
# def make_great(magicians):
#     for magician in range(len(magicians)):
#         magicians[magician] = magicians[magician].title()
#         magicians[magician] += ' the Great'
#
# make_great(magicians)
# print(magicians[:])

#Unchanged magicians
magicians = ['david blaine', 'houdini', 'teller']
great_magicians = []


def make_great(magicians):
    for magician in range(len(magicians)):
        great_mage = magicians.pop().title() + ' the great'
        great_magicians.append(great_mage)
        great_magicians.reverse()

print(magicians)
make_great(magicians)
print(great_magicians)



