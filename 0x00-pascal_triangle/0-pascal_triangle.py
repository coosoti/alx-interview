#!/usr/bin/python3
""" This function returns a representation of a Pascal's
    triangle builf from list of lists of integer values
"""


def pascal_triangle(n):
    """returns a list of lists representing Pascal's triangle"""
    p_list = []
    if (n <= 0):
        return p_list
    p_list.append([1])
    for i in range(n -1): # n is number of rows
        p_list.append([1] + [p_list[i][j] + p_list[i][j + 1]
                    for j in range(len(p_list[i]) - 1)] + [1])
    return p_list
