#!/usr/bin/python3
for var1 in range(0, 10):
    for var2 in range(var1 + 1, 10):
        if var1 == 8 and var2 == 9:
            print("{}{}".format(var1, var2))
        else:
            print("{}{}".format(var1, var2), end=", ")
