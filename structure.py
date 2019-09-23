import random, copy

def random_matrix(num_of_str, num_of_col, min_gen=0, max_gen=9):
    return Matrix([String([random.randint(min_gen, max_gen) for _ in range(num_of_col)]) for _ in range(num_of_str)])


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
        elif isinstance(other, Matrix):
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
            else:
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

    def alg_extension(self, *indexes):
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
        if self.determinant():
            alg_matrix = [String([self.alg_extension(str_index+1, col_index+1) for col_index in range(len(self.value[0]))]) for str_index in range(len(self))]
            alg_matrix = Matrix(alg_matrix).transpose()
            inverse = alg_matrix * (1/self.determinant())
            return inverse
        else:
            raise ValueError('To compute inverse matrix, the determinant must be above zero.')



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
