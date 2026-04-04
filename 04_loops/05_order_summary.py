names = ["Albeiro", "Liam", "Alice", "Veroco"]
bills = [50, 75, 100, 60]

for name, amount in zip(names, bills):
  print(f"{name} paid ${amount} dollars")