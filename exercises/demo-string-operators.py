# Demo of string operators
str1 = "Hello"
str2 = "World"
# Concatenation
result_concat = str1 + " " + str2
print("Concatenation:", result_concat)
# Repetition
result_repeat = str1 * 3
print("Repetition:", result_repeat)
# Membership
is_member = "lo" in str1
print("'lo' in str1:", is_member)
is_not_member = "z" not in str2
print("'z' not in str2:", is_not_member)
# Slicing
sliced_str = str1[1:4]
print("Sliced str1 (1:4):", sliced_str)
# Length
length_str1 = len(str1)
print("Length of str1:", length_str1)
# String Methods
upper_str = str1.upper()
print("Uppercase str1:", upper_str)
lower_str = str2.lower()

# Demo of string methods
print("Lowercase str2:", lower_str)
find_substr = str1.find("l")
print("Find 'l' in str1:", find_substr)
replace_substr = str2.replace("World", "Python")
print("Replace 'World' with 'Python' in str2:", replace_substr)
split_str = "one,two,three".split(",")
print("Split string 'one,two,three':", split_str)
join_str = "-".join(["2024", "06", "15"])
print("Join list with '-':", join_str)

print('\n End of program')
