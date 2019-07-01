import numpy

from ..helpers import article
from ._helpers import E1r2Scheme

citation = article(
    authors=["Alan Genz", "B.D. Keister"],
    title="Fully symmetric interpolatory rules for multiple integrals over infinite regions with Gaussian weight",
    journal="Journal of Computational and Applied Mathematics",
    volume="71",
    number="2",
    month="jul",
    year="1996",
    pages="299-309",
    url="https://doi.org/10.1016/0377-0427(95)00232-4",
)


_points_0 = [0.0]
_points_1 = _points_0 + [1.2247448713915889e00]
_points_2 = _points_1 + [
    5.2403354748695763e-01,
    2.0232301911005157e00,
    2.9592107790638380e00,
]
_points_3 = _points_2 + [
    8.7004089535290285e-01,
    1.8357079751751868e00,
    2.2665132620567876e00,
    3.6677742159463378e00,
    4.4995993983103881e00,
]
# Final extensions
_points_4 = _points_3 + [
    1.7606414208200893e-01,
    1.5794121348467671e00,
    2.5705583765842968e00,
    3.3491639537131945e00,
    4.0292201405043713e00,
    5.0360899444730940e00,
    5.6432578578857449e00,
    6.3759392709822356e00,
]
_points_5 = _points_3 + [
    0.214618180588171e00,
    1.561553427651873e00,
    2.597288631188366e00,
    3.315584617593290e00,
    4.057956316089741e00,
    4.986551454150765e00,
    5.521865209868350e00,
    6.124527854622158e00,
    6.853200069757519e00,
]
_points_6 = _points_3 + [
    0.195324784415805e00,
    1.585873011819188e00,
    2.043834754429505e00,
    2.630415236459871e00,
    3.296114596212218e00,
    4.070919267883068e00,
    4.953574342912980e00,
    5.437443360177798e00,
    5.961461043404500e00,
    6.547083258397540e00,
    7.251792998192644e00,
]
_points_7 = _points_3 + [
    0.196029453662011e00,
    1.583643465293944e00,
    2.089340389294661e00,
    2.633356763661946e00,
    3.295265921534226e00,
    4.071335874253583e00,
    4.952329763008589e00,
    5.434053000365068e00,
    5.954781975039809e00,
    6.535398426382995e00,
    7.231746029072501e00,
    10.167574994881873e00,
]


def genz_keister(n):
    assert n >= 0

    if n == 0:
        degree = 1
        weights = [1.7724538509055159e00]
        points = _points_0
    elif n == 1:
        degree = 5
        points = _points_1
        weights = [1.1816359006036772e00, 2.9540897515091930e-01]
    elif n == 2:
        degree = 15
        points = _points_2
        weights = [
            4.5014700975378197e-01,
            4.7869428549114124e-01,
            1.6811892894767771e-01,
            1.4173117873979098e-02,
            1.6708826306882348e-04,
        ]
    elif n == 3:
        degree = 29
        points = _points_3
        weights = [
            5.3788160700510168e-01,
            3.6924643368920851e-01,
            1.0838861955003017e-01,
            1.1360729895748269e-01,
            3.2055243099445879e-02,
            -1.1232438489069229e-02,
            5.1133174390883855e-03,
            1.0656589772852267e-04,
            1.0802767206624762e-06,
            1.5295717705322357e-09,
        ]
    elif n == 4:
        degree = 51
        points = _points_4
        weights = numpy.array(
            [
                9.1262675363737921e-04,
                3.3988595585585218e-01,
                2.6244871488784277e-01,
                1.6371221555735804e-01,
                8.0245518147390893e-02,
                2.7780508908535097e-02,
                5.5928828911469180e-03,
                4.0967527720344047e-03,
                1.4515580425155904e-03,
                4.8785399304443770e-04,
                6.3328620805617891e-05,
                4.8462799737020461e-06,
                4.3737818040926989e-07,
                3.7920222392319532e-08,
                8.1553721816916897e-10,
                5.4896836948499462e-12,
                9.6599466278563243e-15,
                1.8684014894510604e-18,
            ]
        )
    elif n == 5:
        degree = 55
        points = _points_5
        weights = numpy.array(
            [
                0.171719680968980257e00,
                0.261712932511430884e00,
                0.253636910481387185e00,
                0.16611584261479281e00,
                0.783630990508037449e-01,
                0.274962713372148476e-01,
                0.768092665770660459e-02,
                0.313373786000304381e-02,
                0.174733389581099482e-02,
                0.41642095727577091e-03,
                0.571885531470621903e-04,
                0.586639457073896277e-05,
                0.524482423744884136e-06,
                0.294146671497083432e-07,
                0.748907559239519284e-09,
                0.809333688669950037e-11,
                0.323016866782871498e-13,
                0.332834739632930463e-16,
                0.337304188079177058e-20,
            ]
        )
    elif n == 6:
        degree = 63
        points = _points_6
        weights = numpy.array(
            [
                0.997525375254611951e-01,
                0.293588795735908566e00,
                0.258718519718241095e00,
                0.164543666806555251e00,
                0.799536390803302298e-01,
                0.293244560924894295e-01,
                0.125041498584003435e-02,
                0.317007878644325588e-01,
                -0.25616995850607458e-01,
                0.249379691096933139e-02,
                0.335013114947200879e-03,
                0.512198007019776873e-04,
                0.675628907134744976e-05,
                0.558982787078644997e-06,
                0.264376044449260516e-07,
                0.710371395169350952e-09,
                0.103121966469463034e-10,
                0.724614869051195508e-13,
                0.202183949965101288e-15,
                0.152506745534300636e-18,
                0.117725656974405367e-22,
            ]
        )
    else:
        assert n == 7
        degree = 67
        points = _points_7
        weights = numpy.array(
            [
                0.102730713753441829e00,
                0.292243810406117141e00,
                0.258535954731607738e00,
                0.164609842422580606e00,
                0.798689557875757008e-01,
                0.29000335749726387e-01,
                0.248083722871002796e-02,
                0.119383201790913588e-01,
                -0.687704270963253854e-02,
                0.267479828788552937e-02,
                0.32753080006610181e-03,
                0.508343873102544037e-04,
                0.680410934802210232e-05,
                0.560127964848432175e-06,
                0.263481722999966618e-07,
                0.70903573389336778e-09,
                0.104028132097205732e-10,
                0.747837010380540069e-13,
                0.217337608710893738e-15,
                0.175937309107750992e-18,
                0.15516931262860431e-22,
                0.968100020641528185e-37,
            ]
        )

    w = numpy.array(weights)
    weights = numpy.concatenate([w[1:][::-1], [w[0]], w[1:]])

    p = numpy.sort(points)
    points = numpy.concatenate([-p[1:][::-1], [p[0]], p[1:]])

    return E1r2Scheme("Genz-Keister ({})".format(n), weights, points, degree, citation)
