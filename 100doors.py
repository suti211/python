# this function gets a list index, which is 1 or 0, then swaps up the value
def valueSwap(door):
    if(door == 1):
        return 0
    else:
        return 1
        
# creating a list with 100 elements, all 0's' 
# where the 0 means a closed door, 1 means open.       
doors = [0 for i in range(0, 100)]

# toggles all doors at first iteration, then
# it jumps to the i. iteration numbered element, and toggles it,
# then jumps forward i+1 and toggles it
for i in range (0,100):
    for j in range(i, 100, i+1):
        doors[j] = valueSwap(doors[j])

# prints out open doors only
for i in range(0, 100):
    if(doors[i] == 1):
        print("%d: open" % (i+1))