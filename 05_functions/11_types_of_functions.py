def pure_function(x):
  return x * 2

total_sales = 0

def impure_function(x):
  global total_sales
  total_sales += 2

def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)

drinks = ["coffee", "tea", "juice", "water", "tea", "soda"]

filtered_drinks = list(filter(lambda drink: drink=="tea", drinks))
print(filtered_drinks)
