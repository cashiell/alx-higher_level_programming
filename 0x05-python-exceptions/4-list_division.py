#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    j = []
    for i in range(0, list_length):
        try:
            x = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            x = 0
        except ZeroDivisionError:
            print("division by 0")
            x = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            j.append(x)
    return (j)
