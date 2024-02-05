#!/usr/bin/python3
""" class creation"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits square class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ method area """
        return self.__size ** 2

    def __str__(self):
        """ method __str__ """
        return "[Square] {}/{}".format(self.__size, self.__size)
