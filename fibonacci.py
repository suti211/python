
values = list()

for i in range(0, 30):
    if i == 0:
        values.insert(i, 0)
    elif i == 1:
        values.insert(i, 1)
    elif i > 1:
        values.insert(i, values[i-1] + values[i-2])

    line = str(i) + '. ' + str(values[i])
    print(line)

    
