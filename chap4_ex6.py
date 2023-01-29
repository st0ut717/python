#!/usr/bin/python3
#
#set Vars
#rph = 10.5
max_hour = 40
#rot = 1.5 * (rph)
#
def computepay(hours, rate):
    if (hours) <= (max_hour):
        pay_for_hours = (rate) * (hours)
        print(pay_for_hours)
    else:
        pay_for_hours = (rate) * (max_hour)
        over_hours = (hours) - (max_hour)
        ot_rate = ((rate) * 1.5) * (over_hours)
        tot_pay = (pay_for_hours) + (ot_rate)
        print("Pay", tot_pay)
# Get users input
# hours
def hoursworked():
    raw_hours = input("How many hours did you work?")
    try:
        hours = float(raw_hours)
    except:
        print("How about you try this with an actual number?")
        hours()
    return hours
#
# rate
def hourrate():
    raw_rate = input("What is your hourly rate?")
    try:
        rate = float(raw_rate)
    except:
        print("How about you try this with an actual number?")
        rate()
    return rate

# start logic
hrs = hoursworked()
rts = hourrate()
hours = hrs
rate = rts
computepay(hours, rate)
