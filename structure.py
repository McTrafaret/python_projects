import random, copy

def random_matrix():
    pass

def input_matrix():
    pass

class String:

    def __init__(self, string):
        if not isinstance(string, list):
            raise ValueError('List must be passed as an argument')
        else:
            for element in string:
                if not isinstance(element, int) or isinstance(element, float):
                    raise ValueError('String must contain numbers')
            self.value = string

    def __add__(self, other):
        if isinstance(other, String):
            return String([item1 + item2 for item1, item2 in zip(self.value, other.value)])
        else:
            raise ValueError

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return String([item * other for item in self.value])
        elif isinstance(other, String):
            return String([item*item2 for item, item2 in zip(self.value, other.value)])
        else:
            raise TypeError

class Matrix:

    def __init__(self, matrix):
        if not isinstance(matrix, list):
            raise ValueError('List must be passed as an argument')
        else:
            for element in matrix:
                if not isinstance(element, list):
                    raise ValueError('Matrix must contain lists')
            for string in matrix:
                if len(matrix[0]) != len(string):
                    raise ValueError('Strings must be equivalent size')
            self.value = matrix

    def __add__(self, other):
        if isinstance(matrix, Matrix):
            pass
