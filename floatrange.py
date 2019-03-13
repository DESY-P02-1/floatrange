from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from builtins import (bytes, str, open, super, range,  # noqa
                      zip, round, input, int, pow, object)

from numpy import nextafter, asarray
from math import trunc, floor


def nextfloat(x):
    return nextafter(x, x + 1)


def prevfloat(x):
    return nextafter(x, x - 1)


def inv(x):
    return 1/x


# ported to Python from:
# https://github.com/JuliaLang/julia/issues/2333#issuecomment-33830575
def rat(s):
    b, d, y = 0, 1, abs(s)
    while True:
        f = trunc(y)
        y -= f
        d, b = b, f * b + d
        a = round(b * s)
        if y == 0 or a / b == s:
            return a, b
        y = inv(y)


def frange(start, stop, step=1):
    """
        Create a array of numbers from start to stop with given step size

        The function works with floating point numbers. stop is never included
        in the range. Step size is 1 by default.
    """
    a, b, s = start, stop, step
    x = (b - a) / s
    if x == 0:
        return asarray([])
    A, n, d, N, r = a, s, 1, floor(x), round(x)
    if prevfloat(r) <= x <= nextfloat(r):
        T, D = rat(s)
        if (D * b - D * a) / r / D == s:
            A, n, d, N = D * a, T, D, r
        N = int(N) - 1  # due to subtle difference from Julia
    return asarray([(A + k * n) / d for k in range(0, N + 1)])
