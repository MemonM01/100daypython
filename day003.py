# python day 3 / 100
# how long have you been alive? 

name = input("What is your name? ")
age = int(input("How old are you? "))

days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(name)
print(f"You have been alive for {days} days!")
print(f"{hours} hours!")
print(f"{minutes} minutes!")
print(f"{seconds} seconds!")
             
