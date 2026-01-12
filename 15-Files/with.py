
# f = open("zen.txt", "r")
# content = f.read()
# print(content)
# f.close()

with open("zen.txt", "r") as f:
    content = f.read()
    print(content)
    #the best advantage of using with is that the file is closed by default, so there is no need to write f.close()