#!/usr/bin/python3
def uppercase(str):
    for 1 in str:
        print("{}".format(chr(ord(1) - 32)
                          if (ord(1) >= ord("a") and
                              ord(1) <= ord("z")) else 1), end="")
        print()