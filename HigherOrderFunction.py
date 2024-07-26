def square(num):
    return num ** 2 # 這邊一定要有return，不然會出現TypeError: 'map' object is not subscriptable

myList = [-10, 3, 9, 8, 10]

for item in map(square, myList):
    print(item)


def check_even(num): 
    return num % 2 == 0

anotherList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in filter(check_even, anotherList):
    print(item)