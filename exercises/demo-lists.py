# Lists Demo
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
# Accessing elements
print("First element of list1:", list1[0])
print("Last element of list2:", list2[-1])
# Slicing
print("Sliced list1 (1:4):", list1[1:4])
# Appending elements
list1.append(6)
print("List1 after appending 6:", list1)
# Removing elements
list2.remove('c')
print("List2 after removing 'c':", list2)
# empty list
empty_list = []
print("Empty List:", empty_list)
# different element types in a list
mixed_list = [1, "two", 3.0, True]
print("Mixed List:", mixed_list)

# list in a list
nested_list = [list1, list2]
print("Nested List:", nested_list)
# Length of a list
print("Length of list1:", len(list1))
print("Length of list2:", len(list2))   

# Iterating through a list
print("Elements in list1:")
for item in list1:
    print(item)

