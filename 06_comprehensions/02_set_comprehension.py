favorite_drinks = [
  "coffee", "tea", "juice", "milk", "coffee", "juice", 'water', "milk"
]

unique_drinks = { drink for drink in favorite_drinks }
print(unique_drinks, type(unique_drinks))

recipes = {
  "coffee": ["latte", "milk", "water", "sugar"],
  "tea": ["green tea", "sugar", "water"],
  "lemonade": ["lemon", "water", "sugar", "ice"]
}

unique_recipe = {drink for ingredients in recipes.values() for drink in ingredients}
print(unique_recipe)

colors = ["red", "blue", "red", "yellow", "green", "blue", "orange"]

unique_colors = { color for color in colors}
print(unique_colors)

ages = {
  "child": [10, 8, 6, 7, 6, 4, 4],
  "adolecent": [12, 15, 16, 17, 17, 16],
  "adult": [33, 28, 26, 28, 33, 27]
}

unique_ages = {age for type_ages in ages.values() for age in type_ages}
print(unique_ages)
