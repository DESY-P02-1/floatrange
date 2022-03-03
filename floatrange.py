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
    a, b, s = float(start), float(stop), float(step)
    x = (b - a) / s
    if x == 0:
        return asarray([])
    if abs(s)/max(abs(a), abs(b)) < 1e-12:
        # At some point there are not enough significant digits to represent
        # the difference of one step. A ratio of 1e-12 should be on the safe
        # side and this limit should hardly matter in practice.
        raise ValueError("Step is too small relative to the endpoints")
    A, n, d, N, r = a, s, 1, floor(x), round(x)
    if prevfloat(r) <= x <= nextfloat(r):
        T, D = rat(s)
        if (D * b - D * a) / r / D == s:
            A, n, d, N = D * a, T, D, r
        N -= 1  # due to subtle difference from Julia
        endpoint_plus_step = (A + (N + 1)* n) / d
        if (b - endpoint_plus_step) / (n / d) > 0.1:
            # Fix issue #4
            # In Julia the endpoint cannot be larger than stop, even if the
            # difference is tiny, but in Python endpoint > stop - step is not
            # a problem. If endpoint + step is still a significant part of a
            # step away from stop, we can add another step
            N += 1
    if prevfloat(b) <= a + N * s <= nextfloat(b):
        # Fix issue #3
        # If the endpoint is too close to stop, remove one step
        N -= 1
    ret = asarray([(A + k * n) / d for k in range(0, N + 1)])
    if N >= 0:
        ret[0] = start  # ensure start is contained exactly
    return ret
