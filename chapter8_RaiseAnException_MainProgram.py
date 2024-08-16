import chapter8_RaiseAnException as rae

try:
    #num = 30
    #num = -30
    num = "30"
    rae.enter_age(num)
except rae.NegativeNumberException as Error:
    print(Error)
    print("Please enter a valid age.")
except:
    print("Something went wrong...")