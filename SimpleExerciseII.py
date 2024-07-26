def stars(num):
    for i in range(1, num + 1):
        print("*" * i)


def stars2(num):
    for i in range(1, num + 1):
        print("*" * i)
    for i in range(num - 1, 0, -1):
        print("*" * i)


def table(num):
    for i in range(1, 10):
        print(f"{num} X {i} = {num * i}")


def table9to9():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} X {j} = {i * j}")


def swap(string):
    result =''
    for i in string:
        if(i.isupper()):
            result += i.lower()
        else:
            result += i.upper()

    print(result)


def findMin(list):
    list.sort()
    if len(list) == 0:
        return print("undefined")
    else:
        return print(list[0])
    

def findMin2(list):     # 這個方法是不用sort的
    if len(list) == 0:
        print("undefined")
        return "undefined"
    
    min = list[0]
    for element in list:
        if element < min:
            min = element
    print(min)
    return min

#stars(1);
# *
#stars(4);
# *
# **
# ***
# ****

print("---------------------------------------------------------------")

#stars2(1);
# *
#stars2(2);
# *
# **
# *
#stars2(3);
# *
# **
# ***
# **
# *
#stars2(4);
# *
# **
# ***
# ****
# ***
# **
# *

print("---------------------------------------------------------------")

#table(3)

print("---------------------------------------------------------------")

#table9to9()

print("---------------------------------------------------------------")

swap("Aloha"); # returns "aLOHA"
swap("Love you."); # returns "lOVE YOU."

print("---------------------------------------------------------------")

findMin([1, 2, 5, 6, 99, 4, 5]); # returns 1
findMin([]); # returns undefined
findMin([1, 6, 0, 33, 44, 88, -10]); # returns -10