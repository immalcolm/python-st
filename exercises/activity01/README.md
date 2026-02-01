# GST Calculation
Given that the price of an item is $250 and the gst is 9%
Write a program to calculate and display the total cost of the item.

**QA Challenge:** Format the output to 2 decimal places.

**QA Challenge:** Write a test plan
- Test Case 1: Verify that the total cost is calculated correctly.
- Test Case 2: Verify that the output is formatted to 2 decimal places.
- Test Case 3: Verify that the program handles different item prices and gst rates correctly.
- Test Case 4: Verify that the program runs without errors.
- Test Case 5: Verify that the output matches the expected string format.
- Test Case 6: Verify that the program can be easily modified for different item prices and gst rates.
- Test Case 7: Verify that the program includes comments for clarity.
- Test Case 8: Compliance/logical correctness of the calculations. GST added to the item price or inclusive


|Test Case	| Input	| Expected Result	| Result|
|-----------|-------|-------------------|-------|
|Standard Calculation	    |250, 9% GST	|$272.50|	Pass/Fail|
|Zero Value	|0, 9% GST	    |$0.00	|Pass/Fail|
|Data Type	|"250" (String)	|Graceful Error	|Pass/Fail|