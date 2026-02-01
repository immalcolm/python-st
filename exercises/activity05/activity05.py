#Activity 05: Leap Year Determination
# A year is said to be a leap year if it is divisible by 4 but not divisible by 100, except those that is divisible by 400.
# Write a program to determine if an input year is a leap year.

year = int(input("Enter a year to check if it is a leap year: "))
# Initialize is_leap to False
# this is our flag variable
is_leap = False
# Check leap year conditions 
# A year is a leap year if it is divisible by 4 and not divisible by 100,
# or if it is divisible by 400
# Using logical and comparison operators and importance of parentheses
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    is_leap = True
if is_leap:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
print("End of program\n")