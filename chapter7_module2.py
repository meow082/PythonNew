import random as rd
import sys

# modules in python are object
print(rd.randint(1, 10))

print(sys.path)

x = 10      #global variable => 會改變global namespace 的內容

def hello():
    xx = 5              #會在local namespace裡新增一個變數
    print(locals())     #return local namespace as a dictionary
    print("hello")

print(globals())    #return global namespace as a dictionary

hello()
