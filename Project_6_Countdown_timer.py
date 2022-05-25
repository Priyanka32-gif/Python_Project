import time

sec = input("Enter the time in seconds for countdown: ")
sec = int(sec)

def countdown(sec):
    while sec > 0:
        min, sec = divmod(sec, 60)
        
        print("min:", min, "sec:", sec)
        time.sleep(1)
        sec -= 1

    print("Time's up!")

countdown(sec)
