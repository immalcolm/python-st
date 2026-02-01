# Program Interactivity Demo
# This program calculates running pace and estimated time to complete a run

name = input("Enter your name:")
distance = float(input("Enter the distance covered (km): " ))
time = int(input("Enter number of minutes taken (mins): " ))
remaining = float(input("Distance left to cover (km): " ))
pace = time/distance
mins_more = pace * remaining
print(" Your pace is ", pace, "mins/km")
print(" You should complete your run in", mins_more, "mins")

# Demonstrating different ways to print output
print(f"Hello, {name}! You have {remaining:.2f} km left to run.")
print("Hello, {}! You have {:.2f} km left to run.".format(name, remaining))
print("Hello, " + name + "! You have " + str(round(remaining, 2)) + " km left to run.")