#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Usage Memory

Project: TryPython
A collection of educational materials for learning the Python

Author: Alexander Krasnikov aka askras
Website: trypython.pro

License: BSD 3 clause
"""

import functools
import memory_profiler  # type: ignore
import typing


def get_usage_memory(
    *, interval: float = 0.1, timeout: float = 0.1, ndigits: int = 3
) -> typing.Callable:
    """Decorator for measuring the memory used by the code in Mebibytes (MiB)

    Подробное описание

    Parameters
    ----------
    interval : float, optional
        Interval at which measurements are collected.
    timeout : float, optional
        Maximum amount of time (in seconds) to wait before returning.
    ndigits : int, optional
        Number of decimal places in the returned value.

    Returns
    -------
    decorator: typing.Callable
        Decorator to measure the memory used by a function

    See Also
    --------
    memory-profiler
        A python module for monitoring memory consumption of a process as well
        as line-by-line analysis of memory consumption for python programs.

    References
    ----------
    [1] memory-profiler documentation : https://pypi.org/project/memory-profiler/

    Examples
    --------
    Decorating an existing function:

    >>> import time
    >>> def f(n):
    ...    time.sleep(1)
    ...    L = [2] * (n * 10 ** 7)
    ...    time.sleep(n)
    ...    return L
    ...
    >>> f1 = get_usage_memory(ndigits=0)(f)
    >>> print(f1(3))
    229.0
    >>> get_usage_memory(ndigits=0)(f)(4)
    305.0

    Decorating a function with parameters:

    >>> import time
    >>> def f(n):
    ...    time.sleep(1)
    ...    L = [2] * (n * 10 ** 7)
    ...    time.sleep(n)
    ...    return L
    ...
    >>> for n in range(1,4):
    ...    f2 = get_usage_memory(ndigits=0)(f)
    ...    print(f"The function uses {f2(n)} MiB")
    The function uses 76.0 MiB
    The function uses 152.0 MiB
    The function uses 229.0 MiB

    Decoding the generated function:

    """

    def decorator(func: typing.Callable) -> typing.Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> typing.Callable:
            usage_memory = memory_profiler.memory_usage(
                (func, args, kwargs), interval=interval, timeout=timeout
            )
            return round(max(usage_memory) - usage_memory[0], ndigits)

        return wrapper

    return decorator


if __name__ == '__main__':

    def sum_big_list(num: int) -> int:
        big_list = [2] * (num * 10**7)
        return sum(big_list)

    for i in range(1, 4):
        get_memory = get_usage_memory(ndigits=0)(sum_big_list)
        print(f'The function uses {get_memory(i)} MiB')
