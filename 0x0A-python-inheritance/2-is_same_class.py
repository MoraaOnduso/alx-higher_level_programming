#!/usr/bin/python3
"""Define a class-checking function"""


def is_same_class(obj, a_class):
    """Returns True if object is class a_class, if not false"""
    return (type(obj) == a_class)
