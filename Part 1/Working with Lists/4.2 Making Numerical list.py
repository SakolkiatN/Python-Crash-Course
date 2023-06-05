for value in range(1, 6):
    print(value)

#use list() to convert that set of number into a list
number = list(range(1, 6))
print(number)

even_numbers = list(range(2,11,2))
print(even_numbers)

# squares = []
# for value in range(1,11):
#     square = value**Variables and Simple Data Types
#     squares.append(square)
#
# print(squares)

#more concise version
squares = []
for value in range(1,11):
    squares.append(value**2)
# print(squares)

squares = [value**2 for value in range (1,11)]
print(squares)

additives = [value+1 for value in range(1,10)]
print(additives)

sqr = [value*value for value in range(0,10)]
print(sqr)

count = [value + 1 for value in range(0,20)]
print(count)

print(range(1,10))


