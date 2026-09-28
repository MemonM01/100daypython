# day 23 / 100 python projects
# checking prime number or not

num = int(input("Enter your number: "))
is_prime = True

if num < 2:
    is_prime = False

for i in range(2, num):
    if num % i == 0:
        is_prime = False

if is_prime:
    print(num, "is PRIME")
else:
    print(num, "is NOT prime")