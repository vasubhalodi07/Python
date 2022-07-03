# Nested Loop : One Loop Inside Other Loop

rows = int(input("Rows : "))
column = int(input("Column : "))
symbol = input("Symbol : ")

for i in range(rows):
    for j in range(column):
        print(symbol, end="")
    print()
