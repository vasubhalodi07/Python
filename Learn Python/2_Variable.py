# Variable
# In Python dont declare a data types of var
# convert to int to string then use a str(var)
# could not use a int and string at same print without convert a int to string
# check data type using type function
# float data type doesn't store decimal no
# datatype = string, int, float, boolean

first_name = "Vasu"
last_name = "Bhalodi"
name = first_name + " " + last_name
age = 19
height = 230.5

print("Name : " + name)
print("Age : " + str(age))
print("Height : " + str(height) + " cm")
print(type(name))

# Multiple Variable
a = b = c = d = 30
print(a, b, c, d)