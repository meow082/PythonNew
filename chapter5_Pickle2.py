import pickle

# x = 10
# y = 100
# my_list = [1, 2, 3, 4, 5, 9]

# def save_data():
#     global x, y, my_list
#     data = {'x': x, 'y': y, 'my_list': my_list}

#     with open("my_pickle_file", "wb") as p_file:
#         pickle.dump(data, p_file)


# save_data()


print("------------------------------------------------------------")

x = None
y = None
my_list = None

def restore_data():
    global x, y, my_list
    with open("my_pickle_file", "rb") as p_file:
        data = pickle.load(p_file)     #得到剛才存進的dictionary
        x = data['x']
        y = data['y']
        my_list = data['my_list']


restore_data()
print(x, y, my_list)