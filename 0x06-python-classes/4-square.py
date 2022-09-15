#!/usr/bin/python3
"""Defines a square"""


class Square:
    """square class withsize and proper validation"""

    """Initializes the data"""
    def __init__(self, size=0):
        self.__size = size

    @property
    """Retrieves the size"""
    def size(self):
        return self.__size

    @size.setter
    """Sets the size of a value"""
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer""")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """returns the current square area"""
    def area(self):
        return self.__size ** 2
