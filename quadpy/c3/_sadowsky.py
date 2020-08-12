from sympy import Rational as frac
from sympy import sqrt

from ..helpers import article
from ._helpers import C3Scheme, expand_symmetries

source = article(
    authors=["Michael Sadowsky"],
    title="A Formula for Approximate Computation of a Triple Integral",
    journal="The American Mathematical Monthly",
    volume="47",
    number="8",
    month="oct",
    year="1940",
    pages="539-543",
    url="https://doi.org/10.2307/2303834",
)


def sadowsky():
    d = {
        "symm_r00": [[frac(91, 450)], [1]],
        "symm_rr0": [[frac(-20, 225)], [1]],
        "symm_rrs": [[frac(8, 225)], [sqrt(frac(5, 8))], [1]]
    }
    points, weights = expand_symmetries(d)
    return C3Scheme("Sadowsky", weights, points, 5, source)
