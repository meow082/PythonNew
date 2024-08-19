def new_decorator(original_func):
    def wrap_func():
        print("Here is some code before the original function")
        original_func()
        print("Here is some code after the original function")
    return wrap_func

@new_decorator  # 這樣就是Decorator的用法
def func_needs_decorator():
    print("I am a function that needs a decorator")

func_needs_decorator()


# 沒有Decorator的情況
# decorated_function = new_decorator(func_needs_decorator)
# decorated_function()