# Integer
black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams: {total_grams}") # 17

remaing_tea_grams = black_tea_grams - ginger_grams
print(f"Remaining tea grams: {remaing_tea_grams}") # 11

milk_litres = 7
serving = 4
milk_per_serving = milk_litres / serving
print(f"Milk per serving: {milk_per_serving}") # 1.75

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"Bags per pot: {bags_per_pot}") # 1

total_cadamon_pods = 10
pods_per_cup = 3
letfover_pods = total_cadamon_pods % pods_per_cup
print(f"Letfover pods: {letfover_pods}") # 1

base_flavor_strength = 2
scale_factor = 3
flavor_strength = base_flavor_strength ** scale_factor
print(f"Flavor strength: {flavor_strength}") # 8


total_tea_leaves_harvested = 1_000_000_000
print(f" Tea leaves harvested: {total_tea_leaves_harvested}") # 1000000000
