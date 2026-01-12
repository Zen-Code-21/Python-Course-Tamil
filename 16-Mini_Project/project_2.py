import random
import string

# val = random.choice(['a', 'b', 'c'])
# print(val)

values = string.ascii_letters + string.digits + string.punctuation
pass_len = int(input("Enter the length of your password: "))

password = ""
for i in range(pass_len):
    password += random.choice(values)

print("Your password is : ", password)

# print(string.punctuation)