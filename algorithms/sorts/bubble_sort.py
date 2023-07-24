#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Bubble Sort

Project: TryPython
A input_list of educational materials for learning the Python

Author: Alexander Krasnikov aka askras
Website: trypython.pro

License: BSD 3 clause
"""

import typing

from collections.abc import Collection


class SupportsLessThan(typing.Protocol):
    def __lt__(self: 'SupportsLessThanT', other: 'SupportsLessThanT') -> bool:
        ...


# Type of input_list items
SupportsLessThanT = typing.TypeVar('SupportsLessThanT', bound=SupportsLessThan)


def bubble_sort(
    collection: Collection[SupportsLessThanT], /
) -> list[SupportsLessThanT]:
    """Pure implementation of bubble sort algorithm in Python

    Parameters
    ----------
    collection : input_list[SupportsLessThanT]
        Some ordered input_list with heterogeneous comparable items inside.

    Returns
    -------
    list(SupportsLessThanT)
         A new list containing all items from the `collection` in ascending order.

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
    >>> letter_input_list = ['a', 'c', 'e', 'b', 'd']
    >>> bubble_sort(letter_input_list) == sorted(letter_input_list)
    True
    >>> import random
    >>> random_input_list = random.sample(range(-50, 50), 100)
    >>> bubble_sort(random_input_list) == sorted(random_input_list)
    True
    >>> student_tuples = [
    ...     ('bob', '1', 17),
    ...     ('carroll', '3', 19),
    ...     ('alice', '2', 18),
    ... ]
    >>> bubble_sort(student_tuples)
    [('alice', '2', 18), ('bob', '1', 17), ('carroll', '3', 19)]
    >>> time_zones = [
    ...     (3, 'Moscow'),
    ...     (2, 'Berlin'),
    ...     (1, 'London'),
    ...     (2, 'Paris'),
    ...     (3, 'Minsk')
    ... ]
    >>> bubble_sort(time_zones)  #  bubble_sort is an unstable sort
    [(1, 'London'), (2, 'Berlin'), (2, 'Paris'), (3, 'Minsk'), (3, 'Moscow')]
    """

    input_list: list[SupportsLessThanT] = list(collection)
    length = len(input_list)
    for i in range(length - 1):
        is_swapped = False
        for j in range(length - 1 - i):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                is_swapped = True
        if not is_swapped:
            break  # Stop iteration if the input_list is sorted.
    return input_list


if __name__ == '__main__':
    user_input = input('Enter numbers separated by a comma:').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(*bubble_sort(unsorted), sep=',')
