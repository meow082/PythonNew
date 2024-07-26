def mySort(lst):
    if len(lst) == 0:
        return "undefined"
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    print(lst)
    return lst


def isPrime(num):
    if num < 2:
        print(False)
        return False

    for i in range(2, num):
        if num % i == 0:
            print(False)
            return False

    print(True)
    return True


def palindrome(string):
    if string == string[::-1]:
        print(True)
        return True

    print(False)
    return False


def palindrome2(string):  #效能較好
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            print(False)
            return False
        left += 1
        right -= 1
    
    print(True)
    return True


def pyramid(num):
    count = 1
    for i in range(num - 1, -1, -1):  
        print(" " * i + "*" * count)
        count += 2


def inversePyramid(num):
    count = 0
    for i in range(num, 0, -1):
        print(" " * count + "*" * (2 * i - 1))
        count += 1
    

def has_33(lst):
    if(len(lst) < 2):
        return False
    
    previousNum = -1
    for i in lst:
        if i != previousNum: 
            previousNum = i
            continue
        elif i == 3 and previousNum == 3:
            return True
            
    return False


def spyGame (lst):
    count = 0
    for i in lst:
        if i == 0:
            count += 1
        elif count != 2 and i == 7:
            count = 0
        elif count == 2 and i == 7:
            return True
    
    return False

#mySort([17, 0, -3, 2, 1, 0.5]); # returns [-3, 0, 0.5, 1, 2, 17]


#print("---------------------------------------------------------------")

# isPrime(1)  # returns false
# isPrime(5)  # returns true
# isPrime(91) # returns false
# isPrime(1000000) # returns false


#print("---------------------------------------------------------------")

#palindrome("bearaeb"); # true
#palindrome("Whatever revetahW"); # true
#palindrome("Aloha, how are you today?"); # false


#print("---------------------------------------------------------------")

#pyramid(1);
# *
#pyramid(2);
#  *
# ***
#pyramid(4);
#    *
#   ***
#  *****
# *******

print("---------------------------------------------------------------")

inversePyramid(4);
# *******
#  *****
#   ***
#    *

print("---------------------------------------------------------------")

print(has_33([1, 5, 7, 3, 3])) # True
print(has_33([])) # False
print(has_33([4, 3, 2, 1, 0])) # False

print("---------------------------------------------------------------")

print(spyGame([1, 2, 4, 0, 3, 0, 7])) # True
print(spyGame([1, 2, 5, 0, 3, 1, 7])) # False