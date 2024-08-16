try:
    lst = [1, 2, 3]
    print(lst[3])   # IndexError: list index out of range
except KeyError:    # 抓不到KeyError，所以不會執行
    print("There is a KeyError.")
except LookupError:     
    print("There is a LookupError.")
except IndexError:      # 此Error繼承LookupError，會被上面的LookupError抓到，所以不會執行
    print("There is an IndexError.")