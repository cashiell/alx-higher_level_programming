#!/usr/bin/python3
#5-no_c.py
def no_c.py(my_string):
    x = [j for j in my_string if j != 'c' and j != 'C']
    return ("".join(x))
