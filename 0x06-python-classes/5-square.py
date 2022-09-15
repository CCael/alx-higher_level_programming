#!/usr/bin/python3
"""Defines a square"""


class Square():
    """square class with size and proper validation"""

    def __init__(sef, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
    self.__size = value

    """returns the current square area"""
    def area(self):
        return self.__size ** 2

    """prints in stdout the square with the character #"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
