#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Testing Syracuse Sequence Recursive"""

from syracuse_sequence_recursive import get_syracuse_sequence_recursive


def test_get_syracuse_sequence_recursive():
    """Testing Syracuse Sequence Recursive"""
    assert get_syracuse_sequence_recursive(0) == []

    assert get_syracuse_sequence_recursive(1) == [1]

    assert get_syracuse_sequence_recursive(5) == [5, 16, 8, 4, 2, 1]

    assert get_syracuse_sequence_recursive(150) == [
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
