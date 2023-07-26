#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Testing Usage Time"""

import time

from usage_time import get_usage_time


def sleep_func(n):
    """Function for test"""
    time.sleep(n)
    return n


def test_get_usage_time():
    """Testing get_usage_time"""
    get_usage_time_sleep_func = get_usage_time(ndigits=1)(sleep_func)
    assert get_usage_time_sleep_func(2) == 2.0
