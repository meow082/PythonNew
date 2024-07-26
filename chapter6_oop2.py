class Robot:
    ingredient = "metal" # class attribute，類似於static attribute

    def __init__(self, name, age): # Constructor
        self.name = name
        self.age = age

    def walk(self):
        print(f"{self.name} is walking")

    def sleep(self, hours):  
        print(f"{self.name} is sleeping for {hours} hours")

    def greet(self):
        print(f"Hello, my name is {self.name}, and I am made of {self.__class__.ingredient}.")
        print(f"Hello, my name is {self.name}, and I am made of {self.ingredient}.")

print(Robot.ingredient)

my_robot1 = Robot("James", 10)

print("------------------------------------------------------------1")
print(my_robot1.ingredient)
print("------------------------------------------------------------2")
print(my_robot1.__class__.ingredient)
my_robot1.greet()