#!/usr/bin/python3
#
# Get users input
# hours
raw_score = input("enter the score of the test")
try:
    score = float(raw_score)
except:
    print("How about you try this with an actual number?")
    quit()
# start logic
if (score) > 1:
    print("score out of range")
    quit()
elif (score) >= 0.9:
    print("A")
elif (score) >= 0.8:
    print("B")
elif (score) >= 0.9:
    print("C")
elif (score) >= 0.6:
    print("D")
elif (score) < 0.6:
    print("F")
