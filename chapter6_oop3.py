# 課程97.
class Robot:
    ingredient = "metal" # class attribute，類似於static attribute

    def __init__(self, name, age): # Constructor
        self.name = name
        self.age = age

    @staticmethod   # decorator，用來定義static method
    def greet():    # 第一個參數不是self，所以不能訪問instance attribute
        print("A robot is greeting you")


class Circles:
    """This class creates circle"""
    pi = 3.14159
    all_circles = []

    def __init__(self, radius):
        self.radius = radius
        self.__class__.all_circles.append(self)

    def area(self):
        return self.__class__.pi * self.radius ** 2
    
    @staticmethod
    def total_area():
        total = 0
        for circle in Circle.all_circles:  #如果class name改成Circles，會出現NameError: name 'Circle' is not defined
            total += circle.area()
        return total
    
    @classmethod    #叫節省記憶體，因為不需要創建instance，直接用class name就可以調用
    def total_area2(cls):
        total = 0
        for circle in cls.all_circles:    # 好處是不需要寫死class name，可以直接用cls
            total += circle.area()
        return total
    

my_robot1 = Robot("James", 10)
my_robot2 = Robot("John", 20)

Robot.greet()
my_robot1.__class__.greet()
my_robot1.greet()

print("------------------------------------------------------------1")

c1 = Circles(10)
c2 = Circles(15)

#print(c1.__class__.total_area())
print(c1.__class__.total_area2())   #class name改名後，不會出現NameError: name 'Circle' is not defined