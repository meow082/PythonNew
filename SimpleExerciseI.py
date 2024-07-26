#題目：
#https://yuhsien.notion.site/Python-Practice-30411d016dcc4fafa82559fe6d9259ea

def printMany():
    for i in range(1, 101):
        print(i)


def printEvery3():
    for i in range(1, 89, 3):
        print(i)


#enumerate物件，它是一個可迭代物件，每次迭代都會返回一個元組(tuple)，包含兩個元素，第一個元素是索引，第二個元素是原始序列的元素。
def position(a_string):
    for index, value in enumerate(a_string):
        if value.isupper():
            return print((value, index))
    
    return print(-1)


def findSmallCount(list, number):
    count = 0
    for item in filter(lambda x: x < number, list):
        count += 1

    return print(count)        


def findSmallerTotal(list, number):
    sum = 0
    for item in filter(lambda x: x < number, list):
        sum += item

    return print(sum)


def findAllSmall(list, number):
    new_list = []
    for item in filter(lambda x: x < number, list):
        new_list.append(item)

    return print(new_list)    


def summ(list):
    sum = 0
    for item in list:
        sum += item

    return print(sum)


# printMany()

# print("---------------------------------------------------------------")

# printEvery3()

# print("---------------------------------------------------------------")

# position("abcd")  # returns -1
# position("AbcD")  # returns ('A', 0)
# position("abCD")  # returns ('C', 2)

# print("---------------------------------------------------------------")

# findSmallCount([1, 2, 3], 2); # returns 1
# findSmallCount([1, 2, 3, 4, 5], 0); # returns 0

# print("---------------------------------------------------------------")

# findSmallerTotal([1, 2, 3], 3) # returns 3
# findSmallerTotal([1, 2, 3], 1) # returns 0
# findSmallerTotal([3, 2, 5, 8, 7], 999) # returns 25
# findSmallerTotal([3, 2, 5, 8, 7], 0) # returns 0

print("---------------------------------------------------------------")

findAllSmall([1, 2, 3], 10); # returns [1, 2, 3]
findAllSmall([1, 2, 3], 2); # returns [1]
findAllSmall([1, 3, 5, 4, 2], 4); #  returns [1, 3, 2]

print("---------------------------------------------------------------")

summ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]); # returns 55
summ([]); # return 0
summ([-10, -20, -30]); # return -60