# day 7 / 100 python projects
# number guessing game

import random

secret = random.randint(1, 100)
tries = 0

print("Try guess the number, im thinking of a number between 1 and 100")

while True: # this loops forever untill something breaks the loop
  guess = int(input("Your guess: "))
  tries += 1 # same as tries = tries + 1

  if guess < secret:
    print("The number is higher")
  elif guess > secret:
    print("The number is lower")
  else:
    print(f"You got the number in {tries} attempts")
    break # this stops the loop