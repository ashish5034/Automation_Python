from sys import *
import os
import hashlib
import time
from datetime import datetime
import schedule

# def deleteDuplicateFiles(dups):
#     for path in dups:
#         os.remove(path)

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
        for dirname, subdirname, filenames in os.walk(directory_path):
            for filename in filenames:
                file_path = os.path.join(dirname, filename)
                file_hash = hashfile(file_path)

                if file_hash in filechecksum:
                    dups.append(file_path)
                else:
                    filechecksum[file_hash] = [file_path]
        return dups
    else:
        print("Invalid Path")

def write_to_log_file(dups):
    """
    Write the names of duplicate files to a log file with the current date and time in the filename.

    :param dups: List of duplicate file paths.
    """
    if not dups:
        print("No duplicate files found.")
        return

    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"log_{current_datetime}.txt"

    with open(log_filename, "w") as log_file:
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
        print(datetime.now())
        duration_minutes = int(input("Enter duration in minutes: "))
        if duration_minutes <= 0:
            print("Invalid duration. Please enter a positive number of minutes.")
            exit()

        while True:
            
            starttime = time.time()
            print("Start time is: ", starttime)
            dups = findDuplicatefile(argv[1])
            write_to_log_file(dups)
            # deleteDuplicateFiles(dups)
            endtime = time.time()
            print("End time is: ", endtime)
            print("Duplicate file names have been written to 'log.txt' in the current directory.")
            print('Took %s seconds to evaluate.' % (endtime - starttime))
            
            # schedule.every(1).minutes.do(findDuplicatefile)
            print(f"Waiting for {duration_minutes} minutes before checking again...")
            time.sleep(duration_minutes * 60)  # Convert minutes to seconds

    except ValueError:
        print("Error: Invalid data type of input")

    except Exception as E:
        print("Error: Invalid Input", E)

if __name__ == "__main__":
    main()