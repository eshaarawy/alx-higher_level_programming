#!/usr/bin/python3
""" defining json """


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dict representation"""
        return self.__dict__
