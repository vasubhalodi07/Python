# For Loop
# foor loop : limited size

for i in range(10):
    print(i+1)

for i in range(50,100+1,2):
    print(i)

for i in "Bro Code":
    print(i)

import time
for i in range(5,0,-1):
    print(i)
    time.sleep(1)
print("Happy New Year")

start = 20
contain = "Happy New Year"
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
for i in range(0,100+1,10):
    print(contain.center(start+i))
for i in range(90+1, 0, -10):
    print(contain.center(18+i))
