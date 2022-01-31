#!/usr/bin/python3
"""Locked class module"""


class LockedClass:
    """object prevents dynamic attribute"""

    __slots__ = ['first_name']
