# python day 6 / 100
# rock paper scissors

import random

while True: 
  you = input("rock, paper or scissors? ")
  me = random.choice(["rock", "paper", "scissors"])

  print(f"\nYou = {you}")
  print(f"\nMe = {me}")

  if you == me:
    print("Draw!\n")
  elif (you == "rock" and me == "scissors") or (you == "paper" and me == "rock") or (you == "scissors" and me == "paper"):
    print("You Win\n")
  else:
    print("I Win L :) \n")