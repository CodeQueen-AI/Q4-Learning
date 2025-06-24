from generic_box import Box

int_box = Box 

str_box = Box[str]("Hello, Code Queen!")

# Print values
print(int_box.get_value())
print(str_box.get_value())  
