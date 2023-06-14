#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    sorted_keys = list(a_dictionary.keys())

    for new_dict in sorted_keys:
        if value == a_dictionary.get(new_dict):
            del a_dictionary[new_dict]

    return (a_dictionary)
