#!/usr/bin/python3
"""Module 3-to_json_string
returns the JSON representation
"""

import json


def to_json_string(my_obj):
    """JSON representation of an object (string)
    """

    return json.dumps(my_obj)