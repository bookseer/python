#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Testing Profile Time"""

import time

from profile_time import profile_time


def sleep_func(n):
    """Function for test"""
    time.sleep(n)
    return n

def test_profile_time():
    """Testing get_usage_time"""
    profile_time_sleep_func = profile_time()(sleep_func)
    assert profile_time_sleep_func(2) == 2
