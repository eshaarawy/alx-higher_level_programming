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
        try:
            for att in attrs:
                if type(att) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict

    def reload_from_json(self, json):
        for key, val in json.items():
            if key in self.__dict__:
                self.__dict__[key] = val
