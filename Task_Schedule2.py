import datetime
import schedule
import time

def Schedule_Second():
    print("Schedular Schedules after second...:")
    print("Current time is:",datetime.datetime.now())
    

def Schedule_Minute():
    print("Schedular Schedules after min...:")
    print("Current time is:",datetime.datetime.now())
    
def Schedule_Hour():
    print("Schedular Schedules after Hr...:")
    print("Current time is:",datetime.datetime.now())
    
def Schedule_Sunday():
    print("Schedular Schedules after Sunday...:")
    print("Current time is:",datetime.datetime.now())
    
    
def main():

    print("Automations using Python")
    
    schedule.every(1).seconds.do(Schedule_Second)
    
    schedule.every(1).minutes.do(Schedule_Minute)
    
    schedule.every(1).hour.do(Schedule_Hour)
    
    schedule.every().sunday.do(Schedule_Sunday)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
    
