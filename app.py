# def exponent(a, b):
#     return a ** b

# def sum(*args):
#     result = 0
#     for number in range(len(args)):
#         result += args[number]
#         print(f"Now, the result is {result}")
#     return result

def myfunc(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# #positional arguments
# print(exponent(2, 3))  # 8
# print(exponent(3, 2))  # 9

# #keyword arguments
# print(exponent(a=2, b=3))  # 8
# print(exponent(b=3, a=2))  # 8

# print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # 55

myfunc(name="John", age=25, city="New York")  # name = John, age = 25, city = New York
