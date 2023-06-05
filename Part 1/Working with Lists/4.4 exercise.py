count20 = [value+1 for value in range(0,20)]
print(count20)

# #One million
# countmillion = [value+1 for value in range(0,1000000)]
# print(countmillion)
#
# #Summing a million
# print(min(countmillion))
# print(max(countmillion))
# print(sum(countmillion))

#Odd number
odds =[]
for odd in range(1,20,2):
    odds.append(odd)
print(odds)

odds = [value + 2 for value in range(1,19,2)]
print(odds)

#Threes
threes = []
for three in range(3,31):
    threes.append(3*three)

print(threes)
###
mult3 = [values * 3 for values in range(3,31)]
print(mult3)

#Cubes
for cube in range(1,11):
    print("The cube of "+str(cube) + " is " + str(cube**3) )

#Cubes comprehension

cubes = [cube**3 for cube in range(1,11)]
print(cubes)

