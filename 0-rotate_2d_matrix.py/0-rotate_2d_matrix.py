#!/usr/bin/python3

'''rotate matrix 90 degrees'''

'''func to 2D array'''


def rotate_2d_matrix(matrix):
    '''declare empty arr'''
    rotateArr = []
    '''a var to store the length of my array'''
    lengthOfArr = len(matrix)

    '''iterate thro' my array and add the new array to var rotateArr'''
    for i in range(lengthOfArr):
        rotateArr.append([])

    for i in range(lengthOfArr):
        for j in range(lengthOfArr):
            rotateArr[i].insert(0, matrix[j].pop(0))
    # return rotateArr


# newArr = rotate_2d_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# for i in newArr:
#     print(i)
