motorcycles = ['honda', 'yamaha', 'suzuki' ]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
#popped will remove item from the list and use that popped values
print("The last motorcycles I owned was a " + popped_motorcycles.title() + ".")

motorcycles = ['honda', 'yamaha', 'suzuki' ]
print(motorcycles)
print(motorcycles.pop(2))
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki' ]
motorcycles.remove('honda')

#pop can remove using position but remove need to input "String"
print("")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
