#!/usr/bin/python3
"""Module for matrix_divided.

Defines the function matrix_divided(matrix, div), which divides
all elements of a matrix (list of lists of integers/floats) by
a number and returns a new matrix with the results rounded to
2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.

    Args:
        matrix: list of lists of integers or floats.
        div: number (int or float) used as divisor.
    Returns:
        A new matrix with all values divided by div,
        each rounded to 2 decimal places.
    Raises:
        TypeError: If matrix is not a matrix (list of lists)
                   of integers/floats, if rows have different
                   sizes, or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    msg_matrix = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(msg_matrix)

    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(msg_matrix)

    for row in matrix:
        for num in row:

            if isinstance(num, bool) or not isinstance(num, (int, float)):
                raise TypeError(msg_matrix)

    first_len = len(matrix[0])
    for row in matrix:
        if len(row) != first_len:
            raise TypeError("Each row of the matrix must have the same size")

    if isinstance(div, bool) or not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            result = num / div
            result = round(result, 2)
            new_row.append(result)
        new_matrix.append(new_row)

    return new_matrix
