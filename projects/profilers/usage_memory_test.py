#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Testing Usage Memory"""

from usage_memory import get_usage_memory


def sum_big_list(num: int) -> int:
    big_list = [2] * (num * 10**7)
    return sum(big_list)


def test_get_usage_memory():
    """Testing get_usage_memory"""
    get_usage_memory_sum_big_list = get_usage_memory(ndigits=0)(sum_big_list)
    assert 151 < get_usage_memory_sum_big_list(2) < 154
