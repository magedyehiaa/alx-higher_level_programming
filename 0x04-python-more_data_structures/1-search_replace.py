#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda m: replace if m == search else m, my_list))
