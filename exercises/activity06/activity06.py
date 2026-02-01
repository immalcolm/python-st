'''
The rate for photocopy in a printing shop is as follows:

- First 100 pages: 3 cents per page
- Next 200 pages: 2 cents per page
- Over 300 pages: 1 cent per page

Calculate the cost for printing based on the number of pages input.
'''

# Activity 06
pages = int(input("Enter the number of pages to be printed: "))
# Initialize cost variable
cost = 0.0

# Calculate cost based on the number of pages
# Use conditional statements to determine the cost brackets
# selection structure
if pages <= 100:
    cost = pages * 0.03
elif pages <= 300:
    cost = (100 * 0.03) + ((pages - 100) * 0.02)
else:
    cost = (100 * 0.03) + (200 * 0.02) + ((pages - 300) * 0.01) 
print(f"The total cost for printing {pages} pages is: ${cost:.2f}")
print("End of program\n")
