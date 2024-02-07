#!/usr/bin/python3
"""text file read & print functions"""


def read_file(filename=""):
    """ text file read & print functions"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
