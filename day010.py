# python day 10 / 100
# dice roll

import random, time

for roll_number in range(5): # rolling the dice 5 times
  # randint picks a whole number, both ends included
  number = random.randint(1,6)

  print(f"roll {roll_number}: {number}")
  roll_number = roll_number + 1
  time.sleep(0.6)

print("roll again? run it again! ")