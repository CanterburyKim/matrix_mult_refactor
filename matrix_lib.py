"""
Main library to handle matrix multiply
"""

def matrix_vector_mult(matrix, p):
    """
    TODO: refactor this 
    multiply an m x n matrix and m-dimensional vector p
    matrix is a list of lists
    p is a tuple
    """
    result_list = []

    for matrix_row in matrix:
        row = []
        for j in range(len(p[0])):
            row.append(sum(matrix_row[i]*p[i][j] for i in range(len(matrix_row))))
        result_list.append(row)

    return result_list
