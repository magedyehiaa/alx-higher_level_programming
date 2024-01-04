#!/usr/bin/python3
for m in range(ord('a'), ord('z') + 1):
    if m != ord('q') and m != ord('e'):
        print("{:c}".format(m), end="")
