# day 5 / 100

# division 

for n in range(1,101):

  # note % gives the remainder e.g: 15 % 3 = 0 means 15 is divisble by 3
  #.   // gives the floor division e.g: 10 // 3  will output 3

  if n % 15 == 0:
    print("FizzBuzz")
  elif n % 3 == 0:
    print("Fizz")
  elif n % 5 == 0:
    print("Buzz")
  else:
    print(n)