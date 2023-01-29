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
max = None
min = None 
while True:
    line = input('Gimme a number: ')
    if (line) == "done":
            break
    try:
        x = int(line)
    except:
        print('Invalid input')
    if max is None:
        max = x
    if min is None:
        min = x
        continue
    if x >= (max):
        max = x
    if x <= (min):
        min = x
    
print('Maximum is', (max))
print('Minimum is', (min))
