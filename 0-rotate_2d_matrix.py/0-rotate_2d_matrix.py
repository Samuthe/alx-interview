#!/usr/bin/python3
"""
Module 0-rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise
    """
    N = len(matrix)

    for i in range(N):
        for j in range(i, N):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(N):
        for j in range(N // 2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][N - 1 - j]
            matrix[i][N - 1 - j] = temp


# '''rotate matrix 90 degrees
# '''


# def rotate_2d_matrix(matrix):
#     '''given n x n, rotate 2D matrix 90 degrees clockwise
#     '''
#     n = len(matrix)

#     for i in range(n):
#         for j in range(i, n):
#             temp = matrix[i][j]
#             matrix[i][j] = matrix[j][i]
#             matrix[j][i] = temp

#     for i in range(n):
#         for j in range(n // 2):
#             temp = matrix[i][j]
#             matrix[j][i] = matrix[i][n - 1 - j]
#             matrix[n - i - j] = temp
