#Lambda input1, input2, ...: expression

result = (lambda x: x**2)(5)
print(result)  # 25


myTuple = (lambda x, y: (x + y, x - y))(15, 30)
print(myTuple)  # (45, -15)


for item in map(lambda x: x**2, [-15, 10, 5, 0]):
    print(item)


print('---------------------------------')
for item in filter(lambda x: x % 2 == 0, [-15, 10, 5, 0]):
    print(item)

