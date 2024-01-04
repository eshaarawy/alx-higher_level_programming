#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represents a Rectangle """
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for rectangle width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for rectangle height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return (self.__height + self.__width) * 2
