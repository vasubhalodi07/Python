# Tuple - collection of data which is related data

student = ("Vasu", 19, "Male", "Dhruv", 23, "Male")
print(student.count("Vasu"))
print(student.index("Male"))

for i in student:
    print(i)

if "Vasu" in student:
    print("Vasu is Here..")
