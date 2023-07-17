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

### Гипотеза Коллатца (3n+1 дилемма, сиракузская проблема)


Для объяснения сути гипотезы рассмотрим следующую последовательность чисел, называемую **сиракузской последовательностью**.

Берём любое натуральное число $n$. Если оно чётное, то делим его на 2, а если нечётное, то умножаем на 3 и прибавляем 1 (получаем 3n + 1).
Над полученным числом выполняем те же самые действия, и так далее.

Приведем две реализации вычисления сиракузской последовательнсти: итеративную и рекурсивную.

```python
# %load -y -n -s get_syracuse_sequence_iterative syracuse_sequence_iterative.py
def get_syracuse_sequence_iterative(n: int) -> list[int]:
    """Syracuse_sequence. Iterative implementation.

    To explain the essence of the hypothesis, consider the following sequence
    of numbers, called the Syracuse sequence. We take any natural number n.
    1) If n is even, the next number n is n / 2.
    2) If n is odd, the next number n is n * 3 + 1.
    3) If n is 1, stop. Otherwise, repeat.
    It is generally thought, but so far not mathematically proven, that
    every starting number eventually terminates at 1.

    Parameters
    ----------
    n : int
        The first element of the Syracuse sequence.

    Returns
    -------
    syracuse_sequence : list[int]
        Syracuse sequence with the first element 'n'

    Notes
    -----
    Iterative implementation of the Syracuse sequence calculation.

    References
    ----------
    [1] Collatz Sequence : https://en.wikipedia.org/wiki/Collatz_conjecture

    Examples
    --------
    >>> get_syracuse_sequence_iterative(0)
    []

    >>> get_syracuse_sequence_iterative(1)
    [1]

    >>> get_syracuse_sequence_iterative(5)
    [5, 16, 8, 4, 2, 1]

    >>> get_syracuse_sequence_iterative(27) # doctest: +ELLIPSIS
    [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, ...

    >>> get_syracuse_sequence_iterative(150)
    [150, 75, 226, 113, 340, 170, 85, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    """

    if n < 1:
        return []

    syracuse_sequence = [n]
    while n != 1:
        if n % 2 == 0:  # n is even
            n = n // 2
        else:  # n is odd
            n = 3 * n + 1
        syracuse_sequence.append(n)
    return syracuse_sequence

```

```python
# %load -y -n -s get_syracuse_sequence_recursive syracuse_sequence_recursive.py
def get_syracuse_sequence_recursive(n: int) -> list[int]:
    """Syracuse_sequence. Recursive implementation.

    To explain the essence of the hypothesis, consider the following sequence
    of numbers, called the Syracuse sequence. We take any natural number n.
    1) If n is even, the next number n is n / 2.
    2) If n is odd, the next number n is n * 3 + 1.
    3) If n is 1, stop. Otherwise, repeat.
    It is generally thought, but so far not mathematically proven, that
    every starting number eventually terminates at 1.

    Parameters
    ----------
    n : int
        The first element of the Syracuse sequence.

    Returns
    -------
    syracuse_sequence : list[int]
        Syracuse sequence with the first element 'n'

    Notes
    -----
    Recursive implementation of the Syracuse sequence calculation.

    References
    ----------
    [1] Collatz Sequence : https://en.wikipedia.org/wiki/Collatz_conjecture

    Examples
    --------
    >>> get_syracuse_sequence_recursive(0)
    []

    >>> get_syracuse_sequence_recursive(1)
    [1]

    >>> get_syracuse_sequence_recursive(5)
    [5, 16, 8, 4, 2, 1]

    >>> get_syracuse_sequence_recursive(27) # doctest: +ELLIPSIS
    [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, ...

    >>> get_syracuse_sequence_recursive(150)
    [150, 75, 226, 113, 340, 170, 85, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    """
    if n < 1:
        return []
    elif n == 1:  # n is even
        return [1]
    elif n % 2 == 0:  # n is odd
        return [n] + get_syracuse_sequence_recursive(n // 2)
    else:
        return [n] + get_syracuse_sequence_recursive(3 * n + 1)

```

**Гипотеза Коллатца** заключается в том, что с какого бы числа $n$ мы не начали строить сиракузскую последовательность, рано или поздно мы получим единицу.

Заметим, что гипотеза Коллатца является одной из нерешенных задач математики.

```python
import time

from syracuse_sequence_iterative import (
    get_syracuse_sequence_iterative as get_syracuse_sequence,
)

starting_number = 27

print(f'For n = {starting_number}, the Syracuse sequence has the form:')
syracuse_sequence = get_syracuse_sequence(starting_number)
for item in syracuse_sequence[:-1]:
    print(str(item) + ',', end=' ', flush=True)
    time.sleep(0.10)
print(syracuse_sequence[-1], end='\n\n')

```

```python
import time

from syracuse_sequence_recursive import (
    get_syracuse_sequence_recursive as get_syracuse_sequence,
)

starting_number = 27

print(f'For n = {starting_number}, the Syracuse sequence has the form:')
syracuse_sequence = get_syracuse_sequence(starting_number)
for item in syracuse_sequence[:-1]:
    print(str(item) + ',', end=' ', flush=True)
    time.sleep(0.10)
print(syracuse_sequence[-1], end='\n\n')
```

#### Исследование программы
Попробуйте найти ответы на следующие вопросы.
Поэкспериментируйте с изменениями кода и запустите программу снова, чтобы увидеть, как они повлияют на ее работу.


1. Сколько членов содержит сиракузская последовательность, начинающаяся с 13?

2. Сколько членов содержит последовательность Коллатца, начинающаяся с 76?

3. Всегда ли последовательности Коллатца, начальные члены которых являются степенями двойки (2, 4, 8, 16, 32, 64, 128 и т. д.), состоят только из четных чисел (не считая конечного числа 1)?

4. Найдите какому числу от 1 до 1000 соответсвует самая длинная сиракузская последовательость.


#### Ссылки

https://ru.wikipedia.org/wiki/Гипотеза_Коллатца

https://ru.wikipedia.org/wiki/Открытые_математические_проблемы
