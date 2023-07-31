#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Bead Sort

Project: TryPython
A collection of educational materials for learning the Python

Author: Alexander Krasnikov aka askras
Website: trypython.pro

License: BSD 3 clause
"""

from collections.abc import Collection


def bead_sort(unsorted_collection: Collection[int], /) -> list[int]:
    """Pure implementation of bead sort algorithm in Python

    Parameters
    ----------
    unsorted_collection : Collection[int]
        Some ordered collection with non-negativ integer items inside.

    Returns
    -------
    list(int)
         A new list containing all items from the `collection` in ascending order.

    Raises
    ------
    TypeError
        If `colection` contains non-integer or negative numbers

    Notes
    -----
    Bead sort only works for sequences of non-negative integers.

    References
    ----------
    [1] Bead Sort : https://en.wikipedia.org/wiki/Bead_sort

    Examples
    --------
    >>> bead_sort([4, 3, 8, 2, 7, 1, 9, 5, 0, 6])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> bead_sort([4, 2, 3, 1, 5]) == sorted([4, 2, 3, 1, 5])
    True
    >>> bead_sort([]) == sorted([])
    True
    >>> bead_sort([4, 7, 2, 11, 1, 7, 0]) == sorted([4, 7, 2, 11, 1, 7, 0])
    True
    >>> bead_sort([-2, 10, 16, -3, -11]) == sorted([-2, 10, 16, -3, -11])
    True
    >>> import random
    >>> random_collection = random.sample(range(0, 100), 100)
    >>> bead_sort(random_collection) == sorted(random_collection)
    True
    >>> bead_sort(time_zones)  #  bead_sort is an unstable sort
    [(1, 'London'), (2, 'Berlin'), (2, 'Paris'), (3, 'Minsk'), (3, 'Moscow')]
    >>> bead_sort([1, .9, 0.0, 0, -1, -.9])
    Traceback (most recent call last):
        ...
    TypeError: Sequence must be list of non-negative integers
    >>> bead_sort("Hello world")
    Traceback (most recent call last):
        ...
    TypeError: Sequence must be list of non-negative integers
    """

    collection: list[int] = list(unsorted_collection)

    if any(not isinstance(item, int) or item < 0 for item in collection):
        raise TypeError('Input collection must be list of non-negative integers')
    for _ in range(len(collection)):
        for i, (rod_upper, rod_lower) in enumerate(zip(collection, collection[1:])):
            if rod_upper > rod_lower:
                collection[i] -= rod_upper - rod_lower
                collection[i + 1] += rod_upper - rod_lower
    return collection


if __name__ == '__main__':
    user_input = input('Enter numbers separated by a comma:').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(*bead_sort(unsorted), sep=', ')
