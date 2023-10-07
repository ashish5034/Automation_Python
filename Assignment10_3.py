import os
from sys import *
import shutil

def copy_files(source_dir, dest_dir):
    
    # Check if the source directory exists
    # if not os.path.exists(source_dir):
    #     print("Error: Source directory does not exist.")
    #     return

    # # Create the destination directory if it doesn't exist
    # if not os.path.exists(dest_dir):
    #     os.makedirs(dest_dir)

    flag = os.path.isabs(source_dir)
    
    if flag == False:
        source_dir = os.path.abspath(source_dir)
        
    exist = os.path.isdir(source_dir)
    if exist:
    # Iterate through the files in the source directory
        for foldername, subfoldername, files in os.walk(source_dir):
            for file in files:
                source_path = os.path.join(foldername, file)
                dest_path = os.path.join(dest_dir, file)
                shutil.copy2(source_path, dest_path)
                print(f"Copied: {source_path} -> {dest_path}")


def main():
    print("Automation Script to Copy Files between Directories")
    
    print("Application name is :",argv[0])
    
    if(argv[1]=="-h" or argv[1]=="-H"):
        print("Automation Script to Rename Files by Extension")
        exit()
        
    if(argv[1]=="-u" or argv[1] == "-U"):
        print("Usage:DirectoryName.py")
        print("Demo .txt .py")
        exit()
      
    if(len(argv) != 3):
        print("Invalid number of argument")
        exit()  
    
    try:
        copy_files(argv[1],argv[2])
        
    except ValueError:
        print("Error:Invalid Input:")
        
    except Exception as E:
        print("Error: Invalid input",E)
        
if __name__ == "__main__":
    main()



# It defines a function copy_files that takes two parameters: source_dir (the source directory containing files to copy) and dest_dir (the destination directory where files will be copied).

# Inside this function, it checks if the source directory exists using os.path.exists().

# It creates the destination directory using os.makedirs() if it doesn't already exist.

# It uses os.walk() to traverse the source directory and its subdirectories. For each file encountered, it constructs source and destination paths and copies the file using shutil.copy2().

# In the main() function, it prompts the user to enter the source and destination directory names.

# It calls the copy_files function with the provided directory names.

# To use this script:

# Save it as a .py file, e.g., copy_files_between_directories.py.
# Run the script using Python.
# Enter the source directory name (from which files will be copied) and the destination directory name (where the copied files will be placed) when prompted.
# The script will copy all files from the source directory to the destination directory, creating the destination directory if it doesn't already exist.
