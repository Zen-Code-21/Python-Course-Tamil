student = {"name" : "Jack", "Age" : 21, "Grade" : "A+"}

print(student["Grade"])

student["Age"] = 23

student["city"] = "Banglore"
print(student)


print(student.keys())
print(student.values())

student.clear()

student.pop("Age")
print(student)

