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

if not os.path.isfile(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('[]')

    if len(sys.argv) > 1:
        input = load_from_json_file(filename)
        for i in sys.argv[1:]:
            input.append(i)

save_to_json_file(input, filename)
