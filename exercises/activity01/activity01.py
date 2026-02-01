'''
Given that the price of an item is $250 and the gst is 9%
Write a program to calculate and display the total cost of the item.
QA Challenge: Format the output to 2 decimal places.
QA Challenge: Write a test plan
- Test Case 1: Verify that the total cost is calculated correctly.
- Test Case 2: Verify that the output is formatted to 2 decimal places.
- Test Case 3: Verify that the program handles different item prices and gst rates correctly.
- Test Case 4: Verify that the program runs without errors.
- Test Case 5: Verify that the output matches the expected string format.
- Test Case 6: Verify that the program can be easily modified for different item prices and gst rates.
- Test Case 7: Verify that the program includes comments for clarity.
- Test Case 8: Compliance and logical correctness of the calculations. GST added to the item price or inclusive
'''

item_price = 250
gst  = 0.09
total_cost = item_price + (item_price * gst)
print("The total cost of the item is: ${:.2f}".format(total_cost))
# Alternative way to print the result
#print("The total cost of the item is: $", total_cost)
# alternative way to print the result with rounding
#print("The total cost of the item is: $", round(total_cost, 2))
#print("The total cost of the item is: $ %.2f" % total_cost)
print('\n new line')
print("End of program")

# Output should be: The total cost of the item is: $272.50

