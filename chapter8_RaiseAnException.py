class NegativeNumberException(RuntimeError):
    def __init__(self, age):
        super().__init__()    # Call the base class constructor 複習OOP課程
        self.age = age
        if age < 0:
            print("This is not a valid age.")


def enter_age(age):
    if age < 0:
        raise NegativeNumberException(age)

    if age % 2 == 0:
        print("Your age is even.")
    else:
        print("Your age is odd.")


# 在chapter8_RaiseAnException_MainProgram.py 執行