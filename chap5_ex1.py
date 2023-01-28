#!/usr/bin/python3
#
# get users input on loop
# Test for int
# if input not number print error and loop
# break on 'done'
# count of numbers added
# add all numbers
# avg of all numbers
# 

i = 0
y = 0
while True:
    print('type done when done')
    line = input('Gimme a number: ')
    i += 1
    if (line) == "done":
            i -= 1
            break
    try:
        x = int(line)
        y = (x + y)
    except:
        print('Thats not a number')
        if i == 1:
            i = 0
        i -= 1
    #print('number entered= ', (x))
    #print(' sum = ', (y))
    #print('numbers entered= ', (i))
print('total numbers entered:', (i))
print('sum of all numbers entered:', (y))
z = (y) / (i)
print('average of numbers entered: ', (z))
