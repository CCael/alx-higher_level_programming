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

        return obj.__dict__


if __name__ == '__main__':
    students = [Student("Caleb", "Curry", 19), Student("Collins", "Cael", 21)]

    for student in students:
        j_student = student.to_json()
        print(type(j_student))
        print(j_student['first_name'])
        print(type(j_student['first_name']))
        print(j_student['age'])
        print(type(j_student['age']))
