def cube(n):
    for x in range(n):
        yield x**3      # yield 會return 一個generator object


print(cube(10))         # <generator object cube at 0x0000024E3A3B0F90>

# 用for loop來取得generator object的值，因為generator是一個iterable object
for element in cube(10):
    print(element)




# 一般的做法，但是會佔用記憶體
# def cube(n):
#     result = []
#     for x in range(n):
#         result.append(x**3)
#     return result

# for i in cube(10):
#     print(i)