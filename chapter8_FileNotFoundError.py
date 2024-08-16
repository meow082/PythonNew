# FileNotFoundError: This error occurs when a file is not found.
# with open("hello.exe") as file:
#     print(file.read())



# 處理方式
try:
    with open("hello.exe") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")



print(dir(__builtins__))    # 列出所有內建的例外，不須import