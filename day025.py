# day 25 / 100 python projects
# cipher breaker

import time 

secret = "wkh sdvvzrug lv fkhhvh"

for shift in range(1,26):
    attempt = ""
    for letter in secret:
        if letter == " ":
            attempt += " "
        else:
            pos = (ord(letter) - ord("a") - shift) % 26
            attempt += chr(pos + ord("a"))
    print(f"{shift:>2} {attempt}")
    time.sleep(0.1)