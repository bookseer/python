#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Syracuse Sequence. Iterative implementation.

Project: TryPython
A collection of educational materials for learning the Python

Author: Alexander Krasnikov aka askras
Website: trypython.pro

License: BSD 3 clause
"""


def get_syracuse_sequence_iterative(n: int) -> list[int]:
    """Syracuse_sequence. Iterative implementation.

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
    Iterative implementation of the Syracuse sequence calculation.

    References
    ----------
    [1] Collatz Sequence : https://en.wikipedia.org/wiki/Collatz_conjecture

    Examples
    --------
    >>> get_syracuse_sequence_iterative(0)
    []

    >>> get_syracuse_sequence_iterative(1)
    [1]

    >>> get_syracuse_sequence_iterative(5)
    [5, 16, 8, 4, 2, 1]

    >>> get_syracuse_sequence_iterative(27) # doctest: +ELLIPSIS
    [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, ...

    >>> get_syracuse_sequence_iterative(150)
    [150, 75, 226, 113, 340, 170, 85, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    """

    if n < 1:
        return []

    syracuse_sequence = [n]
    while n != 1:
        if n % 2 == 0:  # n is even
            n = n // 2
        else:  # n is odd
            n = 3 * n + 1
        syracuse_sequence.append(n)
    return syracuse_sequence


if __name__ == '__main__':
    print('Examples of the Syracuse sequence.', end='\n\n')

    test_n = 0
    print(f'For n = {test_n}, the Syracuse sequence has the form:')
    print(get_syracuse_sequence_iterative(test_n), end='\n\n')

    test_n = 1
    print(f'For n = {test_n}, the Syracuse sequence has the form:')
    print(get_syracuse_sequence_iterative(test_n), end='\n\n')

    test_n = 5
    print(f'For n = {test_n}, the Syracuse sequence has the form:')
    print(get_syracuse_sequence_iterative(test_n), end='\n\n')

    test_n = 27
    print(f'For n = {test_n}, the Syracuse sequence has the form:')
    print(get_syracuse_sequence_iterative(test_n), end='\n\n')

    test_n = 150
    print(f'For n = {test_n}, the Syracuse sequence has the form:')
    print(get_syracuse_sequence_iterative(test_n), end='\n\n')