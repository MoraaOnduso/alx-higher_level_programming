#!/usr/bin/python3
def print_sorte_dictionary(a_dictionary):
    for k in sorted(a_dictionary):
        print("{}: {}".format(k, a_dictionary[k]))
