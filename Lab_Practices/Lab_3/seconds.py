seconds = int(input("enter the no.of.seconds: "))
hour = seconds / 3600
minutes = (seconds % 3600) // 60
rem_sec = (seconds % 3600) % 60

print(f"{hour} hours,{minutes} minutes, and {rem_sec} seconds")
