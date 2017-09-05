# -*- coding: utf-8 -*-
#
import pytest
import quadpy

from helpers import check_degree, integrate_monomial_over_enr


@pytest.mark.parametrize(
    'scheme,tol',
    [(quadpy.e2r.RabinowitzRichter(k), 1.0e-14) for k in [1, 2, 3, 5]]
    + [(quadpy.e2r.StroudSecrest(k), 1.0e-14) for k in ['V', 'VI']]
    )
def test_scheme(scheme, tol):
    degree = check_degree(
            lambda poly: quadpy.e2r.integrate(poly, scheme),
            integrate_monomial_over_enr,
            lambda n: quadpy.helpers.partition(n, 2),
            scheme.degree + 1,
            tol=tol
            )
    assert degree == scheme.degree, \
        'Observed: {}   expected: {}'.format(degree, scheme.degree)
    return


@pytest.mark.parametrize(
    'scheme',
    [quadpy.e2r.RabinowitzRichter(1)]
    )
def test_show(scheme):
    quadpy.e2r.show(scheme)
    return


if __name__ == '__main__':
    scheme_ = quadpy.e2r.RabinowitzRichter(5)
    test_scheme(scheme_, 1.0e-14)
    test_show(scheme_)
