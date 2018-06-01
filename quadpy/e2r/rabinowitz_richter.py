# -*- coding: utf-8 -*-
#
'''
Philip Rabinowitz and Nira Richter,
Perfectly Symmetric Two-Dimensional Integration Formulas with Minimal
Numbers of Points,
Mathematics of Computation, Vol. 23, No. 108 (Oct., 1969), pp. 765-779,
<https://doi.org/10.2307/2004962>.
'''
from .helpers import _s40, _s8, _s4
from ..helpers import untangle



def gen1(symbolic):
    data = [
        (.3380228176732269e-1, _s40(6.822859174233539)),
        (.1467201651910359e+1, _s40(1.901350903458987)),
        (.6973178170307865e-1, _s4(4.260195453867070)),
        (.3030570706813315e-4, _s8(6.693991707281686, 14.77112509749386)),
        ]
    return 9, data


def gen2(symbolic):
    data = [
        (.1528937836199174e-3, _s40(12.74800100302598)),
        (.2460475747386993e-1, _s40(6.548756194884845)),
        (.1409433533958677e+1, _s40(1.760536818970077)),
        (.4416296048062511e-3, _s8(10.05412033203744, 5.804749080166705)),
        (.6786094118455858e-1, _s8(4.616780734333329, 2.665499599756826)),
        ]
    return 11, data


def gen3(symbolic):
    data = [
        (.1020154285801705e-3, _s40(13.23694157142503)),
        (.5959360016181913e-1, _s40(5.858647139727296)),
        (.1389898268451152e+1, _s40(1.719290407899388)),
        (.1691597241187992e-5, _s4(12.76644300362842)),
        (.1189929098056537e+0, _s4(3.556098987915152)),
        (.1103920675225255e-2, _s8(9.300537618869137, 4.847679857416328)),
        ]
    return 11, data


# ERR There's a misprint here somewhere.
# When replacing -.1010440929995067e+1 by -.1010440929995067e+3,
# the scheme has order 3.
# TODO find out what's going wrong
# def gen4():
#     data = [
#         (+.3497776022412480e+1, numpy.array([[0.0, 0.0]])),
#         (+.4425802565915590e-6, _s40(19.67638186041246)),
#         (+.4553409712395994e-2, _s40(8.770037945037203)),
#         (+.2775303265875652e-4, _s4(10.20568519238436)),
#         (+.3312777924884182e+1, _s4(3.591105603680783)),
#         (-.1010440929995067e+1, _s4(3.242171893025389)),
#         (+.1127213703086534e-3, _s8(11.94169301540818, 4.911904665577694)),
#         (+.4921143017387419e+2, _s8(3.287383483530638, 3.162277660168379)),
#         ]
#     return 13, data


def gen5(symbolic):
    data = [
        (.1783029629694328e-6, _s40(19.97643084360520)),
        (.3075756711058412e-3, _s40(11.52881449694446)),
        (.8468502916013910e-1, _s40(5.150382368000088)),
        (.1334535254221420e+1, _s40(1.610748055769942)),
        (.7736736266035205e-6, _s4(12.91466976228591)),
        (.5762989342268486e-3, _s4(7.598036758945039)),
        (.1439495304734647e+0, _s4(3.275323454134366)),
        (.5384883122895214e-5, _s8(14.96412806506222, 6.198344793636629)),
        (.3365458295852239e-2, _s8(8.095727497543633, 3.353360126759371)),
        ]
    return 15, data


_gen = {
    1: gen1,
    2: gen2,
    3: gen3,
    # 4: gen4,
    5: gen5,
    }


class RabinowitzRichter(object):
    keys = _gen.keys()

    def __init__(self, key):
        self.degree, data = _gen[key](False)
        self.points, self.weights = untangle(data)
        return
