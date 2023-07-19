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

### Квадратное уравнение


Квадратное уравнение — алгебраическое уравнение второй степени имеющие вид $a x^2 + b x + c = 0$, в котором
$x$ --- неизвестное, а коэффициенты $a$, $b$, $c$ вещественные или комплексные числа, причем $a\neq 0$.

Для решения квадратного уравнения необходимо вычислить его дискриминант $D = b^2 - 4 a c$.
Далее корни могут быть получены по формулам:

$$x_{1}=\frac{-b-\sqrt{D}}{2a}, \;\; x_{2}=\frac{-b+\sqrt{D}}{2a}.$$

В зависимости от знака дискриминанта, возникают три возможных случая.

|Условие |$D > 0$ |$D = 0$ |$D < 0$ |
|:---:|:---:|:---:|:---:|
|Количество корней |Два действительных корня |Один действительный корень кратности 2 (два одинаковых корня)| Два комплексных корня|

Заметим, что приведенный метод решения является универсальным, но не единственным.

```python
# %load -y -n -r 14:16 quadratic_equation.py
import cmath
import math
```

```python
# %load -y -n -s quadratic_equation quadratic_equation.py
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
    if discriminant < 0:
        sqrt_discriminant = cmath.sqrt(discriminant)
    else:
        sqrt_discriminant = math.sqrt(discriminant)

    x_1 = (-b - sqrt_discriminant) / (2 * a)
    x_2 = (-b + sqrt_discriminant) / (2 * a)

    return x_1, x_2
```

```python
print('1. Equation x^2 - x - 6 = 0 has two real roots:')
x1, x2 = quadratic_equation(1, -1, -6)
print(f'x1 = {x1}, x2 = {x2}', end='\n\n')

print('2. Equation 2x^2 - 8x + 8 = 0 has two equal real roots:')
x1, x2 = quadratic_equation(2, -8, 8)
print(f'x1 = {x1}, x2 = {x2}', end='\n\n')

print('3. Equation x^2 + 2x + 10 = 0 has two complex roots:')
x1, x2 = quadratic_equation(1, 2, 10)
print(f'x1 = {x1}, x2 = {x2}', end='\n\n')
```

#### Исследование программы
Попробуйте найти ответы на следующие вопросы.
Поэкспериментируйте с изменениями кода и запустите программу снова, чтобы увидеть, как они повлияют на ее работу.


1. Что произойдет если коэффициент $a$ все-таки будет равен 0?

2. Как модифицировать программу, чтобы в случае $a=0$ получать корректное решение (линейного) уравнения.

3. Что произойдет, если $a=b=c=0$? Каким должно быть решение в данном случае? Модернизируйте программу для корректрой работы в данном случае.


#### Ссылки

https://ru.wikipedia.org/wiki/Квадратное_уравнение