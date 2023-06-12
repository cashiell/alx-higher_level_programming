#!/usr/bin/python3
# 9-max_integer.py
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    j = my_list[0]
    for x in range(len(my_list)):
        if my_list[x] > j:
            j = my_list[i]

    return (j)
