#!/usr/bin/python3
""" defining json """


def class_to_json(obj):
    """return dictionary desc."""
    return obj.__dict__
