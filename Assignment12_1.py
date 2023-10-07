import psutil

def ProcessDisplay():
    listprocess = []
    for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
        try:
            pinfo = proc.info
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return listprocess

def displayLogfile(listprocess):
    if not listprocess:
        print("No processes are running.")
        return
    
    with open("process.txt", "w") as logfile:
        logfile.write("Running Processes:\n")
        for proc in listprocess:
            logfile.write(f"PID: {proc['pid']}, Name: {proc['name']}, Username: {proc['username']}\n")

def main():
    print("Process Monitor:")
    listprocess = ProcessDisplay()
    
    icnt = 0
    for process in listprocess:
        icnt += 1
        print(process)
    
    print("Number of processes running: ", icnt)
    
    displayLogfile(listprocess)
    
    print("Running process are also print in process.txt file")
    
if __name__ == "__main__":
    main()
