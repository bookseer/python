#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Syracuse Sequence. Recursive implementation.

Project: TryPython
A collection of educational materials for learning the Python

Author: Alexander Krasnikov aka askras
Website: trypython.pro

License: BSD 3 clause
"""


def get_syracuse_sequence_recursive(n: int) -> list[int]:
    """Syracuse_sequence. Recursive implementation.

    To explain the essence of the hypothesis, consider the following sequence
    of numbers, called the Syracuse sequence. We take any natural number n.
    1) If n is even, the next number n is n / 2.
    2) If n is odd, the next number n is n * 3 + 1.
    3) If n is 1, stop. Otherwise, repeat.
    It is generally thought, but so far not mathematically proven, that
    every starting number eventually terminates at 1.

    Parameters
    ----------
    n : int
        The first element of the Syracuse sequence.

    Returns
    -------
    syracuse_sequence : list[int]
        Syracuse sequence with the first element 'n'

    Notes
    -----
    Recursive implementation of the Syracuse sequence calculation.

    References
    ----------
    [1] Collatz Sequence : https://en.wikipedia.org/wiki/Collatz_conjecture

    Examples
    --------
    >>> get_syracuse_sequence_recursive(0)
    []

    >>> get_syracuse_sequence_recursive(1)
    [1]

    >>> get_syracuse_sequence_recursive(5)
    [5, 16, 8, 4, 2, 1]

    >>> get_syracuse_sequence_recursive(27) # doctest: +ELLIPSIS
    [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, ...

    >>> get_syracuse_sequence_recursive(150)
    [150, 75, 226, 113, 340, 170, 85, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    """
    if n < 1:
        return []
    elif n == 1:  # n is even
        return [1]
    elif n % 2 == 0:  # n is odd
        return [n] + get_syracuse_sequence_recursive(n // 2)
    else:
        return [n] + get_syracuse_sequence_recursive(3 * n + 1)


if __name__ == '__main__':
    import sys

    print('Examples of the Syracuse sequence.\n')

    print('Enter a starting number of the Syracuse sequence:')
    response = input('> ')

    if not response.isdecimal() or response == '0':
        print('You must enter an integer greater than 0.')
        sys.exit()

    starting_number = int(response)
    print(f'For n = {starting_number}, the Syracuse sequence has the form:')
    print(get_syracuse_sequence_recursive(starting_number))

    input('\nPress ENTER to exit...')
