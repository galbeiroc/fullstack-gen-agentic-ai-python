# Full stack generative and Agentic AI with python

## Python

### What is Python?

Python is a high-level, interpreted programming language widely recognized for its simplicity and readability. Created by Guido van Rossum and first released in 1991, it has become one of the most popular languages in the world due to its versatility and beginner-friendly syntax

### Virtual Environment

A virtual environment in Python is an isolated directory that contains its own Python interpreter, standard library, and a set of installed packages. It allows you to manage dependencies for different projects separately, preventing version conflicts and keeping your global system Python clean.

Create virtual env
`python3 -m venv venv`

Activate virtual env
`source venv/bin/activate`

Deactivate virtual env
`deactivate`

| Traditional Way | Modern Way |
| --------------- | ---------- |
| venv            | uv         |

To install the packages listed in a `requirements.txt` file. The _-r_ or _--requirement_ flag tells pip to install from the specified requirements file.
`pip install -r requirements.txt`

### Data Types

#### Mutable and Immutable

Everything is object in Python.

Object -> identity -> value -> type
**_Note:_** Never check with the value. Check with the identity.

**Mutable:** Is Changeable.

```python
spice_mix = set()
print(f"Initial spice mix: {id(spice_mix)}") # Initial spice mix: 4311179424

spice_mix.add("Ginger")
spice_mix.add("Cardamom")
print(f"After spice mix: {id(spice_mix)}") # After spice mix: 4311179424
```

**Immutable:** Is Not Changeable. Change the reference.

```python
sugar_amount = 2
print(f"Initial sugar amount: {sugar_amount}")

sugar_amount = 12
print(f"Second Initial sugar amount: {sugar_amount}")


print(f"ID of 2: {id(2)}") # ID of 2: 4368924944
print(f"ID of 12: {id(12)}") #ID of 12: 4368925264
```

The whole concept of mutable and immutable is what value can change and what cannot change in the _memory itself_.

#### Numbers

Numbers aren't just one single thing; they are categorized based on whether they have decimals or how they are used.

**Integers** These are whole numbers, positive or negative, without decimals.

```python
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
```

**Floor division** divides two numbers and rounds the result down to the nearest whole number.

```python
total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"Bags per pot: {bags_per_pot}") # 1.75 => 1
```

Boolean -> `True` === 1 or `False` === 0
Real: Float - Decimal -> `15.5`
Complex Number - Fraction -> `3 + 5j`

**Module operator** The module operator is surprisingly useful in real-world codin. Give us the remainder of the division.

```python
total_cadamon_pods = 10
pods_per_cup = 3
letfover_pods = total_cadamon_pods % pods_per_cup
print(f"Letfover pods: {letfover_pods}") # 1
```

**Exponencial Operator** The exponentiation operator is represented by two asterisks: `**`.

```python
base_flavor_strength = 2
scale_factor = 3
flavor_strength = base_flavor_strength ** scale_factor
print(f"Flavor strength: {flavor_strength}")
```

**Visual Readability (Underscores)** You can't use commas because they separate items in a list. Instead, you use underscores (\_).

```python
total_tea_leaves_harvested = 1_000_000_000
print(f"Tea leaves harvested: {total_tea_leaves_harvested}")  # Output: 1000000000
```

#### Boolean

Boolean is a data type that can only have one of two values: `True` or `False`. Boolean is case senstive, lowercase will cause an error.

```python
is_boiling = True
stri_count = 5
print(f"Total actions: {is_boiling + stri_count}") # Total actions 6

milk_present = 0
print(f"Is there milk? {bool(milk_present)}") # Is there milk? False
```

##### Logical Operators

You can combine Booleans to create more complex logic.

- `and`: Returns True only if both sides are true.
- `or`: Returns True if at least one side is true.
- `not`: Reverses the result (True becomes False).

```python
is_sunny = True
is_warm = False

print(is_sunny and is_warm) # False (because it's not warm)
print(is_sunny or is_warm)  # True (because at least one is true)
print(not is_sunny)         # False
```

##### Comparison Operators

Most Booleans are created when you compare two values.

| Operator | Meaning          | Example  | Result  |
| :------- | :--------------- | :------- | :------ |
| `==`     | Equal to         | `5 == 5` | `True`  |
| `!=`     | Not equal to     | `5 != 3` | `True`  |
| `>`      | Greater than     | `5 > 10` | `False` |
| `<`      | Less than        | `5 < 10` | `True`  |
| `>=`     | Greater or equal | `5 >= 5` | `True`  |
| `<=`     | Less or equal    | `3 <= 2` | `False` |

#### Strings

a String (str) is how we handle text.
**Single quotes**: `'Hello'`
**Double quotes**: `"Python is fun"`
**Triple quotes**: `'''This is a multi-line string'''` (Useful for long paragraphs or documentation).

```python
chai_type = "Ginger chai"
customer_name = "Almendra"

print(f"Order for {customer_name} : {chai_type} please!")

print(f"{customer_name[0]}") # A

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[0:8]}") # First word: Aromatic
print(f"Last word: {chai_description[12:]}") # Last word Bold
print(f"Jump word: {chai_description[0:8:3]}") # jump each character 3 'Ami'

print(f"Reverse string {chai_description[::-1]}") # Reverse string dloB dna citamorA

label_text = "Spécial Character"
enconded_text = label_text.encode("utf-8")
print(f"None Encoded text: {label_text}") # Spécial Character
print(f"Encoded text: {enconded_text}") # b'Sp\xc3\xa9cial Character'
print(f"Decoded text: {enconded_text.decode('utf-8')}") # Spécial Character
```

##### String Methods

| Method       | What it does                 | Example                                   |
| :----------- | :--------------------------- | :---------------------------------------- |
| `.upper()`   | Makes everything uppercase   | `"hi".upper()` -> `"HI"`                  |
| `.lower()`   | Makes everything lowercase   | `"HI".lower()` -> `"hi"`                  |
| `.strip()`   | Removes whitespace from ends | `"  cool  ".strip()` -> `"cool"`          |
| `.replace()` | Swaps text                   | `"Java".replace("J", "P")` -> `"Pava"`    |
| `.split()`   | Breaks string into a list    | `"a,b,c".split(",")` -> `['a', 'b', 'c']` |

##### f-Strings (The Best Way to Format)

The most modern and readable way to put variables inside strings is using f-strings (formatted strings). Just put an f before the quotes and use {} for your variables.

```python
ame = "galbeiroc"
lessons = 5
print(f"Hi {name}, you have completed {lessons} lessons!")
```

#### Tuples -> Immutable ()

a Tuple is a collection of items that is ordered and unchangeable (immutable).

```python
vegetables = ("Tomates", "Onions", "Carrots")

vegetable1, vegetable2, vegetable3 = vegetables
print(f"Main vegetables: {vegetable1}, {vegetable2}, {vegetable3}")

garlic_ratio, potatoes_ratio = 2, 4
print(f"Garlic ratio: {garlic_ratio}, Patatoes ratio: {potatoes_ratio}")

# Swaping values
garlic_ratio, potatoes_ratio = potatoes_ratio, garlic_ratio
print(f"Garlic ratio: {garlic_ratio}, Patatoes ratio: {potatoes_ratio}")

# Membership testing
print(f"Is Garlic in vegetables? {'Garlic' in  vegetables}") # False
print(f"Is Carrots in vegetables? {'Carrots' in  vegetables}") # True
```

#### List -> Mutable []

a List is a collection of items that is ordered and changeable (mutable).

```python
ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are {ingredients}") # ['water', 'milk', 'black tea', 'sugar']

ingredients.remove("milk")
print(f"Ingredients are {ingredients}") # ['water', 'black tea', 'sugar']

spice_options = ["ginger", "cardamon"]
ingredients.extend(spice_options)
print(f"Chai Ingredients: {ingredients}") # ['water', 'black tea', 'sugar', 'ginger', 'cardamon']

print(f"The water is the position: {ingredients[0]}") # water

ingredients.insert(1, "milk")
print(f"Chai with milk ingredients: {ingredients}") # ['water', 'milk', 'black tea', 'sugar', 'ginger']

last_ingredient = ingredients.pop()
print(f"Last ingredient: {last_ingredient}") # cardamon
print(f"Chai Ingredients: {ingredients}") # ['water', 'milk', 'black tea', 'sugar', 'ginger']

ingredients.reverse()
print(f"Reversed ingredients {ingredients}") # ['ginger', 'sugar', 'black tea', 'milk', 'water']

ingredients.sort()
print(f"Sorted ingredients {ingredients}") # ['black tea', 'ginger', 'milk', 'sugar', 'water']

sugar_levels = [2, 5, 1, 4, 3]
print(f"Max sugar levels: {max(sugar_levels)}") # 5
print(f"Min sigar level: {min(sugar_levels)}") # 1
print(f"Total sugar levels: {sum(sugar_levels)}") # 15

print(f"Slicing sugar levels: {sugar_levels[0:3]}") # [2, 5, 1]
print(f"Slicing sugar levels: {sugar_levels[2:]}") # [1, 4, 3]
print(f"Slicing sugar levels: {sugar_levels[:2]}") # [2, 5]
print(f"Slicing sugar levels: {sugar_levels[1:4:2]}") # [5, 4]
```

##### Operator Overloading

Operator overloading allows you to define how standard operators (like `+`, `-`, `*`, or `==`).
this is done using "Dunder" (Double Underscore) methods. For example, when you use the + operator, Python actually calls a hidden method named `__add__`.

| Operator | Magic Method           | Purpose                        |
| :------- | :--------------------- | :----------------------------- |
| `+`      | `__add__(self, other)` | Addition                       |
| `-`      | `__sub__(self, other)` | Subtraction                    |
| `*`      | `__mul__(self, other)` | Multiplication                 |
| `==`     | `__eq__(self, other)`  | Equality check                 |
| `<`      | `__lt__(self, other)`  | Less than                      |
| `str()`  | `__str__(self)`        | Readable string representation |

```python
base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]
full_liquid_mix = base_liquid + extra_flavor
print(f"Full liquid mix: {full_liquid_mix}") # ['water', 'milk', 'ginger']

strong_brew = ["black tea", "water"] * 3
print(f"Strong brew: {strong_brew}") # ['black tea', 'water', 'black tea', 'water', 'black tea', 'water']
```

##### Bytearray

A bytearray is a mutable sequence of integers in the range **0 ≤ x < 256**. While a standard bytes object is immutable (like a string), a bytearray allows you to modify the data in place (like a list).

```python
raw_spice_data = bytearray(b"Cinnamon")
raw_spice_data = raw_spice_data.replace(b"Cinn", b"Card")
print(f"Raw spice data: {raw_spice_data}") # bytearray(b'Cardamon')

list_of_numbers = bytearray([65, 66, 67])
list_of_numbers[0] = 68
print(list_of_numbers) # bytearray(b'DEF')
```

#### Set

a Set is an unordered collection of unique items. To create an empty set, you must use `set()`.

```python
essential_spices = {"cardamon", "ginger", "cinnamon"}
optional_spices = {"cloves", "black pepper", "ginger"}

# Union |
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}") # All spices: {'ginger', 'cinnamon', 'cloves', 'black pepper', 'cardamon'}

# Intersection &
common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}") # Common spices: {'ginger'}

# Difference -
only_essential_spice = essential_spices - optional_spices
print(f"Only essential spices: {only_essential_spice}") # Only essential spices: {'cinnamon', 'cardamon'}

# Symmetric Difference ^
exclusive_spices = essential_spices ^ optional_spices
print(f"Exclusive spices: {exclusive_spices}") # Exclusive spices: {'cloves', 'black pepper', 'cinnamon', 'cardamon'}

# Membership testing
print(f"Is cloves in essentials spices {'cloves' in essential_spices}") # Is cloves in essentials spices False
print(f"Is cloves in optional spices {'cloves' in optional_spices}") # Is cloves in optional spices True
```

#### Dictionary -> Mutable {}

a Dictionary is an unordered collection of key-value pairs.

```python
computer_order = dict(type="laptop", size=14, vendor="hp")
print(f"Computer order: {computer_order}") # Computer order: {'type': 'laptop', 'size': 14, 'vendor': 'hp'}

user_profile = {}
user_profile['name'] = "galbeiroc"
user_profile['role'] = "admin"
user_profile["years_exp"] = 5
print(f"User profile: {user_profile}") # User profile: {'name': 'galbeiroc', 'role': 'admin', 'years_exp': 5}
print(f"User name {user_profile['name']}")

del user_profile['years_exp'] # User name galbeiroc
print(f"User profile: {user_profile}") # User profile: {'name': 'galbeiroc', 'role': 'admin'}

print(f"User profile (keys): {user_profile.keys()}") # User profile (keys): dict_keys(['name', 'role'])
print(f"User profile (values): {user_profile.values()}") # User profile (values): dict_values(['galbeiroc', 'admin'])
print(f"User profile (items): {user_profile.items()}") # User profile (items): dict_items([('name', 'galbeiroc'), ('role', 'admin')])

last_item = computer_order.popitem()
print(f"Last item: {last_item}") # Last item: ('vendor', 'hp')
print(f"Computer order: {computer_order}") # Computer order: {'type': 'laptop', 'size': 14}

new_user_properties = {"skills": ["JS", "Python"], "email": "test@email.com"}
user_profile.update(new_user_properties)
print(f"Update user profile: {user_profile}") # User profile: {'name': 'galbeiroc', 'role': 'admin', 'skills': ['JS', 'Python'], 'email': 'test@email.com'}

getting_user_password = user_profile.get("password", "default_password")
print(f"Getting user password: {getting_user_password}") # Getting user password: default_password

# Membership
print(f"Is name in user_profile? {'name' in user_profile}") # Is name in user_profile? True
```

### Conditional Statements

Python's Conditionals will feel very familiar, though the "punctuation" is a bit different.

In Python, we don't use curly braces `{}` or parentheses `()` for conditions. Instead, we use a colon `(:)` and indentation.

The Structure: `if`, `elif`, and `else`

```python
cpu_usage = 85

if cpu_usage > 90:
  print("Alert: Critical usage!")
else:
  print("OK: CPU usage is normal.")
```
