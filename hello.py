import sys


# this function returns a string, based on arguments given in command line
# if no arguments given it returns a "world" string
# with 1 argument, return the argument itself
# with 2 arguments returns the the two args in 1 string
# with 3 arguments or more we assume the user is bullshitting, and return the firs arg.
# if the arguments first letter is lowercase the code will try to switch it to uppercase with the .title() function
def sGetNameFromArgs():
    if(len(sys.argv) == 1):
        sPersonName = "World"
    elif((len(sys.argv) == 2) | (len(sys.argv) > 3)):
        sPersonName = sys.argv[1].title()
    elif(len(sys.argv) == 3):
        sPersonName = sys.argv[1].title() + " " + sys.argv[2].title()
    return sPersonName


# takes two strings as parameter, 1 word used to welcome,
# and 1 name to welcome, and returns these as a string.
def sConstructMessage(sWelcomeWord, sUserName):
    sMessage = sWelcomeWord + " " + sUserName + "!"
    return sMessage

# prints out the message 
print(sConstructMessage("Hello", sGetNameFromArgs()))





