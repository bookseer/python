#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Testing Quadratic Equations"""

from quadratic_equation import quadratic_equation


def test_quadratic_equation_witw_two_real_roots():
    """Testing quadratic_equation: The case of two real roots"""
    assert (-2.0, 3.0) == quadratic_equation(1, -1, -6)


def test_quadratic_equation_witw_two_equal_real_roots():
    """Testing quadratic_equation: The case of two equal real roots"""
    assert (2.0, 2.0) == quadratic_equation(2, -8, 8)


def test_quadratic_equation_witw_two_complex_roots():
    """Testing quadratic_equation: The case of two complex roots"""
    assert ((-1 - 3j), (-1 + 3j)) == quadratic_equation(1, 2, 10)
