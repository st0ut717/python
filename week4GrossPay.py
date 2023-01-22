#!/usr/bin/python3
# Get users input
hours = input("How many hours did you work?")
pay = input("How much do you get paid per hour?")
#
# convert strings to float and calulate
f_hours = float(hours)
f_pay = float(pay)
g_pay = f_hours * f_pay
#
# output
print("Pay:",(g_pay)) 


