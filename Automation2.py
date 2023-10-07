from sys import * #It imports the sys module to access command-line arguments.

def Addition(No1, No2):#It defines a Addition(No1, No2) function that takes two arguments and returns their sum.
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():#It defines the main() function, where the main logic of the script resides.
    print("------------Automation Script------------")
    # It prints a header indicating that it's an automation script and displays the script's name using argv[0], which is the name of the script itself.
    print("Automation Script name : ",argv[0])

    if (len(argv) == 2):#It checks the number of command-line arguments using len(argv). If there are only two arguments, it further checks for specific options:
# If the second argument is -h or -H, it prints a help message and exits.
        if(argv[1] == "-h" or argv[1]=="-H"):  #flag for displaying help
            print("The automation script is used to perform addition of two number")
            exit()
# If the second argument is -u or -U, it prints a usage message and exits.
        elif(argv[1] == "-u" or argv[1] == "-U"):  #flag for displaying usage of script
            print("Usage : Name_of_script First_Argument Second_Argument")
            print("Example: Demo.py 11 10")
            exit()
# If none of the above options match, it prints an error message and exits.
        else:
            print("There is no such option to handle")
            exit()
# If there are not exactly three arguments (script name + two numbers), it prints an "Invalid Number of Arguments" error message and exits.
    if (len(argv)!=3):
        print("Invalid Number of Arguments")
        exit()
# If there are three arguments, it calls the Addition function with the two numbers (parsed as integers) and prints the result.
    else:
        Ret = Addition(int(argv[1]),int(argv[2]))
        print("Addition Is : ",Ret)

if __name__ == "__main__":
    main()