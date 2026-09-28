# day 28 / 100 python projects
# hang man

import random

word = random.choice(["python", "terminal", "computer", "variable"])
guessed = ""
lives = 5

while lives > 0:
    clue = ""
    for letter in word: 
        if letter in guessed:
            clue += letter + " "
        else:
            clue += "_ "
    print(clue, " lives: ", "\u2665" * lives)
    if "_" not in clue:
        print("You win!")
        break
    guess = input("letter: ").lower()
    guessed += guess
    if guess not in word:
        lives -= 1

if lives == 0:
    print("The word was: ", word)