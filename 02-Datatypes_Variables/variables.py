# ------------------------------
# Rules for Naming Variables
# ------------------------------

# 1. Must start with a letter or underscore (_)
valid_name = 10
_validName = 20

# 2. Cannot start with a number
# 1value = 100   # This will cause an error

# 3. Can only contain letters, numbers, and underscores
student_name1 = "X"

# 4. Case-sensitive (different names)
Age = 21
age = 22
AGE = 23
print(Age, age, AGE)   # outputs: 21 22 23

# 5. Cannot use Python keywords (like if, for, class, etc.)
# if = 5    # This is Invalid
# class = "CS"  # This is Invalid

# ✅ Tip: Use meaningful variable names
marks = 95
x = 95  # works, but not clear                      
