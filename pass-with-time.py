from datetime import datetime

print("passed")
print()

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time is: ", current_time)