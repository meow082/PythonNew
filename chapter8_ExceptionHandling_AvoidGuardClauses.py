
def divide(a, b):
    if type(a) != int or type(b) != int:
        raise ValueError("Invalid argument type!!")
    
    if b == 0:
        raise ZeroDivisionError("The second argument cannot be 0.")
    
    return a / b


try:
    #print(divide(10, "hello"))
    print(divide(10, 0))
    print(divide(6, 3))
# except:
#     print("something went wrong")
except Exception as e:
    print(e)



# Guard Clauses  隨著複雜度上升可能會看起來像callback hell
# def divide2(a, b):
#     if type(a) == int and type(b) == int:
#         if b != 0:
#             return a / b
#         else:
#             return "The second argument cannot be 0."     
#     else:
#         return "Invalid argument type!!"
    

# print(divide2(10, "hello"))    # Invalid argument type!!
# print(divide2(10, 0))          # The second argument cannot be 0.
# print(divide2(6, 3))           # 2.0