from search import *

def test(a,b,c=0,d=9):
    matrix = random_matrix(a,b,c,d)
    print(matrix)
    print()
    print(search(matrix))
