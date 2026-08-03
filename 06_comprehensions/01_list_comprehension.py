# [expression for item in iterable if condition]

# old way
old_squares = []
for x in range(5):
  if (x % 2 == 0):
    old_squares.append(x**2)

print(old_squares)

# comprehension way
new_squares = [x**2 for x in range(5) if x % 2 == 0]
print(new_squares)

menu = [
  "Coffee",
  "Iced Lemon Tea",
  "Green Tea",
  "Iced Peach Tea",
  "Ginger Tea"
]

iced_tea = [tea for tea in menu if "Iced" in tea]
len_char_tea = [my_tea for my_tea in menu if len(my_tea) >= 10]
print(iced_tea)
print(len_char_tea)

number = [num for num in [5, 7, 10, 9, 6] if num > 6]
print(number)
