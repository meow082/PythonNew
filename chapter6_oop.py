class Robot:
    #in classes, we can also define doctrings
    """Robot class is for creating robots"""   # docstring 規範，用來描述class的功能
    def __init__(self, name, age): # Constructor
        self.name = name
        self.age = age

    def walk(self):
        print(f"{self.name} is walking")

    def sleep(self, hours):  
        print(f"{self.name} is sleeping for {hours} hours")


# my_robot = Robot()
# print(type(my_robot))  # <class '__main__.Robot'>


my_robot1 = Robot("James", 10)
my_robot2 = Robot("John", 20)
print(my_robot1.name)
print(my_robot1.age)
print(my_robot1.age < my_robot2.age)

print(my_robot1.__doc__)
my_robot1.walk()
my_robot1.sleep(15)
