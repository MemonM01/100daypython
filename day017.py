# python projects day 17 / 100
# vowel counter

text = input("Type anything: ")

for vowel in "aeiou":
    n = text.count(vowel)
    print(vowel, n)

print("total letters: ", len(text))