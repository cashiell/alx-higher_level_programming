#!/usr/bin/python3
def convert_to_roman(assume_num):
    to_convert = 0
    high_val = max(assume_num)

    for x in assume_num:
        if high_val > x:
            to_convert = to_convert + x

    return (high_val - to_convert)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_number = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    keys_convertion = list(rom_number.keys())

    x = 0
    last_roman = 0
    assume_num = [0]

    for j in roman_string:
        for r in keys_convertion:
            if r == j:
                if rom_number.get(j) <= last_roman:
                    x = x + convert_to_roman(assume_num)
                    assume_num = [rom_numner.get(j)]
                else:
                    assume_num.append(rom_number.get(j))

                last_roman = rom_number.get(j)

    x = x + convert_to_roman(assume_num)

    return (x)
