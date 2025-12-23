
def is_greater_than_7(num):
    if(num > 7):
        return True
    else:
        return False
    
a = [3, 4, 45, 679, 569, 609, 6, 1, 2, 567890]

new_list = list(filter(is_greater_than_7, a))
print(new_list)


    
