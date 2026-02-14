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
