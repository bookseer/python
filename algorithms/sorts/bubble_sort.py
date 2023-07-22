#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Bubble Sort

Project: TryPython
A collection of educational materials for learning the Python

Author: Alexander Krasnikov aka askras
Website: trypython.pro

License: BSD 3 clause
"""

import typing

from collections.abc import Collection


class SupportsLessThan(typing.Protocol):
    def __lt__(self: 'SupportsLessThanT', other: 'SupportsLessThanT') -> bool:
        ...


# Type of collection items
SupportsLessThanT = typing.TypeVar('SupportsLessThanT', bound=SupportsLessThan)


def bubble_sort(iterable: Collection[SupportsLessThanT], /) -> list[SupportsLessThanT]:
    """Pure implementation of bubble sort algorithm in Python

    Parameters
    ----------
    iterable : Collection[SupportsLessThanT]
        Some ordered collection with heterogeneous comparable items inside.

    Returns
    -------
    list(SupportsLessThanT)
         A new list containing all items from the `iterable` in ascending order.

    References
    ----------
    [1] Bubble Sort : https://en.wikipedia.org/wiki/Bubble_sort

    Examples
    --------
    >>> bubble_sort([4, 3, 8, 2, 7, 1, 9, 5, 0, 6])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> bubble_sort([4, 2, 3, 1, 5]) == sorted([4, 2, 3, 1, 5])
    True
    >>> bubble_sort([]) == sorted([])
    True
    >>> bubble_sort([4, 7, 2, 11, 1, 7, 0]) == sorted([4, 7, 2, 11, 1, 7, 0])
    True
    >>> bubble_sort([-2, 10, 16, -3, -11]) == sorted([-2, 10, 16, -3, -11])
    True
    >>> letter_collection = ['a', 'c', 'e', 'b', 'd']
    >>> bubble_sort(letter_collection) == sorted(letter_collection)
    True
    >>> import random
    >>> random_collection = random.sample(range(-50, 50), 100)
    >>> bubble_sort(random_collection) == sorted(random_collection)
    True
    >>> student_tuples = [
    ...     ('bob', '1', 17),
    ...     ('carroll', '3', 19),
    ...     ('alice', '2', 18),
    ... ]
    >>> bubble_sort(student_tuples)
    [('alice', '2', 18), ('bob', '1', 17), ('carroll', '3', 19)]
    """

    collection: list[SupportsLessThanT] = list(iterable)
    length = len(collection)
    for i in range(length - 1):
        is_swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
                is_swapped = True
        if not is_swapped:
            break  # Stop iteration if the collection is sorted.
    return collection


if __name__ == '__main__':
    user_input = input('Enter numbers separated by a comma:').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(*bubble_sort(unsorted), sep=',')
