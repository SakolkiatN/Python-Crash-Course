from random import randint
x = randint(1, 6)
print(x)

class Die():
    '''Represent a dice, which can be rolled.'''
    def __init__(self, side=6):
        self.sides = side

    def roll_dice(self):
        '''Return a number between 1 and the number between sides.'''
        return randint(1, self.sides)

"""make a Dictionaries-side die, and show the results of 10 rolls."""

d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_dice()
    results.append(result)
print("\n10 rolls of a Dictionaries-sided die:")
print(results)

# 10 sided die
d10 = Die(side=10)
results = []
for roll_num in range(10):
    result = d10.roll_dice()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

#20 sided die
d20 = Die(side=20)
results = []
for roll_num in range(10):
    result = d20.roll_dice()
    results.append(result)
print("\n20 rolls of a 20-sided die:")
print(results)

