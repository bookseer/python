#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Quadratic Equations

Project: TryPython
A collection of educational materials for learning the Python

Author: Alexander Krasnikov aka askras
Website: trypython.pro

License: BSD 3 clause
"""

import cmath
import math


def quadratic_equation(
    a: float, b: float, c: float
) -> tuple[float | complex, float | complex]:
    """Solving the quadratic equation ax^2+bx+c=0.

    In algebra, a quadratic equation (from Latin quadratus 'square') is an
    equation that can be arranged in standard form as ax^2 + bx + c = 0,
    where x represents an unknown value, and a, b, and c represent known
    numbers, where a ≠ 0. (If a = 0 and b ≠ 0 then the equation is linear,
    not quadratic.) The numbers a, b, and c are the coefficients of the
    equation and may be distinguished by respectively calling them, the
    quadratic coefficient, the linear coefficient and the constant
    coefficient or free term.

    Parameters
    ----------
    a : float
        The the quadratic coefficient of the quadratic equation.
    b : float
        The linear coefficient of the quadratic equation.
    c : float
        Free term of the quadratic equation

    Returns
    -------
    (x_1, x_2) : tuple[float, complex]
        Roots of the quadratic equation

    See Also
    --------
    numpy.roots
        Return the roots of a polynomial with coefficients given in p.

    Notes
    -----
    No distinction is made here between real and complex solutions of
    quadratic equations.

    References
    ----------
    [1] Quadratic equation : https://en.wikipedia.org/wiki/Quadratic_equation

    Examples
    --------
    The case of two real roots:

    >>> quadratic_equation(1, -1, -6)
    (-2.0, 3.0)

    The case of two equal real roots:

    >>> quadratic_equation(2, -8, 8)
    (2.0, 2.0)

    The case of two complex roots:

    >>> quadratic_equation(1, 2, 10)
    ((-1-3j), (-1+3j))
    """

    discriminant = b**2 - 4 * a * c
    # Depending on the sign of the discriminant, we get a real or complex root

    sqrt_discriminant = (
        math.sqrt(discriminant) if discriminant >= 0 else cmath.sqrt(discriminant)
    )

    x_1 = (-b - sqrt_discriminant) / (2 * a)
    x_2 = (-b + sqrt_discriminant) / (2 * a)

    return x_1, x_2


if __name__ == "__main__":
    print("Various cases that arise when solving quadratic equations.", end="\n\n")

    print("1. Equation x^2 + 2x + 10 = 0 has two real roots:")
    x1, x2 = quadratic_equation(1, -1, -6)
    print(f"x1 = {x1}, x2 = {x2}", end="\n\n")

    print("2. Equation 2x^2 - 8x + 8 = 0 has two equal real roots:")
    x1, x2 = quadratic_equation(2, -8, 8)
    print(f"x1 = {x1}, x2 = {x2}", end="\n\n")

    print("3. Equation x^2 + 2x + 10 = 0 has two complex roots:")
    x1, x2 = quadratic_equation(1, 2, 10)
    print(f"x1 = {x1}, x2 = {x2}", end="\n\n")
