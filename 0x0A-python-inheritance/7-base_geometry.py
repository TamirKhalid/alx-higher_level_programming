#!/usr/bin/python3
""" class creation  """


class BaseGeometry:
    """ Class BaseGeometry """
    def area(self):
        """ method  area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
