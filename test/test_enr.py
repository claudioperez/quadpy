# -*- coding: utf-8 -*-
#
import pytest
import quadpy

from helpers import check_degree, integrate_monomial_over_enr


@pytest.mark.parametrize(
    'scheme,tol',
    [(quadpy.enr2.StroudSecrest(n, index), 1.0e-14) for n in range(2, 6)
        for index in [
            'I', 'II',
            ]]
    )
def test_scheme(scheme, tol):
    n = scheme.dim
    degree = check_degree(
            lambda poly: quadpy.enr2.integrate(poly, scheme),
            integrate_monomial_over_enr,
            lambda k: quadpy.helpers.partition(k, n),
            scheme.degree + 1,
            tol=tol
            )
    assert degree == scheme.degree, \
        'Observed: {}   expected: {}'.format(degree, scheme.degree)
    return


if __name__ == '__main__':
    dim_ = 5
    # quadpy.e3r2.show(quadpy.enr2.Stroud(dim_, '5-1a'), backend='vtk')
    scheme_ = quadpy.enr.StroudSecrest(dim_, 'II')
    test_scheme(scheme_, 1.0e-14)
