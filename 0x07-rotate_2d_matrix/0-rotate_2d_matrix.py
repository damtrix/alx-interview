#!/usr/bin/python3
'''2D matrix'''


def rotate_2d_matrix(matrix):
    '''rotates a 2d matrix 90° clockwise
    Returns: Nothing'''
    new_matrix = matrix.copy()

    for i in range(len(new_matrix)):
        a = []
        for j in range(len(new_matrix), 0, -1):
            a.append(new_matrix[j - 1][i])
        matrix[i] = a
