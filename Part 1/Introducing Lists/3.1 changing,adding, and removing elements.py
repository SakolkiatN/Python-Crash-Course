motorcycles = ['honda', 'yamaha', 'suzuki' ]
print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('suzuki')
motorcycles.append('yamaha')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[1]
print(motorcycles)


print(motorcycles)