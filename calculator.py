# please ignore the many print commands, its just aesthetics for the console output
# and some help text for the firs time users
print("------------------------------------")
print("This is a simple claculator, it will ask for 2 numbers, then for an operator, to determine which operation to do with them.")
print("If any character or letter is given instead of an operator, the program will terminate.(You)")
print("The usable operators are the following: ")
print("------------------------------------")
print(" + for adding ")
print(" - for subtraction")
print(" / for division ")
print(" * for multiplying ")
print(" ** for powering ")
print("------------------------------------")


# string list for a lil' bit easier modification
sText = "Enter your number: "
sOpText = "Enter the operator: "
sOpError= "Invalid Operator, exiting..."

# main loop
while(True):
        # asking for a number from the user, and casting it to float, if the casting fails, the break interrupts the loop
        try:   
                fNumber1 = float(input(sText))
        except ValueError:
                break

        # asking for an operator from the user, and storing it for later use
        sOperator = input(sOpText)

        # checking if the operator given by the user is acceptable or not
        # if not, we send a message (a cut horsehead maybe), then break the loop
        if(sOperator != "+") & (sOperator != "-") & (sOperator != "/") & (sOperator != "*") & (sOperator != "**"):
                print(sOpError)
                break

        # asking for a number from the user, and casting it to float, if the casting fails, the break interrupts the loop
        try:   
                fNumber2 = float(input(sText))
        except ValueError:
                break


        # here we decide what each operator does with the given numbers, then storing the result in a variable.
        result = 0

        if(sOperator == "+"):
                result = fNumber1 + fNumber2

        if(sOperator == "-"):
                result = fNumber1 - fNumber2

        if(sOperator == "/"):
                result = fNumber1 / fNumber2

        if(sOperator == "*"):
                result = fNumber1 * fNumber2
        
        if (sOperator == "**"):
                result = fNumber1 ** fNumber2

        #all we got to do is some printing, printing the "equation" and the result, with some aesthetics.
        print("\n{0:.3f} {1:s} {2:.3f} = {3:.3f}\n".format(fNumber1, sOperator, fNumber2, result))
        print("------------------------------------")

