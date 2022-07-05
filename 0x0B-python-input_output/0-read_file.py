#!/usr/bin/python3
"""Module 0-read_file.
Reads a text file
"""


def read_file(filename=""):
    """Reads a UTF* text file and prints
    to stdout.
    """

    with open(filename, encoding="utf-8") as f:
        read_text = f.read()
        print(read_text, end="")
