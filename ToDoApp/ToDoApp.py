#####init
import sys

FILE_NAME = "todos.txt"
argumentNumber = len(sys.argv)
toDoList = []
completedList = []

def readFromFile():
    if len(toDoList) == 0:
        myFile = open(FILE_NAME, "r")
        for line in myFile:
                toDoList.append(line.split(",")[0])
                completedList.append(line.split(",")[1].strip("\n"))
        myFile.close()

def writeToFile():
    myFile = open(FILE_NAME, "w")
    for i in range(0, len(toDoList)):
            myFile.write("%s,%s\n" % (toDoList[i], completedList[i]))
    myFile.close()

def listFileContent():
    index = 0
    for i in range(len(toDoList)):
        if completedList[i] == "True":
            print("%d: %s %s" % (index+1, "[x]", toDoList[i]))
        else:
            print("%d: %s %s" % (index+1, "[ ]", toDoList[i]))
        index += 1

while True:

    while True:
        command = input("Please specifiy a valid command: [add, list, mark, archive, exit]")
        if(command == "add" or command == "list" or command == "mark" or command == "archive" or command == "exit"):
            break

    if command == "list":
        #list all todo

        readFromFile()

        listFileContent()

        #print(toDoList)
        #print(completedList)

    if command == "add":
        entry = input("Please enter your task (task, completed True|False)")
        toDoList.append(entry.split(",")[0])
        completedList.append(entry.split(",")[1])

        myFile = open(FILE_NAME, "a+")
        for i in range(0, len(toDoList)):
            myFile.write("%s,%s\n" % (toDoList[i], completedList[i]))
        myFile.close()

        print(toDoList)
        print(completedList)

    if command == "mark":
        #marks todo as completed
        readFromFile()
        listFileContent()
        marker= int(input("Which task would you like to mark as completed?: "))

        if completedList[marker-1] == "False":
            completedList[marker-1] = "True"
        else:
            completedList[marker-1] = "False"

        writeToFile()
        listFileContent()


    if command == "archive":
        readFromFile()
        listFileContent()
        #print(completedList)
        #print(toDoList)
        print("Removing all marked tasks...")

        #find and remove marked
        i = 0
        while i < len(toDoList):
            if completedList[i] == "True":
                del completedList[i]
                del toDoList[i]
            else:
                i += 1

        writeToFile()
        listFileContent()
    if command == "exit":
        break



