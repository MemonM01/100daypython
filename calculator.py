# Simple Calculator

print("Simple Calculator")
print("-" * 20)
print("Press q to quit")

while True:
  num1 = float(input("Number 1: "))
  if num1 == "q":
    break

  op = input("Operation (+ - * /): ")
  if op == "q":
    break

  num2 = float(input("Number 2: "))
  if num2 == "q":
    break

  if op == "+":
    print(f" = {num1 + num2}\n")
  elif op == "-":
    print(f" = {num1 - num2}\n")
  elif op == "*":
    print(f" = {num1 * num2}\n")
  elif op == "/":
    if num2 == 0:
      print("Can't divide by 0\n")
    else:
      print(f" = {num1 + num2}\n")
  else:
    print("Invalid operator\n")





    