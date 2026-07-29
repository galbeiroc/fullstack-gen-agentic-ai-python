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