#!/usr/bin/python3
""" returns same or inherit class  from a class """
def is_kind_of_class(obj, a_class):
    """ true if the object is an instance of a class, return TRUE """
    if isinstance(obj, a_class):
        return True
    else:
        return False
