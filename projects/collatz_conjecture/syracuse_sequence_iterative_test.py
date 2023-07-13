#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Testing Syracuse Sequence Iterative"""

from syracuse_sequence_iterative import get_syracuse_sequence_iterative


def test_get_syracuse_sequence_iterative():
    """Testing Syracuse Sequence Iterative"""
    assert not get_syracuse_sequence_iterative(0)

    assert get_syracuse_sequence_iterative(1) == [1]

    assert get_syracuse_sequence_iterative(5) == [5, 16, 8, 4, 2, 1]

    assert get_syracuse_sequence_iterative(150) == [
        150,
        75,
        226,
        113,
        340,
        170,
        85,
        256,
        128,
        64,
        32,
        16,
        8,
        4,
        2,
        1,
    ]
