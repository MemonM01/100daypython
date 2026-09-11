# day 13 / 100 python projects
# mood tracker

moods = ["ok", "tired", "great", "great", "dead", "tired", "great"]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for i in range(7):
  print(days[i], "-", moods[i])

#.count() tells u how many times a value appears
print("\nGood days: ", moods.count("great"))
print("Tired days: ", moods.count("tired"))