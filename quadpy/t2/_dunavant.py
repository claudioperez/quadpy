from sympy import Rational as frac

from ..helpers import article
from ._helpers import T2Scheme, concat, s1, s2, s3

source = article(
    authors=["D.A. Dunavant"],
    title="High Degree Efficient Symmetrical Gaussian Quadrature Rules for the Triangle",
    journal="Article in International Journal for Numerical Methods in Engineering",
    volume="21",
    number="6",
    pages="1129-1148",
    month="jun",
    year="1985",
    url="https://doi.org/10.1002/nme.1620210612",
)


def dunavant_01():
    weights, points = s3(1)
    return T2Scheme("Dunavant 1", weights, points, 1, source)


def dunavant_02():
    weights, points = s2([frac(1, 3), frac(1, 6)])
    return T2Scheme("Dunavant 2", weights, points, 2, source)


def dunavant_03():
    weights, points = concat(s3(-frac(9, 16)), s2([frac(25, 48), frac(1, 5)]))
    return T2Scheme("Dunavant 3", weights, points, 3, source)


def dunavant_04():
    weights, points = s2(
        [0.223381589678011, 0.445948490915965], [0.109951743655322, 0.091576213509771]
    )
    return T2Scheme("Dunavant 4", weights, points, 4, source)


def dunavant_05():
    weights, points = concat(
        s3(0.225),
        s2(
            [0.132394152788506, 0.4701420641051], [0.125939180544827, 0.101286507323456]
        ),
    )
    return T2Scheme("Dunavant 5", weights, points, 5, source, 1.795e-13)


def dunavant_06():
    weights, points = concat(
        s2(
            [0.116786275726379, 0.249286745170910],
            [0.050844906370207, 0.063089014491502],
        ),
        s1([0.082851075618374, 0.053145049844817, 0.310352451033784]),
    )
    return T2Scheme("Dunavant 6", weights, points, 6, source)


def dunavant_07():
    weights, points = concat(
        s3(-0.149570044467682),
        s2(
            [0.175615257433208, 0.260345966079040],
            [0.053347235608838, 0.065130102902216],
        ),
        s1([0.077113760890257, 0.048690315425316, 0.312865496004874]),
    )
    return T2Scheme("Dunavant 7", weights, points, 7, source)


def dunavant_08():
    weights, points = concat(
        s3(0.144315607677787),
        s2(
            [0.095091634267285, 0.459292588292723],
            [0.103217370534718, 0.170569307751760],
            [0.032458497623198, 0.050547228317031],
        ),
        s1([0.027230314174435, 0.008394777409958, 0.263112829634638]),
    )
    return T2Scheme("Dunavant 8", weights, points, 8, source)


def dunavant_09():
    # DUP equals TRIEX 19
    weights, points = concat(
        s3(0.097135796282799),
        s2(
            [0.031334700227139, 0.489682519198738],
            [0.077827541004774, 0.437089591492937],
            [0.079647738927210, 0.188203535619033],
            [0.025577675658698, 0.044729513394453],
        ),
        s1([0.043283539377289, 0.036838412054736, 0.221962989160766]),
    )
    return T2Scheme("Dunavant 9", weights, points, 9, source)


def dunavant_10():
    weights, points = concat(
        s3(0.090817990382754),
        s2(
            [0.036725957756467, 0.485577633383657],
            [0.045321059435528, 0.109481575485037],
        ),
        s1(
            [0.072757916845420, 0.141707219414880, 0.307939838764121],
            [0.028327242531057, 0.025003534762686, 0.246672560639903],
            [0.009421666963733, 0.009540815400299, 0.066803251012200],
        ),
    )
    return T2Scheme("Dunavant 10", weights, points, 10, source, 1.049e-14)


def dunavant_11():
    weights, points = concat(
        s2(
            [0.000927006328961, 0.534611048270758],
            [0.077149534914813, 0.398969302965855],
            [0.059322977380774, 0.203309900431282],
            [0.036184540503418, 0.119350912282581],
            [0.013659731002678, 0.032364948111276],
        ),
        s1(
            [0.052337111962204, 0.050178138310495, 0.356620648261293],
            [0.020707659639141, 0.021022016536166, 0.171488980304042],
        ),
    )
    return T2Scheme("Dunavant 11", weights, points, 11, source, 1.210e-13)


def dunavant_12():
    weights, points = concat(
        s2(
            [0.025731066440455, 0.488217389773805],
            [0.043692544538038, 0.439724392294460],
            [0.062858224217885, 0.271210385012116],
            [0.034796112930709, 0.127576145541586],
            [0.006166261051559, 0.021317350453210],
        ),
        s1(
            [0.040371557766381, 0.115343494534698, 0.275713269685514],
            [0.022356773202303, 0.022838332222257, 0.281325580989940],
            [0.017316231108659, 0.025734050548330, 0.116251915907597],
        ),
    )
    return T2Scheme("Dunavant 12", weights, points, 12, source)


def dunavant_13():
    weights, points = concat(
        s3(0.052520923400802),
        s2(
            [0.011280145209330, 0.495048184939705],
            [0.031423518362454, 0.468716635109574],
            [0.047072502504194, 0.414521336801277],
            [0.047363586536355, 0.229399572042831],
            [0.031167529045794, 0.114424495196330],
            [0.007975771465074, 0.024811391363459],
        ),
        s1(
            [0.036848402728732, 0.094853828379579, 0.268794997058761],
            [0.017401463303822, 0.018100773278807, 0.291730066734288],
            [0.015521786839045, 0.022233076674090, 0.126357385491669],
        ),
    )
    return T2Scheme("Dunavant 13", weights, points, 13, source)


def dunavant_14():
    weights, points = concat(
        s2(
            [0.021883581369429, 0.488963910362179],
            [0.032788353544125, 0.417644719340454],
            [0.051774104507292, 0.273477528308839],
            [0.042162588736993, 0.177205532412543],
            [0.014433699669777, 0.061799883090873],
            [0.004923403602400, 0.019390961248701],
        ),
        s1(
            [0.024665753212564, 0.057124757403648, 0.172266687821356],
            [0.038571510787061, 0.092916249356972, 0.336861459796345],
            [0.014436308113534, 0.014646950055654, 0.298372882136258],
            [0.005010228838501, 0.001268330932872, 0.118974497696957],
        ),
    )
    return T2Scheme("Dunavant 14", weights, points, 14, source)


def dunavant_15():
    weights, points = concat(
        s2(
            [0.001916875642849, 0.506972916858243],
            [0.044249027271145, 0.431406354283023],
            [0.051186548718852, 0.277693644847144],
            [0.023687735870688, 0.126464891041254],
            [0.013289775690021, 0.070808385974686],
            [0.004748916608192, 0.018965170241073],
        ),
        s1(
            [0.038550072599593, +0.133734161966621, 0.261311371140087],
            [0.027215814320624, +0.036366677396917, 0.575586555512814],
            [0.002182077366797, -0.010174883126571, 0.285712220049916],
            [0.021505319847731, +0.036843869875878, 0.215599664072284],
            [0.007673942631049, +0.012459809331199, 0.103575616576386],
        ),
    )
    return T2Scheme("Dunavant 15", weights, points, 15, source, 3.544e-14)


def dunavant_16():
    weights, points = concat(
        s3(0.046875697427642),
        s2(
            [0.006405878578585, 0.497380541948438],
            [0.041710296739387, 0.413469438549352],
            [0.026891484250064, 0.470458599066991],
            [0.042132522761650, 0.240553749969521],
            [0.030000266842773, 0.147965794222573],
            [0.014200098925024, 0.075465187657474],
            [0.003582462351273, 0.016596402623025],
        ),
        s1(
            [0.032773147460627, +0.103575692245252, 0.296555596579887],
            [0.015298306248441, +0.020083411655416, 0.337723063403079],
            [0.002386244192839, -0.004341002614139, 0.204748281642812],
            [0.019084792755899, +0.041941786468010, 0.189358492130623],
            [0.006850054546542, +0.014317320230681, 0.085283615682657],
        ),
    )
    return T2Scheme("Dunavant 16", weights, points, 16, source, 1.940e-14)


def dunavant_17():
    weights, points = concat(
        s3(0.033437199290803),
        s2(
            [0.005093415440507, 0.497170540556774],
            [0.014670864527638, 0.482176322624625],
            [0.024350878353672, 0.450239969020782],
            [0.031107550868969, 0.400266239377397],
            [0.031257111218620, 0.252141267970953],
            [0.024815654339665, 0.162047004658461],
            [0.014056073070557, 0.075875882260746],
            [0.003194676173779, 0.015654726967822],
        ),
        s1(
            [0.008119655318993, 0.334319867363658, 0.655493203809423],
            [0.026805742283163, 0.292221537796944, 0.572337590532020],
            [0.018459993210822, 0.319574885423190, 0.626001190286228],
            [0.008476868534328, 0.190704224192292, 0.796427214974071],
            [0.018292796770025, 0.180483211648746, 0.752351005937729],
            [0.006665632004165, 0.080711313679564, 0.904625504095608],
        ),
    )
    return T2Scheme("Dunavant 17", weights, points, 17, source, 1.117e-14)


def dunavant_18():
    weights, points = concat(
        s3(+0.030809939937647),
        s2(
            [+0.009072436679404, 0.493344808630921],
            [+0.018761316939594, 0.469210594241957],
            [+0.019441097985477, 0.436281395887006],
            [+0.027753948610810, 0.394846170673416],
            [+0.032256225351457, 0.249794568803157],
            [+0.025074032616922, 0.161432193743843],
            [+0.015271927971832, 0.076598227485371],
            [+0.006793922022963, 0.024252439353450],
            [-0.002223098729920, 0.043146367216965],
        ),
        s1(
            [+0.006331914076406, 0.358911494940944, 0.632657968856636],
            [+0.027257538049138, 0.294402476751957, 0.574410971510855],
            [+0.017676785649465, 0.325017801641814, 0.624779046792512],
            [+0.018379484638070, 0.184737559666046, 0.748933176523037],
            [+0.008104732808192, 0.218796800013321, 0.769207005420443],
            [+0.007634129070725, 0.101179597136408, 0.883962302273467],
            [+0.000046187660794, 0.020874755282586, 1.014347260005363],
        ),
    )
    return T2Scheme("Dunavant 18", weights, points, 18, source, 5.089e-13)


def dunavant_19():
    weights, points = concat(
        s3(0.032906331388919),
        s2(
            [0.010330731891272, 0.489609987073006],
            [0.022387247263016, 0.454536892697893],
            [0.030266125869468, 0.401416680649431],
            [0.030490967802198, 0.255551654403098],
            [0.024159212741641, 0.177077942152130],
            [0.016050803586801, 0.110061053227952],
            [0.008084580261784, 0.055528624251840],
            [0.002079362027485, 0.012621863777229],
        ),
        s1(
            [0.003884876904981, 0.395754787356943, 0.600633794794645],
            [0.025574160612022, 0.307929983880436, 0.557603261588784],
            [0.008880903573338, 0.264566948406520, 0.720987025817365],
            [0.016124546761731, 0.358539352205951, 0.594527068955871],
            [0.002491941817491, 0.157807405968595, 0.839331473680839],
            [0.018242840118951, 0.075050596975911, 0.701087978926173],
            [0.010258563736199, 0.142421601113383, 0.822931324069857],
            [0.003799928855302, 0.065494628082938, 0.924344252620784],
        ),
    )
    return T2Scheme("Dunavant 19", weights, points, 19, source, 1.670e-14)


def dunavant_20():
    weights, points = concat(
        s3(+0.033057055541624),
        s2(
            [+0.000867019185663, 0.500950464352200],
            [+0.011660052716448, 0.488212957934729],
            [+0.022876936356421, 0.455136681950283],
            [+0.030448982673938, 0.401996259318289],
            [+0.030624891725355, 0.255892909759421],
            [+0.024368057676800, 0.176488255995106],
            [+0.015997432032024, 0.104170855336758],
            [+0.007698301815602, 0.053068963840930],
            [-0.000632060497488, 0.041618715196029],
            [+0.001751134301193, 0.011581921406822],
        ),
        s1(
            [+0.016465839189576, 0.344855770229001, 0.606402646106160],
            [+0.004839033540485, 0.377843269594854, 0.615842614456541],
            [+0.025804906534650, 0.306635479062357, 0.559048000390295],
            [+0.008471091054441, 0.249419362774742, 0.736606743262866],
            [+0.018354914106280, 0.212775724802802, 0.711675142287434],
            [+0.000704404677908, 0.146965436053239, 0.861402717154987],
            [+0.010112684927462, 0.137726978828923, 0.835586957912363],
            [+0.003573909385950, 0.059696109149007, 0.929756171556853],
        ),
    )
    return T2Scheme("Dunavant 20", weights, points, 20, source, 4.690e-14)
