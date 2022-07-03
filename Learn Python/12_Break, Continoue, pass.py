# Break
while True:
    name = input("Enter Your Name : ")
    if name != "":
        break;
print(name)

# Continue
pn = "123-456-7890"
for i in pn:
    if i == '-':
        continue
    print(i, end='')

# Pass
for i in range(1, 50+1):
    if i == 13:
        pass
    else:
        print(i ," ", end='')