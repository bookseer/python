#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Profile Time

Project: TryPython
A collection of educational materials for learning the Python

Author: Alexander Krasnikov aka askras
Website: trypython.pro

License: BSD 3 clause
"""

import functools
import timeit
import typing


def profile_time(
    *,
    number: int = 1,
    setup: str = 'pass',
    ndigits: int = 3,
    output: str = '[{elapsed:0.{ndigits}f}s] {func_name}({func_args}) -> {func_result}',
) -> typing.Callable:
    """Decorator for profiling the speed of the function (in seconds)

    Parameters
    ----------
    number : int, optional
        Number of code repetitions.
    setup : str, optional
        Code executed once before timing.
    ndigits : int, optional
        Number of decimal places in the returned value.
    output : str, optional
        The template of the displayed message

    Returns
    -------
    decorator: typing.Callable
        Decorator for profiling the time of the function in seconds.

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
    >>> def sleep_func(n):
    ...     time.sleep(n)
    ...     return n
    ...
    >>> profile_time_sleep_func = profile_time()(sleep_func)
    >>> profile_time_sleep_func(2)
    [2.000s] sleep_func(2) -> 2
    2
    >>> profile_time(number=5)(sleep_func)(4)
    [4.000s] sleep_func(4) -> 4
    4

    Profiling the running time of a function for different parameter values:

    >>> import time
    >>> def sleep_func(n):
    ...     time.sleep(n)
    ...     return n
    ...
    >>> output_format = 'The function {func_name}({func_args}) was executed for {elapsed:0.{ndigits}} seconds.'
    >>> for n in range(1,4):
    ...    profile_time_sleep_func = profile_time(number=2, output=output_format)(sleep_func)
    ...    profile_time_sleep_func(n)
    The function sleep_func(1) was executed for 1.0 seconds.
    1
    The function sleep_func(2) was executed for 2.0 seconds.
    2
    The function sleep_func(3) was executed for 3.0 seconds.
    3

    Using the `setup` option:

    >>> import time
    >>> def sleep_func(n):
    ...     time.sleep(n)
    ...     return n
    ...
    >>> setup = 'print("Start setup"); time.sleep(10); print("End setup")'
    >>> profile_time_sleep_func = profile_time(setup=setup)(sleep_func)
    >>> profile_time_sleep_func(3)
    Start setup
    End setup
    [3.000s] sleep_func(3) -> 3
    3

    Decoding the generated function:

    >>> import time
    >>> @profile_time(number=2, setup='print("Start");', ndigits=0)
    ... def sleep_func(n):
    ...    time.sleep(n)
    ...    return n
    ...
    >>> sleep_func(5)
    Start
    [5s] sleep_func(5) -> 5
    5
    """

    def decorator(func: typing.Callable) -> typing.Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> float:
            usage_time = timeit.timeit(
                lambda: func(*args, **kwargs),
                setup=setup,
                number=number,
            )
            elapsed = round(  # pylint: disable=possibly-unused-variable
                usage_time / number, ndigits
            )
            # get func's params as string
            position_args = [str(param) for param in args]
            named_args = [f'{str(k)}={str(v)}' for k, v in kwargs.items()]
            func_args = ', '.join(  # pylint: disable=possibly-unused-variable
                position_args + named_args
            )
            func_name = func.__name__  # pylint: disable=possibly-unused-variable
            func_return = func(*args, **kwargs)
            func_result = repr(func_return)  # pylint: disable=possibly-unused-variable
            print(output.format(**locals()))
            return func_return

        return wrapper

    return decorator


if __name__ == '__main__':
    import time

    def sleep_func(n):
        time.sleep(n)
        return n

    for i in range(1, 4):
        time_sleep_func = profile_time(number=3)(sleep_func)
        time_sleep_func(i)
