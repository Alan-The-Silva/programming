import time
import winsound

seconds = int(input("Enter time in seconds: "))
print("Alarm set.......")

time.sleep(seconds)

print("Time's up!")

#The first 1000 represent the frequence
#The second 1000 represent the seconds that the beet will last
winsound.Beep(1000,1000)