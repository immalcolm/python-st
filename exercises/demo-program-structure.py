# Demo on program structure
# flowchart
# Sequence Structure
print("Start of Program")
# input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
# process
next_age = age + 1
# output
print(f"Hello, {name}! Next year, you will be {next_age} years old.")
print("End of Program")

# if else elif demo
# Selection Structure
score = int(input("Enter your score (0-100): "))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Your grade is: {grade}")