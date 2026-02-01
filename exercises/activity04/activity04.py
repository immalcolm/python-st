# Activity 04

monthly_sales = int(input("Enter the monthly sales amount of sales agent: "))
commission_high = 0.10
commission_low = 0.05
threshold = 10000

comission_rate = 0.0
if monthly_sales > threshold:
    commission = monthly_sales * commission_high
    comission_rate = commission_high
else:
    commission = monthly_sales * commission_low
    comission_rate = commission_low

# we could also use a ternary operator here
# comission_rate = commission_high if monthly_sales > threshold else commission_low
# print("The comission rate is : " + str(comission_rate*100) + "%")
print(f"The comission rate is : {comission_rate*100:.0f}%")

# display commission amount with 2 decimal places
print(f"The commission for the sales agent is: ${commission:.2f}")
