#!/usr/bin/python3
#4-new_in_list.py
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    x = [j for j in my_list]
    x[idx] = element
    return (x)
