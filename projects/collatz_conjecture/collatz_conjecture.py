#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Collatz Conjecture or the (3n + 1) Problem
"""

import time

from syracuse_sequence_iterative import get_syracuse_sequence_iterative as get_syracuse_sequence


def main():
    while True:
        print('Enter a starting number greater than 0 or QUIT:')
        response = input('> ') or 'QUIT'

        if response == 'QUIT':
            input('Press ENTER to exit')
            break
        elif not response.isdecimal() or response == '0':
            print('You must enter an integer greater than 0.')
            continue
        else:
            response_n = int(response)

        print(f'For n = {response_n}, the Syracuse sequence has the form:')
        syracuse_sequence = get_syracuse_sequence(response_n)
        for item in syracuse_sequence[:-1]:
            print(str(item) + ',', end=' ', flush=True)
            time.sleep(0.1)
        print(syracuse_sequence[-1], end='\n\n')


if __name__ == '__main__':

    annotation = '''\
To explain the essence of the hypothesis, consider the following
sequence of numbers, called the Syracuse sequence.
We take any natural number n.
    1) If n is even, the next number n is n / 2.
    2) If n is odd, the next number n is n * 3 + 1.
    3) If n is 1, stop. Otherwise, repeat.

It is generally thought, but so far not mathematically proven, that
every starting number eventually terminates at 1.

'''

    print(annotation)
    main()
