from another_module import one_func, two_func   #會把another_module.py轉成byte codes存在__pycache__資料夾裡
from myPackage import some_code, some_more_code
from myPackage.sub_package import happy_hello


def hello():
    print("Hello from chapter7_module.py!")


one_func()
two_func()
hello()

print("----------------------------------------------------")

some_code.some_code()
some_more_code.here_is_some_more()
happy_hello.small_hello()