#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []

        for column_index in row:
            new_row.append(column_index ** 2)
        new_matrix.append(new_row)

    return (new_matrix)
