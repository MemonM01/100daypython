# day 27 / 100 python projects
# guess the word

import time

word = "series"

for end in range(1, len(word) + 1):
    piece = word[:end]
    print(piece)
    time.sleep(0.8)