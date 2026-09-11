# day 8 / 100

# countdown timer

import time

seconds = int(input("countdown from: "))

while seconds > 0:
  print(f"{seconds}", end = "\r")

  time.sleep(1)
  seconds -= 1 # basically seconds = seconds - 1

print("Time's up!!!!")