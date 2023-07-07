#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Usage Time

Project: TryPython
A collection of educational materials for learning the Python

Author: Alexander Krasnikov aka askras
Website: trypython.pro

License: BSD 3 clause
"""

import functools
import timeit
import typing


def get_usage_time(number: int = 1,
                   setup: str = "pass",
                   ndigits: int = 3) -> typing.Callable:
    """Decorator for measuring the speed of the function (in seconds)q

    Parameters
    ----------
    number : int, default=1
        Number of code repetitions.
    setup : str, default="pass"
        Code executed once before timing.
    ndigits : int, default=3
        Number of decimal places in the returned value.

    Returns
    -------
    decorator: typing.Callable
        Decorator for measuring the time of the function in seconds.

    See Also
    --------
    timeit
        Measure execution time of small code snippets.

    References
    ----------
    [1] timeit documentation : https://docs.python.org/3/library/timeit.html

    Examples
    --------
    Decorating an existing function:

    >>> import time
    >>> def f(n):
    ...     time.sleep(n)
    ...     return n
    ...
    >>> f1 = get_usage_time()(f)
    >>> print(f"The function was executed for {f1(2)} seconds")
    The function was executed for 2.0 seconds
    >>> get_usage_time()(f)(4)
    4.0

    Measuring the running time of a function for different parameter values:

    >>> import time
    >>> def f(n):
    ...     time.sleep(n)
    ...     return n
    ...
    >>> for n in range(1,4):
    ...    f2 = get_usage_time(number=2)(f)
    ...    print(f2(n))
    1.0
    2.0
    3.0

    Using the `setup` option:

    >>> import time
    >>> def f(n):
    ...     time.sleep(n)
    ...     return n
    ...
    >>> number = 5
    >>> setup = "print('Start setup'); time.sleep(10); print('End setup')"
    >>> f3 =  get_usage_time(number=number, setup=setup)(f)
    >>> print(f3(3))
    Start setup
    End setup
    3.0

    Decoding the generated function:

    >>> import time
    >>> @get_usage_time(number=2, setup="print('Start');", ndigits=0)
    ... def f(n):
    ...    time.sleep(n)
    ...    return n
    ...
    >>> t = f(3)
    Start
    >>> print(t)
    3.0
    """

    def decorator(func: typing.Callable) -> typing.Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> float:
            usage_time = timeit.timeit(
                lambda: func(*args, **kwargs),
                setup=setup,  # code to be executed once at the beginning of the experiment
                number=number,  # number of repetitions
            )
            return round(usage_time / number, ndigits)
        return wrapper
    return decorator


if __name__ == "__main__":
    import time

    def f(n):
        time.sleep(n)
        return n

    for i in range(1, 4):
        f1 = get_usage_time(number=3)(f)
        print(f1(i))
