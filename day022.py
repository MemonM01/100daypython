# 22 / 100 python projects
# type writer effect

import time

message = "welcome to the page, daily python challenges"

for letter in message:
    # end = "" stops print adding a new line after every letter
    print(letter, end = "", flush = True)
    time.sleep(0.05)

print()