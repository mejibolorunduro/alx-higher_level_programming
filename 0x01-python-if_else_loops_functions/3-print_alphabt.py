#!/usr/bin/python3
for d in range(97, 123):
    if (d == 101) or (d == 113):
        continue
    print(chr(d).format(), end="")
