---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.7
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

### Usage Time: Измерение используемой функцией памяти


Важным критерием оценки алгоритмов является потребляемая ими память.
Чтобы оценить потребляемой памяти, вы можете использовать приведенный здесь декоратор.

```python
# %load -y -n -r 14:17 usage_memory.py
import functools
import memory_profiler  # type: ignore
import typing
```

```python
# %load -y -n -s get_usage_memory usage_memory.py
def get_usage_memory(
    *, interval: float = 0.1, timeout: float = 0.1, ndigits: int = 3
) -> typing.Callable:
    """Decorator for measuring the memory used by the code in Mebibytes (MiB)

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
```

#### Пример использования

```python
def sum_big_list(num: int) -> int:
    big_list = [2] * (num * 10**7)
    return sum(big_list)
```

```python
for i in range(1, 9):
    get_memory = get_usage_memory(ndigits=3)(sum_big_list)
    print(f'The function uses {get_memory(i)} MiB')
```

```python
import matplotlib.pyplot as plt

%matplotlib inline

get_memory = get_usage_memory(ndigits=3)(sum_big_list)

items = range(1, 9)  # multiply by 10**7
memory = [get_memory(i) for i in items]

fig = plt.plot(items, memory, 'bo-')
plt.title('The amount of memory used')
ax = plt.gca()
ax.set_xlabel(f'Number of elements, $n\cdot10^7$ pieces')
ax.set_ylabel('Memory, MiB')
plt.show()
```

Исследование программы

Попробуйте найти ответы на следующие вопросы. Поэкспериментируйте с изменениями кода и запустите программу снова, чтобы увидеть, как они повлияют на ее работу.


1. Модифицируйте декоратор для того чтобы получать значение потребляемой памяти в кибибайтах.


#### Ссылки

1. Документация memory-profiler: https://pypi.org/project/memory-profiler/
