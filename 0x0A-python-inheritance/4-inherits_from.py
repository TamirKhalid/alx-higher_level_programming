#!/usr/bin/python3
""" sub class of a class return """
def inherits_from(obj, a_class):
    """ if the object is an instance of a class, return TRUE """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
