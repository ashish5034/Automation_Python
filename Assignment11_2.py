from sys import *
import os
import hashlib

def hashfile(path, blocksize=1024):
    fd = open(path, 'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)
    fd.close()
    return hasher.hexdigest()

def findDuplicatefile(directory_path):
    flag = os.path.isabs(directory_path)

    if flag == False:
        directory_path = os.path.abspath(directory_path)

    exists = os.path.isdir(directory_path)

    filechecksum = {}
    dups = []

    if exists:
        for dirname,subdirname, filenames in os.walk(directory_path):
            for filename in filenames:
                file_path = os.path.join(dirname, filename)
                file_hash = hashfile(file_path)

                if file_hash in filechecksum:
                    dups.append(file_path)
                    # print(file_path)
                else:
                    filechecksum[file_hash] = file_path
        return dups
    else:
        print("Invalid Path")

def write_to_log_file(dups):
    """
    Write the names of duplicate files to a log file named 'log.txt' in the current directory.

    :param dups: List of duplicate file paths.
    """
    if not dups:
        print("No duplicate files found.")
        return
    else:
        with open("log.txt", "w") as log_file:
            log_file.write("Duplicate Files:\n")
            for path in dups:
                log_file.write(path + "\n")
                
                

def main():
    print("Duplicate file detector:")
    print("Application name:", argv[0])

    if len(argv) != 2:
        print("Invalid Number of Arguments:")
        exit()

    if argv[1] == "-h" or argv[1] == "-H":
        print("Application for showing duplicate files in a log")
        exit()

    if argv[1] == "-u" or argv[1] == "-U":
        print("Directoryname.py Demo")
        exit()

    try:
        dups = findDuplicatefile(argv[1])
        write_to_log_file(dups)
        print("Duplicate file names have been written to 'log.txt' in the current directory.")

    except ValueError:
        print("Error: Invalid data type of input")

    except Exception as E:
        print("Error: Invalid Input", E)

if __name__ == "__main__":
    main()
