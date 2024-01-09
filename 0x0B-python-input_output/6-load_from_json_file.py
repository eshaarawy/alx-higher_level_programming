#!/usr/bin/python3
"""Define write_file"""


import json


def load_from_json_file(filename):
    """Return json representation"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
