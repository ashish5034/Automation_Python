# It imports the sys module to access command-line arguments.
from sys import *
# It defines the main() function, where the main logic of the script resides.
def main():
    print("------------Automation Script------------")
    
    print("Automation Script name : ",argv[0])
# It checks the number of command-line arguments using len(argv). If there are only two arguments, it further checks for specific options:
    if (len(argv) == 2):
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
# If there are not exactly three arguments (script name + two numbers), it prints an "Invalid Number of Arguments" error message and exits.         # 
    if (len(argv)!=3):
        print("Invalid Number of Arguments")
        exit()
# Finally, it ensures that the main() function is executed only if the script is run directly (not imported as a module).
if __name__ == "__main__":
    main()