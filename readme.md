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

| Traditional Way     | Modern Way |
| ------------------- | ---------- |
|         venv        |      uv    |

### Data Types

#### Mutable and Immutable

Everything is object in Python.

Object -> identity -> value -> type
***Note:*** Never check with the value. Check with the identity.

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

The whole concept of mutable and immutable is what value can change and what cannot change in the *memory itself*.
