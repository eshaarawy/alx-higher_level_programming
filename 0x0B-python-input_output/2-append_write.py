#!/usr/bin/python3
"""Define write_file"""


def append_write(filename="", text=""):
    """Reads and print"""
    with open(filename, "a", encoding='utf-8') as file:
        return file.write(text)
