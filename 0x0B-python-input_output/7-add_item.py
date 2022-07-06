#!/usr/bin/python3
"""Module 7-add_item
adds all arguments to a Python list
"""

import os
import json
import sys


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = 'add_item.json'

input = []

if os.path.exists(my_file) and os.path.getsize(my_file) > 0:
    input = load_from_json_file(filename)

    if len(sys.argv) > 1:
        for i in sys.argv[1:]:
            input.append(i)

save_to_json_file(input, filename)
