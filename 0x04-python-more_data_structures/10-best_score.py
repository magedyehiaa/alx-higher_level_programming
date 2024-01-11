#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    mv = 0
    mk = None
    for m, a in a_dictionary.items():
        if a > mv:
            mv = a
            mk = m
    return mk

