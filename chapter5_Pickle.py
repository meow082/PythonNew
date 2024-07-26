import pickle

x = 10
y = [1, 2, 3, 4]

# with open("pickle_file", "wb") as p_file:
#     pickle.dump(x, p_file)  # 將x的值寫入p_file，serialize
#     pickle.dump(y, p_file)



with open("pickle_file", "rb") as p_file:
    x = pickle.load(p_file)   #deserialize
    y = pickle.load(p_file)
    print(x)
    print(y)