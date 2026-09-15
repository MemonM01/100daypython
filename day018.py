# day 18 / 100 python projects

#word counter

text = input("Paste some text: ")

words = text.split() # this splits the text where ever there is a space

print("words: ", len(words))
print("characters: ", len(text))

longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word

print("longest word: ", longest)