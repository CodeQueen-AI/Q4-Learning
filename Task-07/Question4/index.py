from generic_box import Box

# Create a Box that holds an integer
int_box = Box 

# Create a Box that holds a string
str_box = Box[str]("Hello, Code Queen!")

# Print values
print(int_box.get_value())   # Output: 123
print(str_box.get_value())   # Output: Hello, Code Queen!
