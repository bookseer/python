#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Testing Bubble Sort"""

from .bubble_sort import bubble_sort
from pytest import mark


@mark.parametrize(
    'iterable, expected',
    [
        ([4, 7, 2, 11, 1, 8, 0], [0, 1, 2, 4, 7, 8, 11]),
        ((4, 7, 2, 11, 1, 8, 0), [0, 1, 2, 4, 7, 8, 11]),
        ({4, 7, 2, 11, 1, 8, 0}, [0, 1, 2, 4, 7, 8, 11]),
        ({'a', 'y', 'k', 'f', 'x'}, ['a', 'f', 'k', 'x', 'y']),
        (list('hello'), ['e', 'h', 'l', 'l', 'o']),
        (
            {'one': 1, 'three': 3, 'two': 2, 'five': 5, 'four': 4},
            ['five', 'four', 'one', 'three', 'two'],
        ),
        (
            [('bob', '1', 17), ('carroll', '3', 19), ('alice', '2', 18)],
            [('alice', '2', 18), ('bob', '1', 17), ('carroll', '3', 19)],
        ),
        (
            [(3, 'Moscow'), (2, 'Berlin'), (1, 'London'), (2, 'Paris'), (3, 'Minsk')],
            [(1, 'London'), (2, 'Berlin'), (2, 'Paris'), (3, 'Minsk'), (3, 'Moscow')],
        ),
    ],
)
def test_bubble_sort(iterable, expected):
    """Testing bubble_sort"""
    got = bubble_sort(iterable)
    assert got == expected
