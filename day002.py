# python day 2/100
# tip and bill splitter

bill = float(input('Bill total? '))
tip = float(input('Tip percent? '))
people = int(input('How many people? '))

total = bill * (1 + tip / 100)
each = total / people

print(f"Each person pays £{each:.2f}")