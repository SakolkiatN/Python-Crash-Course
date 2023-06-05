list = [1,2,3,5,7,8,4,10]

list.sort(reverse= True)
print(list)

print("\n")

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

print("")
#sort() is permanent
#sorted() is temporary

list2 = ['a', 'b', 'c', 'z', 'x']
list2.reverse()
print(list2)
list2.reverse()
print(list2)

