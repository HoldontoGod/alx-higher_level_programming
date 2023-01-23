#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    idx = 0
    while my_list and idx < x:
        try:
            print("{:d}".format(my_list[idx]), end="")
            idx += 1
        except IndexError:
            break
        print()
        return idx
