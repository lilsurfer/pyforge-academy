"""
curriculum.py — Lesson definitions for the Python Learning Academy.

Each lesson is a dict with:
  - id:           unique slug
  - icon:         emoji for sidebar
  - title:        display name
  - objective:    one-liner learning goal
  - theory:       markdown content explaining the concept
  - starter_code: pre-filled editor code for the student
  - challenge:    optional challenge prompt
"""

LESSONS = [
    {
        "id": "basics",
        "icon": "🐍",
        "title": "Python Basics",
        "objective": "Understand variables, data types, and print()",
        "theory": """
## 🐍 Python Basics

Welcome to the Python Learning Academy! Python is one of the most readable and beginner-friendly programming languages in the world.

### Variables
A **variable** is a named container that stores a value:
```python
name = "Alice"
age = 30
height = 5.7
is_student = True
```

### Data Types
| Type | Example | Description |
|------|---------|-------------|
| `str` | `"hello"` | Text |
| `int` | `42` | Whole number |
| `float` | `3.14` | Decimal number |
| `bool` | `True` | True or False |

### The `print()` Function
Use `print()` to display output:
```python
print("Hello, World!")
print(f"My name is {name} and I am {age} years old.")
```

### `type()` — Inspect a variable's type
```python
print(type(42))      # <class 'int'>
print(type("hi"))    # <class 'str'>
```
""",
        "starter_code": """# 🐍 Python Basics — Explore variables and types!

# Create some variables
name = "Python Learner"
age = 25
height = 5.9
is_awesome = True

# Print them out
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} ft")
print(f"Is awesome? {is_awesome}")

# Check their types
print("\\nData Types:")
print(f"  name  → {type(name)}")
print(f"  age   → {type(age)}")
print(f"  height → {type(height)}")
""",
        "challenge": "Create a variable for your favorite programming language and print a sentence using it with an f-string.",
    },
    {
        "id": "strings",
        "icon": "📝",
        "title": "Strings",
        "objective": "Master string creation, slicing, and methods",
        "theory": """
## 📝 Strings

Strings are sequences of characters. In Python, they're extremely versatile.

### Creating Strings
```python
s1 = "double quotes"
s2 = 'single quotes'
s3 = \"\"\"triple quotes
span multiple lines\"\"\"
```

### String Indexing & Slicing
```python
word = "Python"
print(word[0])     # 'P'  — first character
print(word[-1])    # 'n'  — last character
print(word[0:3])   # 'Pyt' — slice [start:stop]
print(word[::-1])  # 'nohtyP' — reversed!
```

### Useful String Methods
| Method | Result |
|--------|--------|
| `.upper()` | `"hello"` → `"HELLO"` |
| `.lower()` | `"HELLO"` → `"hello"` |
| `.strip()` | `"  hi  "` → `"hi"` |
| `.replace(a, b)` | Replace `a` with `b` |
| `.split(sep)` | Split into a list |
| `.join(list)` | Join a list into a string |
| `.count(sub)` | Count occurrences |
| `.startswith(s)` | Boolean check |

### f-Strings (Python 3.6+)
```python
name = "World"
print(f"Hello, {name}!")
print(f"2 + 2 = {2 + 2}")
```
""",
        "starter_code": """# 📝 Strings — Slice, format, and transform!

sentence = "The quick brown fox jumps over the lazy dog"

# Basics
print("Original:", sentence)
print("Uppercase:", sentence.upper())
print("Word count:", len(sentence.split()))

# Slicing
print("\\nFirst 3 chars:", sentence[:3])
print("Last 3 chars:", sentence[-3:])
print("Reversed:", sentence[::-1])

# Find & Replace
print("\\nReplace 'fox' with 'cat':", sentence.replace("fox", "cat"))

# f-string formatting
animal = "fox"
jumps = 3
print(f"\\nThe {animal} jumped {jumps} time(s)!")
print(f"  → Length of sentence: {len(sentence)} characters")
""",
        "challenge": "Take the string `'  Hello, Python World!  '` and: strip whitespace, convert to title case, split into a list of words, then print the number of words.",
    },
    {
        "id": "numbers",
        "icon": "🔢",
        "title": "Numbers & Math",
        "objective": "Work with integers, floats, and the math module",
        "theory": """
## 🔢 Numbers & Math

Python handles numeric operations with clean, readable syntax.

### Integer & Float Arithmetic
```python
a, b = 10, 3

print(a + b)   # 13  — addition
print(a - b)   # 7   — subtraction
print(a * b)   # 30  — multiplication
print(a / b)   # 3.333... — true division (always float)
print(a // b)  # 3   — floor division
print(a % b)   # 1   — modulo (remainder)
print(a ** b)  # 1000 — exponentiation
```

### Type Conversion
```python
int("42")      # → 42
float("3.14")  # → 3.14
str(100)       # → "100"
round(3.7)     # → 4
```

### The `math` Module
```python
import math

math.sqrt(16)   # 4.0
math.pi         # 3.14159...
math.ceil(4.2)  # 5
math.floor(4.8) # 4
math.log(100, 10)  # 2.0
```
""",
        "starter_code": """# 🔢 Numbers & Math — Crunch some numbers!
import math

# Basic arithmetic
a, b = 17, 5
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.4f}")   # 4 decimal places
print(f"{a} // {b} = {a // b}")     # floor division
print(f"{a} % {b} = {a % b}")       # remainder
print(f"{a} ** {b} = {a ** b}")     # power

# Math module
print("\\nMath module:")
print(f"  √144 = {math.sqrt(144)}")
print(f"  π ≈ {math.pi:.6f}")
print(f"  ceil(4.2) = {math.ceil(4.2)}")
print(f"  log₁₀(1000) = {math.log10(1000)}")

# Circle area calculator
radius = 7
area = math.pi * radius ** 2
print(f"\\nCircle (r={radius}): area = {area:.2f}")
""",
        "challenge": "Write a program that computes the hypotenuse of a right triangle given sides `a=6` and `b=8` using the Pythagorean theorem and `math.sqrt()`.",
    },
    {
        "id": "loops",
        "icon": "🔁",
        "title": "Loops",
        "objective": "Iterate with for and while loops",
        "theory": """
## 🔁 Loops

Loops let you repeat actions. Python has two types: `for` and `while`.

### `for` Loop
Iterates over any sequence (list, string, range):
```python
for i in range(5):
    print(i)          # 0, 1, 2, 3, 4

for char in "Python":
    print(char)       # P, y, t, h, o, n

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### `range(start, stop, step)`
```python
range(5)        # 0..4
range(1, 6)     # 1..5
range(0, 10, 2) # 0, 2, 4, 6, 8
range(5, 0, -1) # 5, 4, 3, 2, 1 (countdown)
```

### `while` Loop
Repeats while a condition is True:
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### `break` and `continue`
```python
for i in range(10):
    if i == 5:
        break       # Stop the loop entirely
    if i % 2 == 0:
        continue    # Skip even numbers
    print(i)        # prints 1, 3
```

### `enumerate()` — Loop with index
```python
for i, fruit in enumerate(["apple", "banana"], start=1):
    print(f"{i}. {fruit}")
```
""",
        "starter_code": """# 🔁 Loops — Repeat and iterate!

# Countdown with range
print("Countdown:")
for i in range(5, 0, -1):
    print(f"  {i}...")
print("  🚀 Liftoff!")

# Loop over a list with enumerate
print("\\nFruit list:")
fruits = ["apple", "banana", "mango", "cherry"]
for i, fruit in enumerate(fruits, start=1):
    print(f"  {i}. {fruit.capitalize()}")

# Sum with a while loop
print("\\nSum 1 to 100:")
total = 0
n = 1
while n <= 100:
    total += n
    n += 1
print(f"  Result: {total}")

# Nested loops — multiplication table
print("\\nMini multiplication table (1-4):")
for i in range(1, 5):
    row = "  "
    for j in range(1, 5):
        row += f"{i*j:4}"
    print(row)
""",
        "challenge": "Use a loop to print every odd number from 1 to 50, then print their sum.",
    },
    {
        "id": "conditionals",
        "icon": "🌿",
        "title": "Conditionals",
        "objective": "Control program flow with if/elif/else",
        "theory": """
## 🌿 Conditionals

Conditionals let your program make decisions.

### `if / elif / else`
```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")
```

### Comparison Operators
| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal |
| `>=` | Greater than or equal |

### Boolean Operators
```python
x = 15
print(x > 10 and x < 20)   # True — both must be True
print(x < 5 or x > 10)     # True — at least one True
print(not x == 15)          # False — negation
```

### Ternary (one-liner if)
```python
label = "even" if x % 2 == 0 else "odd"
```

### `in` Operator
```python
"py" in "Python"     # True
5 in [1, 2, 3, 5]   # True
```
""",
        "starter_code": """# 🌿 Conditionals — Make decisions!

# Grade calculator
score = 78

if score >= 90:
    grade, emoji = "A", "🌟"
elif score >= 80:
    grade, emoji = "B", "😊"
elif score >= 70:
    grade, emoji = "C", "😐"
elif score >= 60:
    grade, emoji = "D", "😟"
else:
    grade, emoji = "F", "❌"

print(f"Score: {score}")
print(f"Grade: {grade} {emoji}")

# FizzBuzz classic
print("\\nFizzBuzz (1-20):")
for n in range(1, 21):
    if n % 15 == 0:
        print("  FizzBuzz")
    elif n % 3 == 0:
        print("  Fizz")
    elif n % 5 == 0:
        print("  Buzz")
    else:
        print(f"  {n}")
""",
        "challenge": "Write a program that classifies a number as: 'negative', 'zero', 'small positive' (1-100), or 'large positive' (>100).",
    },
    {
        "id": "lists_dicts",
        "icon": "📦",
        "title": "Lists & Dicts",
        "objective": "Store and access collections of data",
        "theory": """
## 📦 Lists & Dictionaries

### Lists
Ordered, mutable sequences:
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")        # Add to end
fruits.insert(1, "avocado")  # Insert at index
fruits.remove("banana")      # Remove by value
fruits.pop()                 # Remove last item
fruits.sort()                # Sort in place
print(len(fruits))           # Length
```

### List Comprehensions
```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
upper   = [s.upper() for s in ["a", "b", "c"]]
```

### Dictionaries
Key-value pairs (like a lookup table):
```python
person = {
    "name": "Alice",
    "age": 30,
    "city": "London"
}

print(person["name"])         # Access
person["email"] = "a@b.com"  # Add key
person.get("phone", "N/A")   # Safe get with default
del person["city"]            # Delete key

for key, value in person.items():
    print(f"{key}: {value}")
```

### Common Patterns
```python
# Word frequency counter
words = "to be or not to be".split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
```
""",
        "starter_code": """# 📦 Lists & Dicts — Organize your data!

# List operations
print("=== Lists ===")
numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {numbers}")
numbers.sort()
print(f"Sorted:   {numbers}")
print(f"Min: {min(numbers)}, Max: {max(numbers)}, Sum: {sum(numbers)}")

# List comprehension
squares = [x**2 for x in range(1, 8)]
print(f"Squares:  {squares}")

# Dictionary
print("\\n=== Dictionaries ===")
student = {
    "name": "Alex",
    "grade": "B+",
    "subjects": ["Math", "Science", "English"],
    "score": 87,
}

print(f"Student: {student['name']}")
print(f"Grade: {student['grade']}")
print(f"Subjects: {', '.join(student['subjects'])}")

# Word frequency
print("\\n=== Word Frequency ===")
text = "python is great python is fun python"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1

for word, count in sorted(freq.items(), key=lambda x: -x[1]):
    print(f"  '{word}': {count} time(s)")
""",
        "challenge": "Given a list of numbers, use a list comprehension to create a new list containing only the numbers greater than the list's average.",
    },
    {
        "id": "functions",
        "icon": "🔧",
        "title": "Functions",
        "objective": "Write reusable functions with parameters and return values",
        "theory": """
## 🔧 Functions

Functions let you package reusable logic into named blocks.

### Defining a Function
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))  # Hello, World!
```

### Parameters
```python
# Default parameter values
def power(base, exponent=2):
    return base ** exponent

power(3)     # 9  (exponent defaults to 2)
power(3, 3)  # 27

# Keyword arguments
power(exponent=3, base=2)  # 8

# Variable positional args (*args)
def total(*numbers):
    return sum(numbers)

total(1, 2, 3, 4)  # 10

# Variable keyword args (**kwargs)
def profile(**info):
    for k, v in info.items():
        print(f"  {k}: {v}")

profile(name="Alice", age=30)
```

### Docstrings
```python
def add(a, b):
    \"\"\"Return the sum of a and b.\"\"\"
    return a + b
```

### Lambda Functions
```python
square = lambda x: x ** 2
double = lambda x: x * 2

nums = [3, 1, 4, 1, 5, 9]
nums.sort(key=lambda x: -x)  # sort descending
```
""",
        "starter_code": """# 🔧 Functions — Write reusable code!

# Basic function
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}! 👋"

print(greet("Alice"))
print(greet("Bob", "Hi"))
print(greet("World", greeting="Hey"))

# Function with *args
def stats(*numbers):
    \"\"\"Return min, max, mean of given numbers.\"\"\"
    n = len(numbers)
    return {
        "count": n,
        "min":   min(numbers),
        "max":   max(numbers),
        "mean":  sum(numbers) / n,
    }

result = stats(4, 8, 15, 16, 23, 42)
print(f"\\nStats: {result}")

# Recursive function
def factorial(n):
    \"\"\"Compute n! recursively.\"\"\"
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("\\nFactorials:")
for i in range(1, 8):
    print(f"  {i}! = {factorial(i)}")

# Lambda + sorted
words = ["banana", "apple", "fig", "cherry", "date"]
sorted_words = sorted(words, key=lambda w: len(w))
print(f"\\nSorted by length: {sorted_words}")
""",
        "challenge": "Write a function `is_palindrome(s)` that returns `True` if the string `s` reads the same forwards and backwards (ignore case). Test it with 'racecar', 'Python', and 'Level'.",
    },
    {
        "id": "classes",
        "icon": "🏛️",
        "title": "Classes & OOP",
        "objective": "Model real-world objects with classes",
        "theory": """
## 🏛️ Classes & Object-Oriented Programming

Classes are blueprints for creating objects with attributes and methods.

### Defining a Class
```python
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis lupus familiaris"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says: Woof! 🐕"

    def __repr__(self):
        return f"Dog(name={self.name!r}, age={self.age})"
```

### Using a Class
```python
dog1 = Dog("Rex", 3)
dog2 = Dog("Bella", 5)

print(dog1.bark())      # Rex says: Woof!
print(dog2.name)        # Bella
print(Dog.species)      # Canis lupus familiaris
```

### Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Cat(Animal):     # Cat inherits from Animal
    def speak(self):   # Override the method
        return f"{self.name} says: Meow! 🐱"

cat = Cat("Whiskers")
print(cat.speak())
```

### Properties
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        import math
        return math.pi * self.radius ** 2
```
""",
        "starter_code": """# 🏛️ Classes & OOP — Model the world!
import math

class Shape:
    \"\"\"Base class for geometric shapes.\"\"\"
    def area(self):
        return 0

    def perimeter(self):
        return 0

    def describe(self):
        print(f"  {type(self).__name__}:")
        print(f"    Area:      {self.area():.4f}")
        print(f"    Perimeter: {self.perimeter():.4f}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))


# Create and describe shapes
shapes = [Circle(5), Rectangle(8, 4), Triangle(3, 4, 5)]
print("Geometry Report:")
for shape in shapes:
    shape.describe()
""",
        "challenge": "Extend the `Shape` class system by adding a `Square` class (a special rectangle where width == height). Add a class method `from_diagonal(d)` that creates a Square given its diagonal length.",
    },
]
