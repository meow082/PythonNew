def factorPrime(num):
    lst = []
    for i in range(2, num // 2 + 1):
        while num % i == 0:
            lst.append(i)
            num //= i

    if len(lst) == 0:
        print(num)
        return num

    string = ""
    for i in lst:
        string += str(i) + " X "

    print(string[:-3])
    return string[:-3]


def intersection(lst1, lst2):
    my_set = set(lst1)
    return_lst = []
    for i in set(lst2):
        if i in my_set:
            return_lst.append(i)

    print(return_lst)
    return return_lst


def intersection2(lst1, lst2):
    return list(set(lst1) & set(lst2))


def flatten(lst):
    my_list = []
    for i in lst:
        if type(i) == list:
            my_list += flatten(i)
        else:
            my_list.append(i)
    return my_list


factorPrime(120); # returns "2 x 2 x 2 x 3 x 5"

factorPrime(13); # returns 13


print("---------------------------------------------------------------")


intersection([1, 3, 4, 6, 10], [5, 11, 4, 3, 100, 144, 0]); # returns [3, 4]
print(intersection2([1, 3, 4, 6, 10], [5, 11, 4, 3, 100, 144, 0])); # returns [3, 4]


print("---------------------------------------------------------------")


print(flatten([1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [2]]]));
# returns [1, 2, 0, 1, 3, 1, 3, 3, 4, 1, 2]