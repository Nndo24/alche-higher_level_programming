#!/usr/bin/python3
"""
This module defines a matrix division function.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): Matrix containing integers or floats.
        div (int/float): Number to divide matrix elements by.

    Returns:
        list: A new matrix with results rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats.
        TypeError: If matrix rows are not all the same size.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for element in row:
            if not isinstance(element, (int, float)) or isinstance(element, bool):
                raise TypeError(msg)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
