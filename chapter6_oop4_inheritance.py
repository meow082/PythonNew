class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sleep(self):
        print(f"{self.name} is sleeping")

    def eat(self):
        print(f"{self.name} is eating") 

    
class Student(People):  # Student class is inheriting from People class
    def __init__(self, name, age, student_id):
        #People.__init__(self, name, age)    #此處People為hard coding
        super().__init__(name, age)    #此處super()相當於People，但不能再用self
        self.student_id = student_id

    def eat(self, food):    # method overriding
        print(f"{self.name} is eating {food}")


student_one = Student("James", 20, 1234)
print(student_one.age, student_one.student_id)

student_one.sleep()
student_one.eat("pizza")  # method overriding
