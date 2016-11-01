def valueSwap(door):
    if(door == 1):
        return 0
    else:
        return 1
        
doors = [0 for i in range(0, 100)]

for i in range (0,100):
    step = i+1
    for j in range(i, 100, step):
        doors[j] = valueSwap(doors[j])

for i in range(0, 100):
    if(doors[i] == 1):
        print("%d: open" % (i+1))
