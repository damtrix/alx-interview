#!/usr/bin/python3
    
def rotate_2d_matrix(matrix):
    new_matrix = matrix.copy()
    
    for i in range(len(new_matrix)):
        a = []
        for j in range(len(new_matrix) , 0, -1):
            a.append(new_matrix[j - 1][i])
        matrix[i] = a
