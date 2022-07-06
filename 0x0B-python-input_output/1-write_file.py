#!/usr/bin/python3
"""Model 1-write_file.py
Wrirtes a string to UTF8
"""


def write_file(filename="", text=""):
    """Returns number of characters
    """

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
