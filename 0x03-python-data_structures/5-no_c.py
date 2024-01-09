#!/usr/bin/python3
def no_c(my_string):
    mag = ""
    for m in range(len(my_string)):
        if (my_string[m] != 'c' and my_string[m] != 'C'):
            mag += my_string[m]
    return mag
