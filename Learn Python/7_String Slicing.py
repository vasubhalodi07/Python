# slicing : create a substring
# slice() - [start : stop : step]
# slice - use for remove or delete same poisition of string

name = "Vasu Bhalodi"
first_name = name[0:4]
last_name = name[5:12]
name1 = name[0:12:2]
reverse_name = name[::-1]
print(reverse_name)

website = "http://google.com"
slice = slice(7,-4)
print(website[slice])