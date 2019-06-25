# -*- coding: utf-8 -*-
#

import numpy
import sympy

from ..helpers import untangle, fsd, z, article
from ._helpers import NCubeScheme

_citation = article(
    authors=["Preston C. Hammer", "Arthur H. Stroud"],
    title="Numerical Evaluation of Multiple Integrals II",
    journal="Math. Comp.",
    volume="12",
    year="1958",
    pages="272-280",
    url="https://doi.org/10.1090/S0025-5718-1958-0102176-6",
)


def hammer_stroud_1n(n, symbolic=False):
    frac = sympy.Rational if symbolic else lambda x, y: x / y
    sqrt = sympy.sqrt if symbolic else numpy.sqrt

    data = [(frac(1, 2 * n), fsd(n, (sqrt(frac(n, 3)), 1)))]
    points, weights = untangle(data)
    reference_volume = 2 ** n
    weights *= reference_volume
    return NCubeScheme("Hammer-Stroud 1n", n, weights, points, 3, _citation)


def hammer_stroud_2n(n, symbolic=False):
    frac = sympy.Rational if symbolic else lambda x, y: x / y
    sqrt = sympy.sqrt if symbolic else numpy.sqrt

    r = sqrt(frac(3, 5))
    data = [
        (frac(25 * n ** 2 - 115 * n + 162, 162), z(n)),
        (frac(70 - 25 * n, 162), fsd(n, (r, 1))),
        (frac(25, 324), fsd(n, (r, 2))),
    ]

    points, weights = untangle(data)
    reference_volume = 2 ** n
    weights *= reference_volume
    return NCubeScheme("Hammer-Stroud 2n", n, weights, points, 5, _citation)
