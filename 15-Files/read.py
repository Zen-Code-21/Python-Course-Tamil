#three important steps for file handling in python:
# 1 Opening a File
# 2 Performing operations on the File
# 3 Closing a File

f = open("zen.txt", "r")

content = f.read()
print(content)

f.close()