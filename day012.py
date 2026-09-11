# day 12 / 100

sleep = [7,5,8,4,9,6,8]
names = ["Mon", "Tue" , "Wed", "Thu", "Fri", "Sat", "Sun"]

for i in range(7):
  print(names[i], "\u2588" * sleep[i])

print("total:", sum(sleep), "hours")
