
# define column headers
a, b, c = "a", "b", "a to the power of b"
a_value = 1
b_value = 2
c_value = a_value ** b_value
print (f"{a:<10} | {b:<10} | {c:<15}")
print (f"{'-'*10} + {'-'*10} + {'-'*15}")
print (f"{a_value:<10} | {b_value:<10} | {c_value:<15}")
a_value = 2
b_value = 3
c_value = a_value ** b_value
print (f"{a_value:<10} | {b_value:<10} | {c_value:<15}")
a_value = 3
b_value = 4
c_value = a_value ** b_value
print (f"{a_value:<10} | {b_value:<10} | {c_value:<15}")
a_value = 4
b_value = 5
c_value = a_value ** b_value
print (f"{a_value:<10} | {b_value:<10} | {c_value:<15}")
a_value = 5
b_value = 6
c_value = a_value ** b_value
print (f"{a_value:<10} | {b_value:<10} | {c_value:<15}")
print("End of program\n")
#using just print formatted
print ("{a:<10} | {b:<10} | {c:<15}".format(a=1, b=2, c=1**2))

# easier way using a loop
limit = 5
a, b, c = "a", "b", "a to the power of b"
print (f"{a:<10} | {b:<10} | {c:<15}")
print (f"{'-'*10} + {'-'*10} + {'-'*15}")
for a_value in range(1, 6):
    b_value = a_value + 1
    c_value = a_value ** b_value
    print (f"{a_value:<10} | {b_value:<10} | {c_value:<15}")    
print('End of program\n ')