essential_spices = {"cardamon", "ginger", "cinnamon"}
optional_spices = {"cloves", "black pepper", "ginger"}

# Union |
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

# Intersection &
common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

# Difference -
only_essential_spice = essential_spices - optional_spices
print(f"Only essential spices: {only_essential_spice}")

# Symmetric Difference ^
exclusive_spices = essential_spices ^ optional_spices
print(f"Exclusive spices: {exclusive_spices}")

# Membership
print(f"Is cloves in essentials spices {'cloves' in essential_spices}")
print(f"Is cloves in optional spices {'cloves' in optional_spices}")