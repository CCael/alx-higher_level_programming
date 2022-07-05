#!/usr/bin/python3
"""Model 1-write_file.py
Wrirtes a string to UTF8
"""


def write_file(filename="", text=""):
    """Returns number of characters
    """

    count = 0

    with open(filename, encoding="utf-8"):
        text = f.readlines()
        for line in text:
            count += 1

    return count


if __name__ == '__main__':
    filename = "Mine_file_1.txt"
    count = number_of_lines(filename)
    print("{} has {:d} lines".format(filename, count))
