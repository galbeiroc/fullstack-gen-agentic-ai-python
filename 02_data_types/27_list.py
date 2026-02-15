ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are {ingredients}")

ingredients.remove("milk")
print(f"Ingredients are {ingredients}")

spice_options = ["ginger", "cardamon"]
ingredients.extend(spice_options)
print(f"Chai Ingredients: {ingredients}")

print(f"The water is the position: {ingredients[0]}")

ingredients.insert(1, "milk")
print(f"Chai with milk ingredients: {ingredients}")

last_ingredient = ingredients.pop()
print(f"Last ingredient: {last_ingredient}")
print(f"Chai Ingredients: {ingredients}")

ingredients.reverse()
print(f"Reversed ingredients {ingredients}")

ingredients.sort()
print(f"Sorted ingredients {ingredients}")

sugar_levels = [2, 5, 1, 4, 3]
print(f"Max sugar levels: {max(sugar_levels)}")
print(f"Min sigar level: {min(sugar_levels)}")
print(f"Total sugar levels: {sum(sugar_levels)}")

print(f"Slicing sugar levels: {sugar_levels[0:3]}")
print(f"Slicing sugar levels: {sugar_levels[2:]}")
print(f"Slicing sugar levels: {sugar_levels[:2]}")
print(f"Slicing sugar levels: {sugar_levels[1:4:2]}")