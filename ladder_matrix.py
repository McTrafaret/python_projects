import random, timer, copy


def string_mul(string, number):
    return [item * number for item in string]


def string_add(first, second):
    return [item + item1 for item, item1 in zip(first, second)]


def string_x_string(string, string2):
    return [i*k for i, k in zip(string, string2)]


def matrix_input(str_number):
    matrix = []
    for i in range(str_number):
        while True:
            try:
                print('Input the string #', str(i+1), ', separate numbers by spaces.')
                string = input()
                matrix.append(list(map(int, string.split(' '))))
                break
            except ValueError:
                print('Invalid input')
                continue
    if len(matrix) == 1:
        return matrix
    for i in range(1, len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            return 'String must be equivalent size'
            break
        else:
            return matrix
            break


def matrix_add(matrix, matrix2):
    if len(matrix) != len(matrix2) or len(matrix[0]) !=  len(matrix2[0]):
        return [string_add(i, k) for i, k in zip(matrix, matrix2)] 
    else:
        return 'Can\' add those matrixes'


def matrix_mul(matrix, number):
    return [string_mul(i, number) for i in matrix]


def matrix_x_matrix(matrix, matrix2):
    if len(matrix[0]) == len(matrix2):
        columns = []
        for i in range(len(matrix2[0])):
            columns.append([string[i] for string in matrix2])
        return [[sum(string_x_string(string, column))  for column in columns] for string in matrix]
    else:
        return 'Can\'t multiply those matrixes'


def matrix_transpon(matrix):
    str_len = len(matrix[0])
    return [[string[i] for string in matrix] for i in range(str_len)]


def opred(matrix):
    if len(matrix) != len(matrix[0]):
        return 'Can\'t compute'
    elif len(matrix) == 1:
        return matrix[0][0]
    else:
        opredelitel = 0
        for index, element in enumerate(matrix[0]):
            opred_matrix = copy.deepcopy(matrix[1:])
            for string in opred_matrix:
                string.pop(index)
            opredelitel += ((-1)**(index + 2))*element*opred(opred_matrix)
        return opredelitel


def random_matrix(strings, columns):
    return [[random.randint(0, 9) for _ in range(columns)] for _ in range(strings)]


def search(matrix):
    for i in range(len(matrix[0])):
        column = [string[i] for string in matrix]
        if any(column):
            for element in column:
                if element:
                    index = column.index(element)
            matrix.insert(0, matrix.pop(index))
            break
    return matrix


def ladder(matrix):
    index = 0
    for string in matrix:
        if not matrix.index(string) == len(matrix) - 1:
            strindex = matrix.index(string)
            left = matrix[strindex + 1 :]
            del matrix[strindex + 1 :]
            matrix.extend(search(left))
        if any(string):
            for item in string:
                if item == 0:
                    continue
                else:
                    index = string.index(item)
                    break
            for other in matrix[matrix.index(string) + 1 :]:
                pos = matrix.index(other)
                matrix.insert(
                    pos,
                    string_add(
                        matrix.pop(pos),
                        string_mul(string, -other[index] / string[index]),
                    ),
                )
    return matrix



