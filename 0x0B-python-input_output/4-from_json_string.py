#!/usr/bin/python3
"""Object represente by JSON string"""

import json


def from_json_string(my_str):
    """Object represente by JSON string"""
    return json.loads(my_str)
