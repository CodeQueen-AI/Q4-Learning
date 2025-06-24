from typing import TypeVar, Generic

# Create a type variable (can be any type: int, str, etc.)
T = TypeVar('T')

# Define a generic Box class
class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        return self.value

    def __repr__(self):
        return f"Box({self.value})"
