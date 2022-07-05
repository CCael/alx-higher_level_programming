#!/usr/bin/python3
"""Module 5-save_to_json_file
Writes Object to a text file
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file
    using a JSON representation
    """

    with open(filename, "w") as f:
        json.dump(my_obj, f)
