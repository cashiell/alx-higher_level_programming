#!/usr/bin/python3
#1-element_at.py
def element_at(my_list, j):
    """A function thata retrives an element from a list."""
    if j < 0 or j > (len(my_list) - 1):
        return None
    return (my_list[j])
