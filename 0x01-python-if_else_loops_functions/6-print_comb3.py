#!/usr/bin/python3
for m in range(10):
    for a in range(m, 10):
        if m < a:
            print("{:d}{:d}".format(m, a),
                  end="\n" if m == 8 and a == 9 else ", ")
