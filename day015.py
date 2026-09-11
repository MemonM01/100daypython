# day 15 / 100 
# name reverser - common interview style question

name = input("Your naame: ")

# [::-1] means go through it one step at a time backwards

backwards = name[::-1]

print("Forwards: ", name)
print("Backwards: ", backwards)
print("You can capitalize it aswell: ", backwards.capitalize())