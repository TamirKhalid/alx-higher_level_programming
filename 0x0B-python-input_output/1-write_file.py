#!/usr/bin/python3
"""file write function."""


def write_file(filename="", text=""):
    """String to a UTF"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
