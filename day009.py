# day 9 of 100
# loading bar

import time

for i in range(1, 31):
  bar = "\u2588" * i
  #"u2588" is for the Unicode character █
  space = "-" * (30 - i)

  print(f"{bar}{space}{i * 100 // 30}%", end = "\r")
  time.sleep(0.08)

print("\n Access Granted")