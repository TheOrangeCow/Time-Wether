from datetime import datetime

def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") 
    print(f"Current time: {current_time}")

def day():
    now = datetime.now()
    current_day = now.strftime("%A")
    print(f"Current day: {current_day}")

time()