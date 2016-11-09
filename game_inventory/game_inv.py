
# usage : display_inventory(dictionary)
# recieves a dictionary as parameter and prints out the contents of it,
# plus the sum of the values at the end.
##############################################################################
def display_inventory(inv):
    print("Inventory:")
    for key, value in inv.items():
        print("%d %s" % (value, key))
    print("Total number of items: %d" % (get_total_item_count(inv)))


# usage: get_total_item_count(dictionary)
# iterates through the given dictionary, and sums up its values, then returns
# it as an int.
##############################################################################
def get_total_item_count(inv):
    total = 0
    for value in inv.values():
        total += value
    return total
        

# usage: add_to_inventory(dictionary, list(strings only))
# checks if an item from the list, is present in the recieved dictionary,
# and increments its value, if not, then it adds it.
##############################################################################
def add_to_inventory(inv, added_items):
    for item in added_items:
        if item in inv:
            inv[item] += 1
        else:
            inv.update({item : inv.get(item, 0) + 1})


# usage: print_table(order) where order="" | "count,asc" | "count,desc"
# constructs a table, then sorts it based on the given arguments:
# count,asc = ascending
# count,desc = descending
# no parameter = default, unsorted
##############################################################################
def print_table(*order):
    table_width = len(max(inventory, key=len))
    print("Inventory:")
    print("{0:>{width}s}   {1:>{width}s}".format("count","item name", width = table_width))

    # we print out 2 times the length of the longest string because of the two
    # collumns plus we need to compensate for the three spaces between the 
    # spaceholders
    dash_line_len = table_width * 2 + 3
    print_dashline(dash_line_len)

    # converting dictionary to a list of tuples so we can sort it
    inv_list = [(key, value) for key, value in inventory.items()]

    if len(order) == 0:
        for i,j in inv_list:
            print("{0:>{width}d}   {1:>{width}s}".format(j, i, width = table_width))
        print_dashline(dash_line_len)
        
        print("Total number of items: %d" %(get_total_item_count(inventory)))

    # we sort the tuple list
    elif order[0] == "count,asc":
        inv_list = sorted(inv_list, key=lambda tup: tup[1])

        for i,j in inv_list:
            print("{0:>{width}d}   {1:>{width}s}".format(j, i, width = table_width))
        print_dashline(dash_line_len)

        print("Total number of items: %d" %(get_total_item_count(inventory)))

    # we reverse the sorting to get the descending list
    elif order[0] == "count,desc":
        inv_list = sorted(inv_list, key=lambda tup: tup[1], reverse=True)

        for i,j in inv_list:
            print("{0:>{width}d}   {1:>{width}s}".format(j, i, width = table_width))
        print_dashline(dash_line_len)

        print("Total number of items: %d" %(get_total_item_count(inventory)))
    else:
        print("invalid arg for print_table()")
        exit()
        
# prints out dashes,in the same line the length parameter determines how many.
##############################################################################
def print_dashline(length):
    for i in range(length):
        print("-", end="")
    print("\n")
            
# import loot from a csv file, and merges it with inventory dictionary
##############################################################################
def import_inventory(*filename):
    
    param_len = len(filename)
    file_to_read = ""

    if param_len == 0:
        file_to_read = DEFAULT_FILE_NAME
    elif param_len == 1:
        file_to_read = filename[0]
    else:
        print("egész nap fe sem álltam, te meg szar paraméterekkel akarod itt meghívni...")
        exit()

    inputPrompt = "File does not exist, should i create a template?(y/n)"
    loot_from_file = []
    try:
        loot_file = open(file_to_read, "r")
    except FileNotFoundError:
        if get_y_or_n(inputPrompt) == True:
            create_loot_template(file_to_read)
            print("Template created, go add some loot. Then run again!")
            exit()
        else:
            print("Create template file manually!")
    else:
        # reading in every line from file, then appending every line
        # as list, into another list, so we get the key value pairs in a
        # neat 2d list
        for line in loot_file:
            loot_from_file.append(line.strip().lower().split(","))

        # removing first element since it has no use at this point
        #(contains item name,count)
        del loot_from_file[0]

        # removing empty sublists from list, if we got any from file input
        i = 0
        while i < len(loot_from_file):
            # for debug
            print(loot_from_file[i])
            if len(loot_from_file[i]) == 1:
                del loot_from_file[i]
            i += 1

        # for debug
        print(loot_from_file)

        # since we have our loot from file in list of lists,
        # we iterate through the list of lists, and check if the
        # first element of the
        # sublist is present in the inventorys keys, if yes,
        # we add to its value the
        # second element of the sublist.
        # if the first element is not present in the keys of
        # the inventory, we add it as a key,
        # then we pair the second sublist element to it as value
        for i in range(len(loot_from_file)):
            if loot_from_file[i][0] in inventory:
                inventory[loot_from_file[i][0]] += int(loot_from_file[i][1])
            else:
                inventory.update({loot_from_file[i][0] : int(loot_from_file[i][1])})
        loot_file.close()
            

# usage: get_y_or_n(string)
# asks user for y or n input, returns true if input = y, returns false else        
##############################################################################      
def get_y_or_n(prompt):
    correctInput = False

    while not correctInput:
        choice = input(prompt)
        choice = choice.lower()

        if choice == "y" or choice == "n":
            correctInput = True
        else:
            print("Invalid input use y/n.")

    if choice == "y":
        return True
    else:
        return False

# creates a CSV file with a default line in it
# if no paramteres give it creates the default import_inventory.csv file
##############################################################################
def create_loot_template(*filename):
    file_to_create = ""
    if len(filename) == 0:
        file_to_create = DEFAULT_FILE_NAME
    elif len(filename) == 1:
        file_to_create = filename[0]
    else:
        exit()

    file = open(file_to_create, "w")
    file.write("item name,count")
    file.close()
          
# exports the current inventory into a file given in parameter, into
##############################################################################
def export_inventory(*filename):
    file_to_write = ""
    if len(filename) == 0:
        file_to_write = DEFAULT_FILE_NAME
    elif len(filename) == 1:
        file_to_write = filename[0]
    else:
        print("F you then...")

    try:
        loot_file = open(file_to_write, "w")
    except:
        print("lel?")
    else:
        loot_file.write("item name,count\n")
        for key, value in inventory.items():
            loot_file.write("%s,%d\n" % (key, value))
        
DEFAULT_FILE_NAME = "import_inventory.csv"

inventory = {"pocket fluff": 1}

print("This is our base inventory from file:\n")
import_inventory()
print_table("count,desc")

print("We slay a dargon, who was guarding a chest and find:\n")
print("2 gold coins, 1 dagger, 3 ruby, 1 rope")
dragon_loot = ["gold coin", "gold coin", "dagger", "ruby", "ruby", "rope", "ruby"]
add_to_inventory(inventory, dragon_loot)

print("This is our bag now:\n")
print_table("count,asc")

export_inventory()

