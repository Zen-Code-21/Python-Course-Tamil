
nums = [1,2,3,4,5]

def square(num):
    return num * num 

new_list = list(map(square, nums))
print(new_list)
