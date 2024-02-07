#!/usr/bin/python3
"""text file string append"""


def append_write(filename="", text=""):
    """text file string append"""
    with open(filename, 'a') as f:
        return f.write(text)
