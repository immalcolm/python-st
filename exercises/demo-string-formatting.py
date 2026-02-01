# String formatting demo
name = "Alice"
age = 30
height = 1.75

# Using format() method
print("Name: {}, Age: {}, Height: {:.1f} m".format(name, age, height))

# Using f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}, Height: {height:.1f} m")

# using integer f-string
print(f"Name: {name}, Age: {age:d}, Height: {height:.1f} m")

# change precision of float
print(f"Name: {name}, Age: {age}, Height: {height:.3f} m")

# padding spaces
# right align and left align with specified width
print("Using padding and alignment:")
# Right align with format() method 
print("Name: {:>10}, Age: {:>5}, Height: {:>6.2f} m".format(name, age, height))

print(f"Name: {name:>10}, Age: {age:>5}, Height: {height:>6.2f} m")
print(f"Name: {name:<10}, Age: {age:<5}, Height: {height:<6.2f} m")

# character padding demos
# using different characters for padding
# ^ for center alignment 
# Explain * for padding character 
print("Using character padding:")
print("Name: {:*<10}, Age: {:*>5}, Height: {:*^10.4f} m".format(name, age, height))
print(f"Name: {name:*^10}, Age: {age:*^5}, Height: {height:*^6.2f} m")
print(f"Name: {name:-^10}, Age: {age:-^5}, Height: {height:-^6.2f} m")  

# how to include curly braces in formatted strings
# using double curly braces to escape
print("Including curly braces in formatted strings:")
print("Using format() method: {{ Name: {}, Age: {} }}".format(name, age))
print(f"Using f-strings: {{ Name: {name}, Age: {age} }}")

# format specificers inside curly braces
# demonstrate alignment within curly braces
print("Using format() method with specifiers: {{ Name: {:^10}, Age: {:^5} }}".format(name, age))
print(f"Using f-strings with specifiers: {{ Name: {name:^10}, Age: {age:^5} }}")