import os

file = open("myFile.txt")

print(file.read(5))  # return the first 5 characters(string) of the file
print(file.read())
file.seek(0)  # move the cursor to the beginning of the file
print(file.read())

file.seek(0)
print("********************")
print(file.readline())  # return the first line of the file including the newline (\n)
file.seek(0)
print("********************")
print(file.readlines())  # return a list of all the lines in the file


file.seek(0)
print("********************")
while True:     # 節省記憶體
    line = file.readline()
    if not line:
        break
    print(line)


file.close()    # 關閉檔案，釋放資源

print("----------------------------------------------------------")
with open("myFile.txt", mode="r") as my_file:   # 這樣寫可以不用寫file.close()，預設是r(read mode)，如果是a(append mode)的話，會發生錯誤
    all_content = my_file.read()
    print(all_content)

print("----------------------------------------------------------")
# os.remove("index.html")  # 刪除檔案
# os.rmdir("myFolder")  # 刪除資料夾