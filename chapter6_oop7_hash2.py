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

    

robot = Robot("James", 20, "New York")
dictionary = {robot: "James"}     #把robot當作dict的key
print(dictionary[robot])  # James


robot1 = Robot("Wilson", 30, "Taiwan")
robot2 = Robot("Wilson", 30, "Taiwan")
print (robot1 == robot2)  # 有了__eq__()方法後，才會回傳True