#!/usr/bin/python3
""" BaseGeometry inherits class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ BaseGeometry inherits """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ method area """
        return self.__width * self.__height

    def __str__(self):
        """ method __str__ """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
