'''
That module lets you create a string and matrix from strings,
it lets you perform different operations on them.
'''

import random, copy

def random_matrix(num_of_str, num_of_col, min_gen=0, max_gen=9):

    '''
    Returns num_of_str x num_of_col matrix,
    with random numbers from min_gen to max_gen.
    '''

    return Matrix([String([random.randint(min_gen, max_gen) for _ in range(num_of_col)]) for _ in range(num_of_str)])


def input_matrix():
    '''
    Input matrix manually, string by string, no arguments needed.
    '''

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

    '''
    Defines a Matrix, which is basically a two-dimensional list.
    '''

    def __init__(self, matrix):

        '''
        Requires a list of Strings as an argument, returns Matrix object.
        '''

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
        '''
        Overloads the "+" operator, so you can add Matrices.
        '''
        if isinstance(other, Matrix):
            pass
        if len(self) == len(other):
            if len(self[0]) == len(other[0]):
                return Matrix([string + string1 for string, string1 in zip(self, other)])
            raise TypeError('To add Matrixes they should be equivalent size')
        else:
            raise TypeError("Can't add Matrix to %s" % type(other))

    def __mul__(self, other):
        '''
        Overloads the "*" operator, so you can multiply Matrix by number or by
        other Matrix. Hovewer, for some reason(which i don't know yet), you
        can't write like "5*Matrix", you can only use it like "Matrix*5".
        '''
        if isinstance(other, float) or isinstance(other, int):
            return Matrix([string * other for string in self])
        elif isinstance(other, Matrix):
            if len(self[0]) == len(other):
                columns = []
                matrix = []
                for i in range(len(other[0])):
                    columns.append(String([string[i] for string in other]))

                for string in self:
                    element = []
                    for column in columns:
                        element.append(sum((column * string).value))

                    matrix.append(String(element))

                return Matrix(matrix)
            else:
                raise TypeError('Number of columns of first matrix  should be equal to number of strings of second matrix.')
        else:
            raise TypeError('Unsupported operand types for "*"')

    def __len__(self):
        '''
        Returns the number of Strings.
        '''
        return len(self.value)

    def __repr__(self):
        '''
        Formats the Matrix, so it would be displayed nicely.
        '''
        return '\n'.join(('{}'.format(i) for i in self.value))

    def __getitem__(self, key):
        '''
        Returns take a string #key or a slice of strings, which is basically a
        smaller matrix.
        '''
        if isinstance(key, slice):
            if key.start:
                if key.start>=len(self):
                    start = len(self)
                else:
                    start = key.start
            else:
                start = 0
            if key.stop:
                if key.stop>=len(self):
                    stop = len(self)
                else:
                    stop = key.stop
            else:
                stop = len(self)
            if key.step:
                step = key.step
            else:
                step = 1
            return Matrix([self.value[i] for i in range(start, stop,
                                                        step)])
        return self.value[key]

    def __iter__(self):
        '''
        I don't know what that thing does, i just wanted to get this thing
        iteratable.
        '''
        self.index = 0
        return self

    def __next__(self):
        '''
        Lets you iterate with the elements of the Matrix.
        '''
        if self.index < len(self):
            result = self[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def transpose(self):
        '''
        Returns transposed Matrix(switches strings and columns).
        '''
        return Matrix([String([string[i] for string in self]) for i in range(len(self[0]))])

    def determinant(self):
        '''
        Returns Matrix determinant if Matrix is square, else raises the
        Exception.
        '''
        if len(self) != len(self[0]):
            raise TypeError('Matrix must be square to compute the determinant.')
        elif len(self) == 1:
            return self[0][0]
        else:
            det = 0
            for index, element in enumerate(self[0]):
                det_matrix = copy.deepcopy(self[1:].value)
                for string in det_matrix:
                    string.value.pop(index)

                det += (-1) ** (index + 2) * element * Matrix.determinant(Matrix(det_matrix))

            return det

    def alg_extension(self, *indexes):
        '''
        Returns algebraic_extension, requires string and column indexes, when
        calling write string indexes first.
        '''
        if len(indexes) % 2 == 0:
            num_of = int(len(indexes)/2)
            str_indexes = list(indexes[:num_of])
            str_indexes.sort()
            str_indexes.reverse()
            col_indexes = list(indexes[num_of:])
            col_indexes.sort()
            col_indexes.reverse()
            ad_minor = copy.deepcopy(self.value)
            for index in str_indexes:
                ad_minor.pop(int(index)-1)
            for string in ad_minor:
                for index in col_indexes:
                    string.value.pop(int(index)-1)
            extension = ((-1)**(sum(indexes)))*(Matrix(ad_minor).determinant())
            return extension
        else:
            raise TypeError('You must pass k column numbers AND k string numbers.')

    def inverse(self):
        '''
        Returns inverse matrix, but only if matrix is square and the
        determinant != 0, else raises an Exception.
        '''
        if self.determinant():
            alg_matrix = [String([self.alg_extension(str_index+1, col_index+1) for col_index in range(len(self[0]))]) for str_index in range(len(self))]
            alg_matrix = Matrix(alg_matrix).transpose()
            inverse = alg_matrix * (1/self.determinant())
            return inverse
        else:
            raise ValueError('To compute inverse matrix, the determinant must be above zero.')

class String():         #add (Matrix) if don't work
    '''
    Converts a list of numbers into a String objuct, which could be passed to
    build Matrix. You could also perform operations on strings.
    '''

    def __init__(self, string):
        '''
        Requires a list of numbers, returns String object.
        '''
        if not isinstance(string, list):
            raise ValueError('List must be passed as an argument')
        else:
            for element in string:
                if not isinstance(element, int):
                    if not isinstance(element, float):
                        raise ValueError('String must contain numbers')

            self.value = string

    def __add__(self, other):
        '''
        Overloads the "+" operator so you can add Strings.
        '''
        if isinstance(other, String):
            return String([item1 + item2 for item1, item2 in zip(self, other)])
        raise ValueError

    def __mul__(self, other):
        '''
        Overloads the "*" operator so you can multiply a String by number.
        '''
        if isinstance(other, int) or isinstance(other, float):
            return String([item * other for item in self])
        if isinstance(other, String):
            return String([item * item2 for item, item2 in zip(self, other)])
        raise TypeError

    def __len__(self):
        '''
        Returns the number of columns.
        '''
        return len(self.value)

    def __repr__(self):
        '''
        Formats the String so it could be displayed nicely.
        '''
        return ' '.join(('{:>7.2f}'.format(i) for i in self))

    def __getitem__(self, key):
        '''
        Returns the element #key.
        '''
        return self.value[key]

    def __iter__(self):
        '''
        The same as with Matrix.
        '''
        self.index = 0
        return self

    def __next__(self):
        '''
        Lets you iterate elements of the strings.
        '''
        if self.index < len(self):
            result = self[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


def search(matrix):
    for iteration in range(len(matrix[0])):
        while True:
            column = [string[iteration] for string in matrix[iteration:]]
            if not column:
                break
            leader = max(column)
            if not leader:
                leader = min(column)
            for element in column:
                if element:
                    if abs(element)<leader:
                        leader = element
            leader_index = column.index(leader) + iteration
            matrix.value.insert(iteration, matrix.value.pop(leader_index))
            for other in matrix[iteration + 1:]:
                if other[iteration]:
                    if not other[iteration] % leader:
                        matrix.value[matrix.value.index(other)] = other + matrix[iteration]*(-other[iteration]/leader)
                    elif other[iteration]>0:
                        if matrix[iteration][iteration]>0:
                            matrix.value[matrix.value.index(other)] = other + matrix[iteration]*(-1)
                        else:
                            matrix.value[matrix.value.index(other)] = other + matrix[iteration]
                    else:
                        if matrix[iteration][iteration]>0:
                            matrix.value[matrix.value.index(other)] = other + matrix[iteration]
                        else:
                            matrix.value[matrix.value.index(other)] = other + matrix[iteration]*(-1)
            column = [string[iteration] for string in matrix[iteration:]]
            if not any(column[1:]):
                break
    return matrix
