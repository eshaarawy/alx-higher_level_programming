#!/usr/bin/python3
"""Define write_file"""


import json


def save_to_json_file(my_obj, filename):
    """Return json representation"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
