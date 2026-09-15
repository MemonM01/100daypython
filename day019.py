# python series day 19 / 100

# initials maker

name = input("Your full name: ")

initials = ""

for word in name.split():
    # word[0] is the first letter of that word
    initials += word[0].upper() + "."

print(initials)