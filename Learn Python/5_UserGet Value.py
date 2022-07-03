# User Get Value
# input() - use for get value for user
from numpy import longlong

first_name = input("First Name : ")
last_name = input("Last Name : ")
email = input("Email : ")
phonenumber = longlong(input("Phone Number : "))
birth_date = input("Birth Date : ")
gender = input("Gender : ")
name =  first_name.capitalize() + " " + last_name.capitalize()

print("Name : " + name)
print("Email : " + email)
print("Phone Number : " + str(phonenumber))
print("Birth Date : " + birth_date)
print("Gender : " + gender.capitalize())

