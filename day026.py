# day 26 / 100 python projects
# receipt printer

items = ["Coffee", "Tea", "Croissant", "Orange Juice"]
prices = [2.80, 3.20, 2.50, 1.75]
total = 0

print("=" * 24)
print(f"{'CODE CAFE':^24}")  # ^ centers it
print("=")

for i in range(len(items)):
    print(f"{items[i]:<16}{prices[i]:>8.2f}")
    total += prices[i]

print("-" * 24)
print(f"{'Total':<16}{total:>8.2f}")