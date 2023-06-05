digits = [1,2,3,4,5,6,7,8,9,0]
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))


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
