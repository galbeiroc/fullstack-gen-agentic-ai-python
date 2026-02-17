computer_order = dict(type="laptop", size=14, vendor="hp")
print(f"Computer order: {computer_order}")

user_profile = {}
user_profile['name'] = "galbeiroc"
user_profile['role'] = "admin"
user_profile["years_exp"] = 5
print(f"User profile: {user_profile}")
print(f"User name {user_profile['name']}")

del user_profile['years_exp']
print(f"User profile: {user_profile}")

print(f"User profile (keys): {user_profile.keys()}")
print(f"User profile (values): {user_profile.values()}")
print(f"User profile (items): {user_profile.items()}")

last_item = computer_order.popitem()
print(f"Last item: {last_item}")
print(f"Computer order: {computer_order}")

new_user_properties = {"skills": ["JS", "Python"], "email": "test@email.com"}
user_profile.update(new_user_properties)
print(f"Update user profile: {user_profile}")

getting_user_password = user_profile.get("password", "default_password")
print(f"Getting user password: {getting_user_password}") 

# Membership
print(f"Is name in user_profile? {'name' in user_profile}")
