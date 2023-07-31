#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Testing Bead Sort"""

from pytest import mark

from .bead_sort import bead_sort


@mark.parametrize(
    'unsorted_collection, sorted_collection',
    [
        ([4, 7, 2, 11, 1, 8, 0], [0, 1, 2, 4, 7, 8, 11]),
        ((4, 7, 2, 11, 1, 8, 0), [0, 1, 2, 4, 7, 8, 11]),
        ({4, 7, 2, 11, 1, 8, 0}, [0, 1, 2, 4, 7, 8, 11]),
    ],
)
def test_bubble_sort(unsorted_collection, sorted_collection):
    """Testing bead_sort"""
    expected = sorted_collection
    got = bead_sort(unsorted_collection)
    assert got == expected
