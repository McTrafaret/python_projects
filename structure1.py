import random, copy

def random_matrix():
    pass


def input_matrix():
    string = None
    matrix = []
    print('Input strings, separate numbers by spaces, when done printing a string press Enter.\n', 'When done inputing strings press Enter:')
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
            pass
        if len(self) == len(other):
            if len(self.value[0]) == len(other.value[0]):
                return Matrix([string + string1 for string, string1 in zip(self.value, other.value)])
            raise TypeError('To add Matrixes they should be equivalent size')
        else:
            raise TypeError("Can't add Matrix to %s" % type(other))

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Matrix([string * other for string in self.value])
        if isinstance(other, Matrix):
            if len(self.value[0]) == len(other):
                columns = []
                matrix = []
                for i in range(len(other.value[0])):
                    columns.append(String([string.value[i] for string in other.value]))

                for string in self.value:
                    element = []
                    for column in columns:
                        element.append(sum((column * string).value))

                    matrix.append(String(element))

                return Matrix(matrix)
            raise TypeError('Number of columns of first matrix  should be equal to number of strings of second matrix.')
        else:
            raise TypeError('Unsupported operand types for "*"')

    def __len__(self):
        return len(self.value)

    def __repr__(self):
        return '\n'.join(('{}'.format(i) for i in self.value))

    def transpose(self):
        return Matrix([String([string.value[i] for string in self.value]) for i in range(len(self.value[0]))])

    def determinant(self):
        if len(self) != len(self.value[0]):
            raise TypeError('Matrix must be square to compute the determinant.')
        elif len(self) == 1:
            return self.value[0].value[0]
        else:
            det = 0
            for index, element in enumerate(self.value[0].value):
                det_matrix = copy.deepcopy(self.value[1:])
                for string in det_matrix:
                    string.value.pop(index)

                det += (-1) ** (index + 2) * element * Matrix.determinant(Matrix(det_matrix))

            return det


class String(Matrix):

    def __init__(self, string):
        if not isinstance(string, list):
            raise ValueError('List must be passed as an argument')
        else:
            for element in string:
                if not isinstance(element, int):
                    if not isinstance(element, float):
                        raise ValueError('String must contain numbers')

            self.value = string

    def __add__(self, other):
        if isinstance(other, String):
            return String([item1 + item2 for item1, item2 in zip(self.value, other.value)])
        raise ValueError

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return String([item * other for item in self.value])
        if isinstance(other, String):
            return String([item * item2 for item, item2 in zip(self.value, other.value)])
        raise TypeError

    def __len__(self):
        return len(self.value)

    def __repr__(self):
        return ' '.join(('{:^7.2f}'.format(i) for i in self.value))
