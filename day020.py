# python series day 20 / 100
# palindrome checker POPULAR Interview question

text = input("word or phrase: ").lower() # making the input lowercase

# strip out spaces:
clean = text.replace(" ", "")

if clean == clean[::-1]:    
    print("Palindrome. Same both ways!")
else: 
    print("Nope! not a palindrome")
    print(clean)
    print(clean[::-1])