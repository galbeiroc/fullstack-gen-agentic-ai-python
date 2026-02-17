vegetables = ("Tomates", "Onions", "Carrots")

vegetable1, vegetable2, vegetable3 = vegetables
print(f"Main vegetables: {vegetable1}, {vegetable2}, {vegetable3}")

garlic_ratio, potatoes_ratio = 2, 4
print(f"Garlic ratio: {garlic_ratio}, Patatoes ratio: {potatoes_ratio}")

# Swaping values
garlic_ratio, potatoes_ratio = potatoes_ratio, garlic_ratio
print(f"Garlic ratio: {garlic_ratio}, Patatoes ratio: {potatoes_ratio}")

# Membership testing
print(f"Is Garlic in vegetables? {'Garlic' in  vegetables}")
print(f"Is Carrots in vegetables? {'Carrots' in  vegetables}")
