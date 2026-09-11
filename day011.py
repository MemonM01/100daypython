# python day 11 / 100
# coin flip tracker

import random

heads = 0
tails = 0

for flip in range(100): # flipping the coin 100 times
  if random.choice(["H", "T"]) == "H":
    heads += 1
  else:
    tails += 1

print(f"Heads: {heads} times \n")
print(f"Tails: {tails} times")