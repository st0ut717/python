#!/usr/bin/python3
#
# Get users input
# hours
# start logic
def grade(score):
    if (score) > 1:
        print("score out of range")
    elif (score) >= 0.9:
        grd = "A"
        return grd
    elif (score) >= 0.8:
        grd = "B"
        return grd
    elif (score) >= 0.7:
        grd = "C"
        return grd
    elif (score) >= 0.6:
        grd = "D"
        return grd
    elif (score) < 0.6:
        grd = "F"
        return grd
#
raw_score = input("enter the score of the test")
try:
   score = float(raw_score)
   grd = grade(score)
   print(grd)
except:
    print("How about you try this with an actual number?")

