#!/usr/bin/python3
"""Module 9-student
class Student
"""


class student:
    """class Student that defines a student
    public instance attributes:
            first_name
            last_name
            age
    """

    def __init__(self, first_name, last_name, age):
        """Initializes a student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        "Public method
        retrieves a dictionary  representation
        of a Student instance
        """

        return self.__dict__
