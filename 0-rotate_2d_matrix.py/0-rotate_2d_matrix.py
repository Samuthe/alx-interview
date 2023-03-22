#!/usr/bin/python3

'''rotate matrix 90 degrees
'''


def rotate_2d_matrix(matrix):
    '''given n x n, rotate 2D matrix 90 degrees clockwise
    '''
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        for j in range(n // 2):
            temp = matrix[i][j]
            matrix[j][i] = matrix[i][n - 1 - j]
            matrix[n - i - j] = temp
