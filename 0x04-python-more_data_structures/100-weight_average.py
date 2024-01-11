#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        return (sum(m * a for m, a in my_list) / sum (a for m, a in my_list))
