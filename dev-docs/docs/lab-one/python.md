---
sidebar_position: 1
id: Introduction To Python
description: 🚁 Helicopter view some python features.
slug: /lab-one/python
---

## Disclaimer
This is not an exotic list of important nor basic python features, it is your own responsibility and  you can always access internet during labs.

## Python Functions
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


## REFERENCES
- [5 Types of Arguments in Python Function Definitions](https://medium.com/gitconnected/5-types-of-arguments-in-python-function-definition-e0e2a2cafd29)