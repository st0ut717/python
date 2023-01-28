#!/usr/bin/python3
#
# get users input on loop
# Test for int
# if input not number print error and loop
# break on 'done'
# count of numbers added
# show min
# show max
# 
max = 0 
min = 0 
while True:
    print('type done when done')
    line = input('Gimme a number: ')
    if (line) == "done":
            break
    try:
        x = int(line)
    except:
        print('Thats not a number')
    if max == 0:
        max = x
    if min == 0:
        min = x
    if x >= (max):
        max = x
    if x <= (min):
        min = x
    
print('minimum value entered: ', (min))
print('maximum value entered: ', (max))
