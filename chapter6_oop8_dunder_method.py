class Robot:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    #define a private method __key()
    def __key(self):
        return (self.name, self.age, self.address)
    
    #implement __hash__() method
    def __hash__(self):
        return hash(self.__key())   #把__key()的tuple的值hash
    
    def __eq__(self, other):    #other 可能相當於另一個Robot instance
        if isinstance(other, Robot):    #確認other是否為Robot instance
            return self.__key() == other.__key()
        return NotImplemented
    
    def __len__(self):
        return len(self.name)
    
    def __str__(self):
        return f"{self.name} is {self.age} years old and lives in {self.address}"
    
    def __repr__(self):
        return f"name: {self.name}, age: {self.age}, address: {self.address}"
    
    def __add__(self, other):
        if isinstance(other, Robot):
            return self.age + other.age
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Robot):
            return self.age > other.age
        return NotImplemented
        

robot1 = Robot("Wilson", 30, "Taiwan")
robot2 = Robot("Wilson", 25, "Taiwan")

print(len(robot1))  # 6

print(robot1)       # Wilson is 30 years old and lives in Taiwan 實作__str__後不會再印出記憶體位置
print(str(robot1))  # 一樣的結果
print(repr(robot1)) # name: Wilson, age: 30, address: Taiwan 

print(robot1 + robot2)  # 55

print(robot1 > robot2)  # True