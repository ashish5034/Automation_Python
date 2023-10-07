import os
import psutil
from sys import *

def create_process_log(directory):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    log_file_path = os.path.join(directory, "process_log.txt")

    with open(log_file_path, "w") as log_file:
        log_file.write("Process Information:\n\n")

        for process in psutil.process_iter(attrs=['pid', 'name', 'username']):
            try:
                process_info = process.info
                pid = process_info['pid']
                name = process_info['name']
                username = process_info['username']

                log_file.write(f"Process Name: {name}\n")
                log_file.write(f"PID: {pid}\n")
                log_file.write(f"Username: {username}\n")
                log_file.write("-" * 40 + "\n")

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    print(f"Process log file '{log_file_path}' has been created.")

def main():
    print("Application name:",argv[0])
    
    if len(argv)!=2:
        print("Invalid number of Arguments:")
        exit()
        
    if argv[1] == "-h" or argv[1] == "-H":
        print("Application for showing running process ")
        exit()

    if argv[1] == "-u" or argv[1] == "-U":
        print("Usage: processInfo.py Notepad")
        exit()
        
    print("Process Monitor: ")

    create_process_log(argv[1])

if __name__ == "__main__":
    main()
