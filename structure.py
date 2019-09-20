import random, copy

def random_matrix():
    pass

def input_matrix():
    string = None
    matrix = []
    print('Input strings, separate numbers by spaces, when done printing a string press Enter.\n',
          'When done inputing strings press Enter:')
    while string != '':
        try:
            string = input()
            if string:
                string = string.split(' ')
                matrix.append(String(list(map(float, string))))
        except ValueError:
            print('Invalid input')
            continue
    return Matrix(matrix)

class Matrix:

    def __init__(self, matrix):
        if not isinstance(matrix, list):
            raise ValueError('List must be passed as an argument')
        else:
            for element in matrix:
                if not isinstance(element, String):
                    raise ValueError('Matrix must contain Strings')
            for string in matrix:
                if len(matrix[0].value) != len(string.value):
                    raise ValueError('Strings must be equivalent size')
            self.value = matrix

    def __add__(self, other):
        if isinstance(other, Matrix):
            if len(self) == len(other) and len(self.value[0]) == len(other.value[0]):
                return Matrix([string + string1  for string, string1 in zip(self.value, other.value)])
            else:
                raise TypeError('To add Matrixes they should be equivalent size')
        else:
            raise TypeError('Can\'t add Matrix to %s' % type(other))

    def __len__(self):
        return len(self.value)


class String(Matrix):

    def __init__(self, string):
        if not isinstance(string, list):
            raise ValueError('List must be passed as an argument')
        else:
            for element in string:
                if not (isinstance(element, int) or isinstance(element, float)):
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

    def __len__(self):
        return len(self.value)
