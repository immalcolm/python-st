# Calculates the Body Mass Index (BMI) based on user input for weight and height

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate BMI using formula
bmi = weight / (height * height)

# use formatted string literals (f-strings) to display results
# precision of 2 decimal places
print("Your height is: {:.2f} m".format(height))    
print("Your weight is: {:.2f} kg".format(weight))
print("Your BMI is: {:.2f}".format(bmi))

# newer way using f-strings (Python 3.6+)
print(f"Your height is: {height:.2f} m")
print(f"Your weight is: {weight:.2f} kg")
print(f"Your BMI is: {bmi:.2f}")  

# Alternative way to print the results using string concatentation and type conversion
# decimals may not be formatted nicely
print("Your height is: " + str(height) + " m")
print("Your weight is: " + str(weight) + " kg")
print("Your BMI is: " + str(bmi))
print('\n End of program')

# variable types in Python
int_var = 10          # integer
float_var = 10.5     # floating-point number
str_var = "Hello"    # string
bool_var = True      # boolean

'''
multi
line 
comment
'''