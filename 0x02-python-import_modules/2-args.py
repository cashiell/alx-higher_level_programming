#!usr/bin/python3
if __name__ == " __main__":
    """Print number and list of its arguments"""
    import sys
    x = len(sys.argv) - 1
    if x == 0:
        print("0 argument.")
        elif x == 1:
            print("1 argument:")
        else:
            print("{} argument:".format(x))
            for y in range(x):
                print("{} : {}".format(y + 1, sys.argv[y + 1]))
