---
sidebar_position: 1
id: Introduction To Python
description: 🚁 Helicopter view some python features.
slug: /lab-one/python
---

## Disclaimer
This is not an exotic list of important nor basic python features, it is your own responsibility and  you can always access internet during labs.

## Style Guide
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/).
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

## Types in Python
Python type system is unlike other languages you might have encountered, everything in python is an object. That object carries:
    - Type
    - Reference count
    - Value
Read more about garbage collection in python and basics of Memory Management in Python [here](https://youtu.be/URNdRl97q_0?si=u3aoWj2yePDiIXII).

### Type hinting
Python is a dynamically typed language, which means that you don't have to declare the type of the variable when you create one. The interpreter infers the type of the variable based on the value it is assigned. This is unlike statically typed languages like C, C++, Java, etc. where you have to declare the type of the variable when you create one.

Type hinting is a way for developers to add metadata to a codebase to make it easier to perform static analysis during development. Some have speculated that Python type hinting could in time give rise to a fork of the language that is statically typed, perhaps as a way to make Python faster. Plus, it hugely improves the readability of your code.

### Variables and Constants

```python
from typing import Final

COURSE_NAME: Final[str] = "CMPS446"
var_one: int = 3
var_two: bool = True
var_three: str = "Hello World"
print(var_one, var_two, var_three)
var_four: str = "your favv TA"
print(f"{COURSE_NAME}: {var_three}, by {var_four} :)")
```

```Console
3 True Hello World
CMPS446: Hello World, by your favv TA :)
```

<hr/>

```python
from typing import Optional
x: Optional[int] = None
print('x is None' if x is None else 'x is not None')
```

```console
x is None
```

## Printing in Python

### Printing to file
Consider running `Python Basic Syntax.ipynb` inside the following code structure:
```
(.venv) ziadh@Ziads-MacBook-Air lab-one-sol % tree  
.
├── Lab_one_std.ipynb
├── Lab_one_ta.ipynb
├── Python Basic Syntax.ipynb
├── README.md
├── data
│   ├── coffee.jpeg
│   ├── histogram
│   │   ├── ex1.jpg
│   │   ├── ex2.png
│   │   └── ex3.png
│   ├── hsv
│   │   ├── ex1.png
│   │   ├── ex2.jpg
│   │   └── ex3.jpg
│   └── pyramids.jpeg
├── lab-one-std.zip
├── materials
│   ├── Image Processing - Lab - Intro to Python and Jupyter.pdf
│   ├── Lab1-HSV-Noise-Histogram.pptx
│   ├── Lab1-Intro to Image Processing in Python.pptx
│   └── Lab1.pdf
├── output
│   └── output.log
└── requirements.txt

5 directories, 19 files
```

```python
"""Printing to file in Python
Example logging to a file
"""
import os
from pathlib import Path

BASE_PATH: Final[Path] = Path().resolve()
log_file_path: Final[Path] = os.path.join(BASE_PATH, "output", "output.log")

def log_to_file(file_path: Path, message: str) -> None:
    with open(file_path, "w") as f:
        import datetime
        timestamp: datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message: str = f"[{timestamp}] {message}"
        print(log_message, file=f)

log_to_file(log_file_path, "Hello World!")
```

```output.log
[2023-10-04 01:39:18] Hello World!
```

## Operators in Python

### Division
```python
# division in python
print(5/2)

# floor division or integer division
print(5 // 2)
```

```console
2.5
2
```

## Looping in Python
```python
array: list[int] = [1, 2, 3, 4, 5]
```

<hr/>

```python
for num in array:
    print(num)
```

```console
1
2
3
4
5
```

<hr/>

```python
for i in range(5):
    print(i)
```

```console
0
1
2
3
4
```

<hr/>

```python
# range(start, stop, step)
for i in range(0, 1_000_000, 10_000):
    print(f"{i:,}")
```

```console
0
10,000
20,000
30,000
...
970,000
980,000
990,000
```

<hr/>

```python
for num in array:
    if num%2 == 0:
        print(num)

# Usage of list comprehension
even_items: list[int] = [num for num in array if num%2 == 0]
print(even_items)
print(*even_items)
print(*even_items, sep=', ')
```

```console
2
4
[2, 4]
2 4
2, 4
```

## Functions in python

### Inline functions
```python
from typing import Callable

add: Callable[[int, int], int] = lambda x, y: x + y
result: int = add(3, 5)
print(result)
```

```console
8
```

## Decorators in Python
A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.

```python
import time
from typing import Callable
from pathlib import Path

BASE_PATH: Final[Path] = Path().resolve()
log_file_path: Final[str] = os.path.join(BASE_PATH, "output", "tune.log")

def log_to_file(file_path: str, message: str) -> None:
    with open(file_path, "w") as f:
        import datetime
        timestamp: datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message: str = f"[{timestamp}] {message}"
        print(log_message, file=f)

def timeit(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        log_to_file(log_file_path, f"Started {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        log_to_file(log_file_path, f"Done {func.__name__} took {end_time - start_time:,} seconds to execute.")
        return result
    return wrapper

@timeit
def add(a: int, b: int) -> int:
    time.sleep(10)
    return a + b

add(1, 2)
```

```console
[2023-10-04 03:12:59] Done add took 10.0048 seconds to execute.
```

## Passing arguments to Functions
Formal parameters are mentioned in the function definition. Actual parameters(arguments) are passed during a function call. We can define a function with a variable number of arguments.

### default arguments
Default arguments are values that are provided while defining functions. The assignment operator = is used to assign a default value to the argument. `Take care of mutable Data Structures`. Default arguments become optional during the function calls. If we provide a value to the default arguments during function calls, it overrides the default value. The function can have any number of default arguments. Default arguments should follow non-default arguments.

```python
def add(a: int, b: int = 5, c: int = 10) -> int:
    return a+b+c
print(add(3))
# Output:18
print(add(3, 4))
# Output:17
print(add(2, 3, 4))
# Output:9
```

**Note:** Default values are evaluated only once at the point of the function definition in the defining scope. So, it makes a difference when we pass mutable objects like a list or dictionary as default values.

### keyword arguments
Functions can also be called using keyword arguments of the form kwarg=value. During a function call, values passed through arguments need not be in the order of parameters in the function definition. This can be achieved by keyword arguments. But all the keyword arguments should match the parameters in the function definition.

```python
def add(a: int, b: int = 5, c: int = 10) -> int:
    return a+b+c
print(add(b=10, c=15, a=20))
# Output:45
print(add(a=10))
# Output:25
```

### positional arguments
During a function call, values passed through arguments should be in the order of parameters in the function definition. This is called positional arguments. Keyword arguments should follow positional arguments only.

```python
def add(a: int, b: int, c: int) -> int:
    return a+b+c
print(add(10, 20, 30))
# Output:60
print(add(10, c=30, b=20)) # Mix of positional and keyword arguments, keyword arguments should always follow positional arguments
# Output:60
```

### Variable-length arguments
Variable-length arguments are also known as arbitrary arguments. If we don’t know the number of arguments needed for the function in advance, we can use arbitrary arguments.

#### 🤓 arbitrary positional arguments
For arbitrary positional argument, an asterisk (*) is placed before a parameter in function definition which can hold non-keyword variable-length arguments. These arguments will be wrapped up in a tuple. Before the variable number of arguments, zero or more normal arguments may occur.
```python
def add(*args: list[int]) -> int:
    result: int = 0
    for i in args:
         result = result + i
    return result

print(add(1, 2, 3, 4, 5))
# Output:15
print(add(10, 20))
# Output:30
```

#### 🤓 arbitrary keyword arguments
For arbitrary positional argument, a double asterisk (**) is placed before a parameter in a function which can hold keyword variable-length arguments.

```python
from typing import Any

def fn(**kwargs: dict[str, Any]) -> None:
    for i in kwargs.items():
        print(i)
fn(numbers=5, colors="blue", fruits="apple")
'''
Output:
('numbers', 5)
('colors', 'blue')
('fruits', 'apple')
'''
```

### Special Parameters
By default, arguments may be passed to a Python function either by position or explicitly by keyword. For readability and performance, it makes sense to restrict the way arguments can be passed so that a developer need only look at the function definition to determine if items are passed by position, by position or keyword, or by keyword.

```python
def func(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    """pos1, pos2: Positional only parameters
    pos_or_kwd: Can be passed by position or keyword
    kwd1, kwd2: Keyword only parameters
    """
    pass
# Example
def add(a: int, b: int, /, c:int, d: int, *, e: int, f: int) -> int:
    return a + b + c + d + e + f
print(add(3, 4, 5, 6, e=7, f=8))
# Output:33
```

where `/` and `*` are optional. If used, these symbols indicate the kind of parameter by how the arguments may be passed to the function: positional-only, positional-or-keyword, and keyword-only.

#### 🤓 Positional or keyword arguments
If `/` and `*` are not present in the function definition, arguments may be passed to a function by position or by keyword.
```python
def func(a: int, b: int, c: int) -> int:
    return a + b + c
print(add(3, 4, 5))
# Output:12
print(add(3, c=1, b=2))
# Output:6
```

#### 🤓 Positional only arguments
Positional-only parameters are placed before a `/` (forward-slash) in the function definition. The `/` is used to logically separate the positional-only parameters from the rest of the parameters. Parameters following the `/` may be positional-or-keyword or keyword-only.

```python
def add(a: int, b: int, /, c:int, d: int) -> int:
    return a + b + c + d
print(add(3, 4, 5, 6))
# Output:12
print(add(3, 4, c=1, d=2))
# Output:6
print(add(3, b=4, c=1, d=2))
# Output:TypeError: add() got some positional-only arguments passed as keyword arguments: 'b'
```

#### 🤓 Keyword only arguments
To mark parameters as keyword-only, place an `*` in the arguments list just before the first keyword-only parameter.
```python
def add(a: int, b: int, *, c:int, d: int) -> int:
    return a + b + c + d
print(add(3, 4, c=1, d=2))
# Output:10
print(add(3, 4, 1, d=2))
# Output:TypeError: add() takes 2 positional arguments but 3 positional arguments (and 1 keyword-only argument) were given.
```

### Usage
- Use `positional-only` if you want the name of the parameters to not be available to the user. This is useful when parameter names have no real meaning.
- Use `positional-only` if you want to enforce the order of the arguments when the function is called.
- Use `keyword-only` when names have meaning and the function definition is more understandable by being explicit with names.
- Use `keyword-only` when you want to prevent users from relying on the position of the argument being passed.

## Numpy

### Generating NumPy arrays
```python
import numpy as np
```

```python
zeros_array: np.ndarray[int] = np.zeros(shape=(6, 5), dtype=int)
ones_array: np.ndarray[int] = np.ones(shape=(6, 5), dtype=int)

print(zeros_array)
print(ones_array)
print(ones_array.shape)
print(ones_array.shape[0])
```

```console
[[0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]]
[[1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]]
(6, 5)
6
```

### Array Indexing
```python
array: list[int] = [0, 1, 2, 3, 4, 5]
print(array[:3])

second_array: np.ndarray[int] = np.array(array)
third_array: np.ndarray[int] = np.copy(second_array)

print(third_array)
third_array[:3] = 0
print(third_array)

third_array: np.ndarray[int] = np.copy(second_array)
third_array[third_array%2==0] = -1
print(third_array)

third_array: np.ndarray[int] = np.copy(second_array)
third_array[(third_array%2==0) & (third_array==2)] = -1
print(third_array)
```

```console
[0, 1, 2]
[0 1 2 3 4 5]
[0 0 0 3 4 5]
[-1  1 -1  3 -1  5]
[ 0  1 -1  3  4  5]
```

<hr/>

```python
original_matrix: np.ndarray[list[int]] = np.array([
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
])

copied_matrix: np.ndarray[list[int]] = np.copy(original_matrix)
print(copied_matrix)

copied_matrix[1:3, 1:3] = 0
print(copied_matrix)
```

```console
[[1 2 3 4 5]
 [1 2 3 4 5]
 [1 2 3 4 5]]
[[1 2 3 4 5]
 [1 0 0 4 5]
 [1 0 0 4 5]]
```

## Extra Useful Talks
Always keep yourself updated with each new python release changes.
- [Sebastian Witowski - Writing faster Python](https://youtu.be/YjHsOrOOSuI?si=mEhQO4nUWcYty4yi)
- [Memory Management in Python - The Basics](https://youtu.be/URNdRl97q_0?si=y509rZJ3myM65dMB)
- [PyCon 2015 - Python's Infamous GIL by Larry Hastings](https://youtu.be/KVKufdTphKs?si=26ylGTmYtPIlXBFN)
- [What are metaclasses in Python?](https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python)
- [Scaling Instagram Infrastructure](https://www.youtube.com/watch?v=hnpzNAPiC0E)
- [Software Design in Python](https://youtube.com/playlist?list=PLC0nd42SBTaNuP4iB4L6SJlMaHE71FG6N&si=w1dURsMpT8tWhX0N)
- [State of the Art Python Features](https://youtube.com/playlist?list=PLC0nd42SBTaMpVAAHCAifm5gN2zLk2MBo&si=RWDSKyzrabProhud)

## REFERENCES
- [5 Types of Arguments in Python Function Definitions](https://medium.com/gitconnected/5-types-of-arguments-in-python-function-definition-e0e2a2cafd29)