
values = list()
print("Fibonacci sequence:")
rows = int(input("How many lines do you want? "))

for i in range(0, rows):
    if i == 0:
        values.insert(i, 0)
    elif i == 1:
        values.insert(i, 1)
    elif i > 1:
        values.insert(i, values[i-1] + values[i-2])

    line = str(i+1) + '. ' + str(values[i])
    print(line)

    
