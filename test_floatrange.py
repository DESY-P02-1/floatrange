from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from builtins import (bytes, str, open, super, range,  # noqa
                      zip, round, input, int, pow, object)

from floatrange import frange, prevfloat, nextfloat
from numpy import arange
import pytest


# testsuite from:
# https://github.com/JuliaLang/julia/blob/master/test/ranges.jl#L522
@pytest.mark.parametrize('start, step, stop, length',
                         [(1, 1, 3, 2), (0, 1, 3, 3),
                          (3, -1, -1, 4), (1, -1, -3, 4),
                          (0, 1, 10, 10), (0, 7, 21, 3),
                          (0, 11, 33, 3), (1, 11, 34, 3),
                          (0, 13, 39, 3), (1, 13, 40, 3),
                          (11, 11, 33, 2), (3, 1, 11, 8),
                          (0, 10, 55, 6), (0, -1, 5, 0),
                          (0, 10, 5, 1), (0, 1, 5, 5),
                          (0, -10, 5, 0), (0, -10, 0, 0),
                          (0, -1, 1, 0), (0, 1, -1, 0),
                          (0, -1, -10, 10)])
def test_frange_new(start, step, stop, length):
        r = frange(start/10, stop/10, step/10)
        a = arange(start, stop, step)/10
        assert len(r) == length
        if len(r) > 0:
            all(r == a)


# testsuite from https://github.com/JuliaLang/julia/pull/5636/files
def test_frange():
    assert all(frange(0.1, 0.3, 0.1) == arange(1, 3)/10)
    assert all(frange(0.0, 0.3, 0.1) == arange(0, 3)/10)
    assert all(frange(0.3, -0.1, -0.1) == arange(3, -1, -1)/10)
    assert all(frange(0.1, -0.3, -0.1) == arange(1, -3, -1)/10)
    assert all(frange(0.0, 1.0, 0.1) == arange(0, 10)/10)
    assert len(frange(0.0, 1.0, -0.1)) == 0
    assert len(frange(0.0, -1.0, 0.1)) == 0
    assert all(frange(0.0, -1.0, -0.1) == arange(0, -10, -1)/10)
    assert all(frange(1.0, 27.0, 1/49) == arange(49, 1323)/49)
    assert all(frange(0.0, 2.1, 0.7) == arange(0, 21, 7)/10)
    assert all(frange(0.0, 3.3, 1.1) == arange(0, 33, 11)/10)
    assert all(frange(0.1, 3.4, 1.1) == arange(1, 34, 11)/10)
    assert all(frange(0.0, 3.9, 1.3) == arange(0, 39, 13)/10)
    assert all(frange(0.1, 4.0, 1.3) == arange(1, 40, 13)/10)
    assert all(frange(1.1, 3.3, 1.1) == arange(11, 33, 11)/10)
    assert all(frange(0.3, 1.1, 0.1) == arange(3, 11, 1)/10)
    assert all(frange(3e-3, 1.1, 1e-3) == arange(3, 1100, 1)/1000)

    assert all(frange(0.0, 5.5, 1.0) == arange(0, 55, 10)/10)
    assert len(frange(0.0, 0.5, -1.0)) == 0
    assert frange(0.0, 0.5, 1.0) == [0.0]

    assert all(frange(prevfloat(0.1), 0.3, 0.1) == [prevfloat(0.1), 0.2])
    assert all(frange(nextfloat(0.1), 0.3, 0.1) == [nextfloat(0.1), 0.2])
    assert all(frange(prevfloat(0.0), 0.3, 0.1) == [prevfloat(0.0), 0.1, 0.2])
    assert all(frange(nextfloat(0.0), 0.3, 0.1) == [nextfloat(0.0), 0.1, 0.2])
    assert all(frange(0.1, prevfloat(0.3), 0.1) == [0.1, 0.2])
    assert all(frange(0.1, nextfloat(0.3), 0.1) == [0.1, 0.2])
    assert all(frange(0.0, prevfloat(0.3), 0.1) == [0.0, 0.1, 0.2])
    assert all(frange(0.0, nextfloat(0.3), 0.1) == [0.0, 0.1, 0.2])
    assert all(frange(0.1, 0.3, prevfloat(0.1)) == [0.1, 0.2])
    assert all(frange(0.1, 0.3, nextfloat(0.1)) == [0.1, 0.2])
    assert all(frange(0.0, 0.3, prevfloat(0.1)) == [0.0, prevfloat(0.1),
                                                    prevfloat(0.2)])
    assert all(frange(0.0, 0.3, nextfloat(0.1)) == [0.0, nextfloat(0.1),
                                                    nextfloat(0.2)])
