# IF ELSE
# Condition : >, <, ==, !=, >=, <=
# Logical Oprtaot : and, or, not
# and : c1 and c2 - both are true
# or : c1 or c2 - any one are true

p = int(input("Enter Your Percentage : "))

if (p <= 100) and (p >= 80):
    print("A")   #Block(statement)
elif p < 80 and p >= 60:
    print("B")
elif p < 60 and p >= 40:
    print("C")
elif p < 40 and p >= 33:
    print("D")
else:
    print("F")
