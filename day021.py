# day 21 / 100 python projects
# password strength checker

pw = input("Password: ")
score = 0

if len(pw) >= 8:
    score += 1
if pw != pw.lower(): # checking for uppercase letters
    score += 1
if pw != pw.upper(): # checking for lowercase letters
    score += 1

for letter in pw:
    if letter in "0123456789":
        score += 1
        break

print("\u2588" * score + "-" * (4 - score), f"{score}/4")