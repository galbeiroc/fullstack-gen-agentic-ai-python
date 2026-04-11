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

#### Ternary Operator

**Syntax**: value_if_true `if` _condition_ `else` value_if_false

```python
order_amount = int(input("Enter the order amout: "))

delivery_fees = 0 if order_amount > 300 else 30

print(f"Delivery fees is: {delivery_fees}")
# 301 -> Delivery fees is: 0
# 299 -> Delivery fees is: 30
```

#### Match Case

Since Python 3.10, there is a `match` statement which is similar to `switch` in other languages.

```python
seat_type = input("Enter seat type: (sleeper/AC/general/luxury): ").lower()

match seat_type:
  case "sleeper":
    print("Sleeper - No AC, beds available")
  case "ac":
    print("AC - Air conditioned, comfy ride")
  case "genreral":
    print("General - Cheapest option, no reservation")
  case "luxury":
    print("Luxury - Premium seats with meals")
  case _:
    print("Invalid seat type")
```

### Loops

- Use `for` and `while` loops
- Loops through sequences using `range()`, `enumerate()` and `zip()`
- Control loop behavior using `break`, `continue` and `else` clauses

#### For Loops

A `for` loop is used for iterating over a sequence (that is either a _list_, a _tuple_, a _dictionary_, a _set_, or a _string_).

```python
orders = ["Rodri", "Samuel", "Rose", "Salome"]

for order in orders:
  print(f"Order ready for: {order}") # Order ready for: Rodri, Order ready for: Samuel, Order ready for: Rose, Order ready for: Salome
```

##### Else in For Loop

The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

```python
for x in range(6):
  print(x) # 0, 1, 2, 3, 4, 5
else:
  print("Finally finished!") # Finally finished!


staff = [("Amit", 16), ("Zara", 17), ("Rafa", 15)]

for name, age in staff:
  if age >= 18:
    print(f"{name} is eligible to manage staff")
    break
else:
  print(f"No one  is eligible to manage staff") # No one  is eligible to manage staff
```

##### The range()

The `range()` function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
`range(start, stop, step)`

- `start`: Optional. An integer number specifying at which position to start. Default is 0
- `stop`: Required. An integer number specifying at which position to stop (not included).
- `step`: Optional. An integer number specifying the incrementation. Default is 1

```python
y = range(3, 6)
for n in y:
  print(n) # 3, 4, 5

x = range(3, 20, 2)
for n in x:
  print(n) # 3, 5, 7, 9, 11, 13, 15, 17, 19
```

##### The enumerate()

The `enumerate()` function takes a collection (e.g. a tuple) and returns it as an enumerate object.
The `enumerate()` function adds a counter as the key of the enumerate object.
`enumerate(iterable, start)`

- `iterable` - An iterable object
- `start` - A Number. Defining the start number of the enumerate object. Default 0

```python
x = ('apple', 'banana', 'cherry')
y = enumerate(x)

print(list(y)) # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]


menu = ["Green", "Spiced", "Lemon", "Mint"]

for idx, item in enumerate(menu, start=1):
  print(f"Menu item #{idx}: {item} tea") # Menu item #1: Green tea, Menu item #2: Spiced tea, Menu item #3: Lemon tea, Menu item #4: Mint tea
```

##### zip()

The `zip()` function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
`zip(iterator1, iterator2, iterator3 ...)`

```python
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)

print(tuple(x)) # (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
print(list(x)) # [('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica')]

names = ["Albeiro", "Liam", "Alice", "Veroco"]
bills = [50, 75, 100, 60]

for name, amount in zip(names, bills):
  print(f"{name} paid ${amount} dollars") # Albeiro paid $50 dollars, Liam paid $75 dollars, Alice paid $100 dollars, Veroco paid $60 dollars
```

#### While Loops

With the `while` loop we can execute a set of statements as long as a condition is true.

```python
temperature=40

while temperature < 100:
  print(f"Current temperature: {temperature}")
  temperature += 15

print("Tea is ready to boil")
```

#### The break Statement

With the break statement we can stop the loop before it has looped through all the items:

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) # "apple", "banana"
  if x == "banana":
    break
```

#### The continue Statement

With the continue statement we can stop the current iteration of the loop, and continue with the next:

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) # "apple", "cherry"
```

#### The pass Statement

`for` loops cannot be empty, but if you for some reason have a `for` loop with no content, put in the `pass` statement to avoid getting an error.

```python
for x in [0, 1, 2]:
  pass
```

#### Walrus Operator :=

Python 3.8 introduced the `:=` operator, known as the "walrus operator". It assigns values to variables as part of a larger expression:

```python
value = 14
""" remainder = value % 5

if remainder:
  print(f"Not divisible by 5, remainder is {remainder}") """

if (remainder := value % 5):
  print(f"Not divisible by 5, remainder is {remainder}")

if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")

available_sizes = ["small", "medium", "large"]

if (size := input("What size do you want? ")) in available_sizes:
  print(f"Great, we have {size} size available")
else:
  print(f"Sorry, we don't have {size} size available")
```

### Functions

A function is a block of code which only runs when it is called.
A function can return data as a result.
A function helps avoiding code repetition.

In Python, a function is defined using the `def` keyword, followed by a function name and parentheses:

```python
def my_function():
  print("Hello from a function")
```

To call a function, write its name followed by parentheses: `my_function()`

#### Scopes

A variable is only available from inside the region it is created. This is called scope.

##### Local Scope

A variable created inside a function belongs to the _local scope_ of that function, and can only be used inside that function.

##### Enclosing Scope or Function Inside Function

As explained in the example above, the variable `x` is not available outside the function, but it is available for any function inside the function.

##### Global Scope

A variable created in the main body of the Python code is a global variable and belongs to the global scope.
Global variables are available from within any scope, global and local.

```python
def serve_drink():
  drink_type = "Soda" # -> Local scope
  print(f"Inside Serving {drink_type}...") # Inside Serving Soda...

drink_type = "Water"
serve_drink()
print(f"Outside Serving {drink_type}...") # Outside Serving Water...


def drink_counter():
  drink_ordered = "Lemonade" # -> Enclosing scope
  def print_order():
    drink_ordered = "Juice"
    print(f"Inner function: {drink_ordered}") # Outer function: Juice
  print_order()
  print(f"Outer function: {drink_ordered}") # Outer function: Lemonade

drink_ordered = "Beer" # -> Global scope
drink_counter()
print(f"Global variable: {drink_ordered}") # Global variable: Beer
```

##### Nonlocal Keyword

The `nonlocal` keyword is used to work with variables inside nested functions.
The `nonlocal` keyword makes the variable belong to the outer function.

```python
def update_order():
  order_type = "Pizza"

  def kitchen():
    nonlocal order_type ##
    order_type = "Pasta"
    print(f"Inside Kitchen: {order_type}") # Inside Kitchen: Pasta

  kitchen()
  print(f"Outside Kitchen: {order_type}") # Outside Kitchen: Pasta

update_order()
```

##### Global Keyword

If you need to create a global variable, but are stuck in the local scope, you can use the `global` keyword.

```python
order_type = "Burger" # Global scope

def front_desk():
  def kitchen():
    global order_type
    order_type = "Pasta"
  kitchen()

front_desk()
print(f"Global variable: {order_type}") # Global variable: Pasta
```

#### Arguments

Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

```python
burger = "burger"

def prepare_meal(order):
  print(f"Preparing {order}...")

prepare_meal(burger)
print(f"{burger} is ready!")

num_orders = [1, 2, 3]

def update_orders(orders):
  orders[1] = 42 # This will modify the original list passed as an argument

update_orders(num_orders)
print(num_orders)
```

#### Parameters vs Arguments

A `parameter` is the variable listed inside the parentheses in the function definition.
An `argument` is the actual value that is sent to the function when it is called.

```python
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("galbeiroc") # "galbeiroc" is an argument
```

#### Default Parameter Values

You can assign default values to parameters. If the function is called without an argument, it uses the default value:

```python
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden") # I am from Sweden
my_function() # I am from Norway
```

#### Keyword Arguments

You can also send arguments with the `key = value` syntax.
This way the order of the arguments does not matter.

The phrase _Keyword Arguments_ is often shortened to **kwargs** in Python documentation.

##### Keyword-Only Arguments

To specify that a function can have only keyword arguments, add `*,` before the arguments:

```python
def my_function(*, name):
  print("Hello", name)

my_function(name="galbeiroc") # "galbeiroc" is a keyword argument
```

#### Positional Arguments

When you call a function with arguments without using keywords, they are called positional arguments.
Positional arguments must be in the correct order:

```python
def make_pizza(size, cheese, toppings):
  print(f"Making a {size} pizza with {cheese} cheese and {toppings} toppings.")

make_pizza("large", "mozzarella", ["pepperoni", "mushrooms"]) # Positional arguments
make_pizza(size="medium", toppings=["olives", "onions"], cheese="cheddar") # Keyword arguments (order doesn't matter)
```

##### Positional-Only Arguments

You can specify that a function can have ONLY positional arguments.
To specify positional-only arguments, add `, /` after the arguments:

```python
def my_function(name, /):
  print("Hello", name)

my_function("galbeiroc") # "galbeiroc" is a positional argument
```

#### Combining Positional-Only and Keyword-Only

You can combine both argument types in the same function.
Arguments before `/` are positional-only, and arguments after `*` are keyword-only:

```python
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result) # 50
```
