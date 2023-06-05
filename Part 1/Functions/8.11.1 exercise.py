magicians = ['david blaine', 'houdini', 'teller']
great_magicians = []

def make_great(magicians):
    for i, name in enumerate(magicians):
        magicians[i] = name.title() + ' the Great'

make_great(magicians)
print(magicians)

