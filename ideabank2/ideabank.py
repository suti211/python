# NOTE: 
# this code is volatile, and inefficient, because it reads in the whole file
# in the memory, then after modifications it's rewriting it.
# importing sys lib, to handle cli arguments, and os to reach some
# os level file managing functions

import sys
import os


#creating some references
ideas = []
highestID = 0
FILE_NAME = "ideas.txt"

# this function opens the file recieved in parameters, in writing mode
# then overwrites it with the contents of the "ideas" list.

def vWriteToFile(sFileName):
    with open(sFileName, "w") as file:
        for i in ideas:
            file.write("{0:s}".format(i + "\n"))

# this function reads from a file recieved in parameters, into a list
# where the lines are split at every "\n" new line character, this produces an empty
# "" char in the list, the .remove("") removes this.
# after this it returns the list.

def vReadFromFile(sFileName): 
    with open(sFileName, "r") as file:
        ideasArray = file.read().split("\n")
        ideasArray.remove("")
    return ideasArray


# if we dont have any cli arguments, this will be our default behaviour

if len(sys.argv) == 1:
    
    # main loop
    # its purpose to run the try: again if we run into an exception

    while True:
        # we try to check if the file is empty, if this fails, then we know that
        # it doesnt even exist. in this case we print a message, and create the file itself
        # in theory the file doesnt need to be closed because we did not stored any Reference
        # to it so it happens automatically

        try:
            if os.stat(FILE_NAME).st_size != 0:
                ideas = vReadFromFile(FILE_NAME)
            highestID = len(ideas) + 1
            break
        except FileNotFoundError:

            # if the file doesnt exists we create it.

            print("File not found, making file...")
            open(FILE_NAME,"w")

    # we append the new ideas to the ideas list, with a number, which is derived from
    # the length of the list, and write the whole list into file.

    ideas.append(input("What's your newest idea?: "))
    vWriteToFile(FILE_NAME)

    # printing out all of the ideas.

    print("Your ideabank: ")
    for i in range(0, len(ideas)):
        print("%d: %s.\n" % (i+1, ideas[i]))

# only check arguments if we even have to avoid errors

if len(sys.argv) > 1:
    
    # a little help message

    if (sys.argv[1] != "-ls") & (sys.argv[1] != "-rm") | (len(sys.argv) > 2):
        print("Usage: python ideabank.py or python ideabank.py -ls|-rm")

    # if the first argument is -ls we only read and list file content

    if sys.argv[1] == "-ls":
        try:
            ideas = vReadFromFile(FILE_NAME)
            print("Your ideabank: ")
            print("ID-Idea")
            for i in range(0, len(ideas)):
                print("%d: %s.\n" % (i+1, ideas[i]))
        except FileNotFoundError:
            print("There is no ideabank file yet, exiting. Run the program without arguments first.")
            exit()

    # if the first argument is rm, we get an id from the user
    # and remove it from the ideas list, then rewrite the file

    if sys.argv[1] == "-rm":
        
        try:
            ideas = vReadFromFile(FILE_NAME)
        except FileNotFoundError:
            print("There is no file to remove from yet, exiting. Run the program without arguments first.")
            exit()

        # controlled value input

        while True:
            try:
                rmID = int(input("Which idea you wish to remove?(ID): "))
                if (rmID >= 1) & (rmID <= len(ideas)):
                    break
            except:
                print("The value given is not a number, or invalid.")
            
        #remove value from ideas list

        try:
            del ideas[rmID-1]
        except:
            print("Failed to delete idea.")
        
        # rewrite file

        vWriteToFile(FILE_NAME)
