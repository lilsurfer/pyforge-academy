"""
curriculum.py — All 8 lessons for PyForge Academy (Cloudflare/Wasm version).
Theory is written as HTML strings for direct rendering.
"""

LESSONS = [
    {
        "id": "basics",
        "icon": "🐍",
        "title": "Python Basics",
        "objective": "Understand variables, data types, and print()",
        "theory": """
<h2>🐍 Python Basics</h2>
<p>Python is one of the most readable languages in the world. Let's start with <strong>variables</strong> — containers that store data.</p>
<pre><code>name = "Alice"
age  = 30
pi   = 3.14
ok   = True</code></pre>
<h3>Data Types</h3>
<table>
<tr><th>Type</th><th>Example</th><th>Meaning</th></tr>
<tr><td><code>str</code></td><td><code>"hello"</code></td><td>Text</td></tr>
<tr><td><code>int</code></td><td><code>42</code></td><td>Whole number</td></tr>
<tr><td><code>float</code></td><td><code>3.14</code></td><td>Decimal</td></tr>
<tr><td><code>bool</code></td><td><code>True</code></td><td>Yes / No</td></tr>
</table>
<h3>print() and f-strings</h3>
<pre><code>print("Hello, World!")
print(f"My name is {name} and I am {age}")</code></pre>
<p><strong>💡 Tip:</strong> Type <code>pri</code> then hit <kbd>Tab</kbd> to autocomplete <code>print</code>!</p>
""",
        "starter_code": """\
# 🐍 Python Basics — Explore variables and types!

name      = "Python Learner"
age       = 25
height    = 5.9
is_awesome = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} ft")
print(f"Awesome? {is_awesome}")

print("\\nTypes:")
print(f"  name   -> {type(name)}")
print(f"  age    -> {type(age)}")
print(f"  height -> {type(height)}")
""",
        "challenge": "Create a variable for your favourite language and print a sentence using an f-string.",
    },
    {
        "id": "strings",
        "icon": "📝",
        "title": "Strings",
        "objective": "Master slicing, formatting, and string methods",
        "theory": """
<h2>📝 Strings</h2>
<p>Strings are sequences of characters enclosed in quotes.</p>
<h3>Indexing &amp; Slicing</h3>
<pre><code>word = "Python"
print(word[0])    # 'P'  — first char
print(word[-1])   # 'n'  — last char
print(word[0:3])  # 'Pyt'
print(word[::-1]) # 'nohtyP' reversed!</code></pre>
<h3>Useful Methods</h3>
<table>
<tr><th>Method</th><th>Result</th></tr>
<tr><td><code>.upper()</code></td><td>ALL CAPS</td></tr>
<tr><td><code>.lower()</code></td><td>all lower</td></tr>
<tr><td><code>.strip()</code></td><td>remove whitespace</td></tr>
<tr><td><code>.replace(a,b)</code></td><td>swap text</td></tr>
<tr><td><code>.split()</code></td><td>list of words</td></tr>
</table>
<h3>f-Strings</h3>
<pre><code>lang = "Python"
print(f"I love {lang}!")</code></pre>
""",
        "starter_code": """\
# 📝 Strings — Slice, format, transform!

sentence = "The quick brown fox jumps over the lazy dog"

print("Original:", sentence)
print("Uppercase:", sentence.upper())
print("Word count:", len(sentence.split()))

print("\\nSlicing:")
print("  First 3:", sentence[:3])
print("  Last 3:", sentence[-3:])
print("  Reversed:", sentence[::-1])

print("\\nReplace:", sentence.replace("fox", "cat"))

animal = "fox"
print(f"\\nThe {animal} is quick!")
""",
        "challenge": "Take '  Hello Python World!  ', strip it, title-case it, split into words, and print the count.",
    },
    {
        "id": "numbers",
        "icon": "🔢",
        "title": "Numbers & Math",
        "objective": "Work with integers, floats, and the math module",
        "theory": """
<h2>🔢 Numbers &amp; Math</h2>
<h3>Arithmetic</h3>
<pre><code>a, b = 10, 3
print(a + b)   # 13  addition
print(a - b)   # 7   subtraction
print(a * b)   # 30  multiply
print(a / b)   # 3.33 true division
print(a // b)  # 3   floor division
print(a % b)   # 1   remainder
print(a ** b)  # 1000 power</code></pre>
<h3>math Module</h3>
<pre><code>import math
math.sqrt(16)      # 4.0
math.pi            # 3.14159...
math.ceil(4.2)     # 5
math.floor(4.8)    # 4
math.log10(1000)   # 3.0</code></pre>
""",
        "starter_code": """\
# 🔢 Numbers & Math!
import math

a, b = 17, 5
print(f"{a} + {b} = {a+b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b:.4f}")
print(f"{a} // {b} = {a//b}")
print(f"{a} % {b} = {a%b}")
print(f"{a} ** {b} = {a**b}")

print("\\nMath module:")
print(f"  sqrt(144) = {math.sqrt(144)}")
print(f"  pi = {math.pi:.6f}")
print(f"  ceil(4.2) = {math.ceil(4.2)}")

radius = 7
area = math.pi * radius ** 2
print(f"\\nCircle area (r={radius}): {area:.2f}")
""",
        "challenge": "Compute the hypotenuse of a right triangle with sides a=6, b=8 using math.sqrt().",
    },
    {
        "id": "loops",
        "icon": "🔁",
        "title": "Loops",
        "objective": "Iterate with for and while loops",
        "theory": """
<h2>🔁 Loops</h2>
<h3>for Loop</h3>
<pre><code>for i in range(5):
    print(i)   # 0,1,2,3,4

for char in "Python":
    print(char)</code></pre>
<h3>range(start, stop, step)</h3>
<pre><code>range(5)         # 0..4
range(1,6)       # 1..5
range(0,10,2)    # 0,2,4,6,8
range(5,0,-1)    # 5,4,3,2,1</code></pre>
<h3>while Loop</h3>
<pre><code>n = 0
while n &lt; 5:
    print(n)
    n += 1</code></pre>
<h3>break / continue / enumerate</h3>
<pre><code>for i, v in enumerate(["a","b","c"], start=1):
    print(i, v)</code></pre>
""",
        "starter_code": """\
# 🔁 Loops!

print("Countdown:")
for i in range(5, 0, -1):
    print(f"  {i}...")
print("  Liftoff!")

fruits = ["apple", "banana", "mango", "cherry"]
print("\\nFruits:")
for i, fruit in enumerate(fruits, 1):
    print(f"  {i}. {fruit}")

total = 0
n = 1
while n <= 100:
    total += n
    n += 1
print(f"\\nSum 1-100: {total}")

print("\\nTimes table (1-4):")
for i in range(1, 5):
    print("  " + "  ".join(f"{i*j:2}" for j in range(1, 5)))
""",
        "challenge": "Print every odd number from 1 to 50, then print their sum.",
    },
    {
        "id": "conditionals",
        "icon": "🌿",
        "title": "Conditionals",
        "objective": "Control program flow with if/elif/else",
        "theory": """
<h2>🌿 Conditionals</h2>
<pre><code>score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "F"</code></pre>
<h3>Operators</h3>
<table>
<tr><th>Op</th><th>Meaning</th></tr>
<tr><td><code>==</code></td><td>Equal</td></tr>
<tr><td><code>!=</code></td><td>Not equal</td></tr>
<tr><td><code>&gt;=</code></td><td>Greater or equal</td></tr>
<tr><td><code>and</code></td><td>Both true</td></tr>
<tr><td><code>or</code></td><td>Either true</td></tr>
<tr><td><code>not</code></td><td>Negate</td></tr>
</table>
<h3>Ternary</h3>
<pre><code>label = "even" if x % 2 == 0 else "odd"</code></pre>
""",
        "starter_code": """\
# 🌿 Conditionals!

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

print(f"Score: {score}  Grade: {grade} {emoji}")

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
        "challenge": "Classify a number as 'negative', 'zero', 'small' (1-100), or 'large' (>100).",
    },
    {
        "id": "lists_dicts",
        "icon": "📦",
        "title": "Lists & Dicts",
        "objective": "Store and access collections of data",
        "theory": """
<h2>📦 Lists &amp; Dictionaries</h2>
<h3>Lists</h3>
<pre><code>fruits = ["apple", "banana"]
fruits.append("cherry")
fruits.sort()
print(len(fruits))</code></pre>
<h3>List Comprehensions</h3>
<pre><code>squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x%2==0]</code></pre>
<h3>Dictionaries</h3>
<pre><code>person = {"name": "Alice", "age": 30}
print(person["name"])
person["city"] = "London"
person.get("phone", "N/A")
for k, v in person.items():
    print(k, v)</code></pre>
""",
        "starter_code": """\
# 📦 Lists & Dicts!

nums = [64, 34, 25, 12, 22, 11, 90]
print("Original:", nums)
nums.sort()
print("Sorted:", nums)
print(f"Min:{min(nums)} Max:{max(nums)} Sum:{sum(nums)}")

squares = [x**2 for x in range(1, 8)]
print("Squares:", squares)

student = {
    "name": "Alex",
    "grade": "B+",
    "subjects": ["Math", "Science", "English"],
}
print(f"\\nStudent: {student['name']}, {student['grade']}")
print("Subjects:", ", ".join(student["subjects"]))

text = "python is great python is fun"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print("\\nFrequency:", freq)
""",
        "challenge": "Given a list of numbers, use a comprehension to keep only those above the list's average.",
    },
    {
        "id": "functions",
        "icon": "🔧",
        "title": "Functions",
        "objective": "Write reusable functions with parameters and return values",
        "theory": """
<h2>🔧 Functions</h2>
<pre><code>def greet(name):
    return f"Hello, {name}!"

print(greet("World"))</code></pre>
<h3>Default Args &amp; *args</h3>
<pre><code>def power(base, exp=2):
    return base ** exp

def total(*nums):
    return sum(nums)

total(1, 2, 3, 4)  # 10</code></pre>
<h3>Lambda</h3>
<pre><code>square = lambda x: x ** 2
nums.sort(key=lambda x: -x)</code></pre>
<h3>Docstrings</h3>
<pre><code>def add(a, b):
    """Return sum of a and b."""
    return a + b</code></pre>
""",
        "starter_code": """\
# 🔧 Functions!

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}! 👋"

print(greet("Alice"))
print(greet("Bob", "Hi"))

def stats(*numbers):
    """Return stats dict for given numbers."""
    n = len(numbers)
    return {"count": n, "min": min(numbers),
            "max": max(numbers), "mean": sum(numbers)/n}

print("\\nStats:", stats(4, 8, 15, 16, 23, 42))

def factorial(n):
    """Compute n! recursively."""
    return 1 if n <= 1 else n * factorial(n-1)

print("\\nFactorials:")
for i in range(1, 8):
    print(f"  {i}! = {factorial(i)}")

words = ["banana", "apple", "fig", "cherry", "date"]
print("\\nBy length:", sorted(words, key=len))
""",
        "challenge": "Write is_palindrome(s) returning True if s reads the same forwards/backwards (ignore case).",
    },
    {
        "id": "classes",
        "icon": "🏛️",
        "title": "Classes & OOP",
        "objective": "Model real-world objects with classes",
        "theory": """
<h2>🏛️ Classes &amp; OOP</h2>
<pre><code>class Dog:
    species = "Canis lupus"

    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def bark(self):
        return f"{self.name}: Woof!"

dog = Dog("Rex", 3)
print(dog.bark())</code></pre>
<h3>Inheritance</h3>
<pre><code>class Animal:
    def speak(self): return "..."

class Cat(Animal):
    def speak(self): return "Meow!"</code></pre>
<h3>Properties</h3>
<pre><code>class Circle:
    def __init__(self, r): self.r = r

    @property
    def area(self):
        import math
        return math.pi * self.r ** 2</code></pre>
""",
        "starter_code": """\
# 🏛️ Classes & OOP!
import math

class Shape:
    def area(self):      return 0
    def perimeter(self): return 0
    def describe(self):
        n = type(self).__name__
        print(f"  {n}: area={self.area():.3f}  perim={self.perimeter():.3f}")

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self):        return math.pi * self.r**2
    def perimeter(self):   return 2 * math.pi * self.r

class Rectangle(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self):            return self.w * self.h
    def perimeter(self):       return 2*(self.w+self.h)

class Triangle(Shape):
    def __init__(self, a,b,c): self.a,self.b,self.c = a,b,c
    def perimeter(self):       return self.a+self.b+self.c
    def area(self):
        s = self.perimeter()/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

print("Geometry Report:")
for shape in [Circle(5), Rectangle(8,4), Triangle(3,4,5)]:
    shape.describe()
""",
        "challenge": "Add a Square class that inherits Rectangle. Add a class method from_diagonal(d) that builds a Square from its diagonal length.",
    },
]
