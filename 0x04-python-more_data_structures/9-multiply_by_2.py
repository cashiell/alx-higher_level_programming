
#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    sorted_list = list(new_dict.keys())

    for x in sorted_list:
        new_dict[x] = new_dict[x] * 2

    return (new_dict)
