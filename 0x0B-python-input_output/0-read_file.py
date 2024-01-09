#!/usr/bin/python3
"""Define read_file"""


def read_file(filename=""):
    """Reads and print"""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
