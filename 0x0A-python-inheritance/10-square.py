#!/usr/bin/python3
""" class creation """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ inherits square class """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ mehtod area """
        return self.__size ** 2
