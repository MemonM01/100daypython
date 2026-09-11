#day 14 / 100
# timetabless

import time

n = int(input("Which times tables? "))

for i in range (1, 13):
    print(f"{i} x {n} = {i * n}")
    time.sleep(0.3) # you dont need this, this is just so it prints it slowly
    

print(f"Done, thats the {n} times table.")