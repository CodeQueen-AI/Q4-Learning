

# 🧠 What Are Generics?

**Generics** allow you to write **flexible, reusable, and type-safe** code in Python.

Instead of writing different versions of a class or function for different data types (like `int`, `str`, or `float`), you can write **one generic version** that works with **all** of them


## 🔧 Where Are Generics Used?

- ✅ Classes
- ✅ Functions
- ✅ Data structures (like lists, stacks, queues)
- ✅ APIs and libraries for flexibility


## 🧩 Core Concepts

| Concept   | Description                                      |
|-----------|--------------------------------------------------|
| `TypeVar` | Represents a placeholder for any type (like `T`) |
| `Generic` | A base class to create generic classes           |

## 🧪 Example: Generic `Box` Class

We’ll create a `Box` class that can hold any type of value (like int, str, float, etc.)

### 📁 `generic_box.py`

```python
from typing import TypeVar, Generic

T = TypeVar('T')  # T can be any type

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        return self.value

    def __repr__(self):
        return f"Box({self.value})"
````

### 📁 `main.py`

```python
from generic_box import Box

# Integer box
int_box = Box 

# String box
str_box = Box[str]("Hello, Code Queen!")

# Print values
print(int_box.get_value())  # Output: 123
print(str_box.get_value())  # Output: Hello, Code Queen!
```


## ✅ Output

```
123
Hello, Code Queen!
```

## 🎯 Why Use Generics?

| Benefit         | Why It Matters                              |
| --------------- | ------------------------------------------- |
| 💡 Reusability  | Write once, use with any type               |
| 🔐 Type safety  | Catch bugs at compile-time using type hints |
| 🧼 Cleaner code | Avoid repeating logic for each data type    |
| 📦 Flexibility  | Supports many different input types easily  |



## 🧠 Real-World Use

Generics are used in libraries like:

* FastAPI (`Response[T]`)
* SQLModel / Pydantic
* Type-safe APIs and services


## 🏁 Conclusion

Generics help you build **smart, clean, and powerful** code that grows with your project — whether you're writing APIs, utilities, or data models


### *Mastered by Code Queen with clarity and confidence!*


