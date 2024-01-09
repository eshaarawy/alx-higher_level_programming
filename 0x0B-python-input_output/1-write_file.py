#!/usr/bin/python3
"""Define write_file"""


def write_file(filename="", text=""):
    """Reads and print"""
    with open(filename, "w", encoding='utf-8') as file:
        return file.write(text)
