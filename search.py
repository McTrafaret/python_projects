from stest import *

def search(matrix):
    for iteration in range(len(matrix[0])):
#        counter = 20
        while True:
            column = [string[iteration] for string in matrix[iteration:]]
            leader = max(column)
            for element in column:
                if element:
                    if abs(element)<leader:
                        leader = element
            leader_index = column.index(leader) + iteration
            matrix.value.insert(iteration, matrix.value.pop(leader_index))
            for other in matrix[iteration + 1:]:
                if other[iteration]:
                    print(other[iteration], leader, sep='\n')
                    if not other[iteration] % leader:
                        matrix.value[matrix.value.index(other)] = other + matrix[iteration]*(-other[iteration]/leader)
                    else:
                        matrix.value[matrix.value.index(other)] = other + matrix[iteration]*(-1)
            print(matrix, end='\n\n')
 #           counter -=1
            column = [string[iteration] for string in matrix[iteration:]]
            print(column[1:])
            if not any(column[1:]):
 #               counter = 0
                break
    return matrix
