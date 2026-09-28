# day 24 / 100 python challenges
# caesar cipher

text = input("message: ").lower()
shift = 3
secret = ""

for letter in text:
    if letter in "abcdefghijklmnopqrstuvwxyz":
        pos = ord(letter) - ord("a") # a=0, b=1 ... z=25
        pos = (pos + shift) % 26  # wrap z around to a
        secret += chr(pos + ord("a"))
    
    else:
        secret += letter

print(secret)