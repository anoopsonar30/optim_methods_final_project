import pathlib

import numpy as np
from PIL import Image


def get_lines():
    lines = [
        np.array([[1696, 1959], [2796, 1743]]),
        np.array([[1696, 2195], [1696, 1959]]),
        np.array([[1696, 2195], [1900, 2239]]),
        np.array([[1908, 2239], [2204, 2239]]),
        np.array([[2204, 1863], [2208, 2071]]),
        np.array([[2208, 2071], [2388, 2067]]),
        np.array([[2464, 1827], [2468, 2163]]),
        np.array([[2464, 2235], [2796, 2239]]),
        np.array([[2796, 2235], [2796, 1819]]),
        np.array([[2468, 2051], [2796, 2051]]),
        np.array([[1579, 2190], [1571, 2334]]),
        np.array([[1571, 2334], [1411, 2286]]),
        np.array([[1411, 2286], [1347, 2522]]),
        np.array([[1347, 2522], [1503, 2574]]),
        np.array([[1503, 2574], [1451, 2842]]),
        np.array([[1451, 2842], [1623, 2842]]),
        np.array([[1623, 2842], [1627, 2978]]),
        np.array([[1627, 2978], [2311, 2974]]),
        np.array([[2311, 2974], [2315, 2646]]),
        np.array([[2315, 2646], [3159, 2642]]),
        np.array([[3159, 2642], [3147, 2998]]),
        np.array([[3151, 2998], [3715, 2986]]),
        np.array([[3711, 2986], [3627, 2674]]),
        np.array([[3627, 2674], [4427, 2458]]),
        np.array([[4427, 2458], [4511, 2726]]),
        np.array([[4516, 2722], [5024, 2622]]),
        np.array([[5020, 2618], [5000, 2478]]),
        np.array([[5008, 2478], [5128, 2454]]),
        np.array([[5128, 2454], [5092, 2278]]),
        np.array([[5092, 2278], [5040, 2290]]),
        np.array([[5040, 2290], [4964, 2098]]),
        np.array([[4964, 2098], [5036, 2070]]),
        np.array([[5040, 2067], [4936, 1831]]),
        np.array([[5088, 1951], [5000, 1727]]),
        np.array([[5000, 1727], [5056, 1707]]),
        np.array([[5056, 1707], [4952, 1487]]),
        np.array([[4856, 1543], [4920, 1663]]),
        np.array([[4920, 1663], [4808, 1727]]),
        np.array([[4612, 1659], [4684, 1787]]),
        np.array([[4684, 1787], [4816, 1723]]),
        np.array([[4476, 1723], [4320, 1803]]),
        np.array([[4320, 1803], [4272, 1799]]),
        np.array([[4272, 1799], [4268, 1955]]),
        np.array([[4268, 1963], [4312, 2019]]),
        np.array([[4316, 2019], [4468, 2031]]),
        np.array([[4488, 2067], [4468, 2031]]),
        np.array([[4476, 2031], [4756, 1911]]),
        np.array([[4720, 1935], [4824, 2151]]),
        np.array([[4552, 2211], [4572, 2255]]),
        np.array([[4576, 2251], [4960, 2095]]),
        np.array([[4824, 1883], [4936, 1831]]),
        np.array([[2796, 2346], [2796, 2638]]),
        np.array([[2912, 2354], [3208, 2362]]),
        np.array([[3140, 2414], [3156, 2638]]),
        np.array([[3244, 2386], [3312, 2362]]),
        np.array([[3312, 2362], [3308, 2666]]),
        np.array([[3316, 2666], [3492, 2662]]),
        np.array([[3268, 1737], [3268, 2189]]),
        np.array([[3276, 2033], [3416, 2033]]),
        np.array([[3492, 2001], [3496, 1737]]),
        np.array([[3276, 1737], [3492, 1737]]),
        np.array([[3496, 1737], [3724, 1733]]),
        np.array([[3724, 1733], [3720, 2033]]),
        np.array([[3720, 2033], [3572, 2037]]),
        np.array([[3688, 2045], [3696, 2069]]),
        np.array([[3724, 1733], [3948, 1737]]),
        np.array([[3948, 1737], [3952, 2033]]),
        np.array([[3800, 2033], [3952, 2033]]),
        np.array([[3772, 2157], [4132, 2157]]),
        np.array([[4132, 2157], [4148, 2249]]),
        np.array([[4160, 2301], [4176, 2341]]),
        np.array([[4184, 2389], [4224, 2513]]),
        np.array([[4164, 2317], [3936, 2377]]),
        np.array([[3872, 2157], [3992, 2581]]),
        np.array([[3700, 2429], [3932, 2365]]),
        np.array([[3692, 2121], [3696, 2549]]),
        np.array([[3692, 2609], [3692, 2657]]),
        np.array([[4692, 1365], [4952, 1337]]),
        np.array([[4904, 1017], [4956, 1337]]),
        np.array([[4916, 1029], [5068, 1005]]),
        np.array([[5020, 913], [5192, 1257]]),
        np.array([[5028, 1333], [5212, 1241]]),
        np.array([[5260, 1217], [5372, 1161]]),
        np.array([[5236, 841], [5356, 1173]]),
        np.array([[5040, 909], [5472, 765]]),
        np.array([[5468, 773], [5524, 1125]]),
        np.array([[5520, 1125], [5424, 1149]]),
        np.array([[5524, 1137], [5544, 1225]]),
        np.array([[5554, 1217], [5978, 1009]]),
        np.array([[5978, 1009], [6422, 1869]]),
        np.array([[6418, 1873], [5534, 2325]]),
        np.array([[5534, 2321], [5430, 2125]]),
        np.array([[5430, 2125], [5714, 1977]]),
        np.array([[5750, 2037], [5942, 1941]]),
        np.array([[5806, 2017], [5870, 2149]]),
        np.array([[5998, 1925], [6078, 2057]]),
        np.array([[5986, 1905], [6050, 1877]]),
        np.array([[6006, 1793], [6302, 1637]]),
        np.array([[5994, 1769], [6018, 1813]]),
        np.array([[5970, 1721], [5918, 1621]]),
        np.array([[6218, 1485], [5930, 1641]]),
        np.array([[5910, 1641], [5790, 1701]]),
        np.array([[5790, 1701], [5766, 1693]]),
        np.array([[5766, 1693], [5550, 1809]]),
        np.array([[5838, 1465], [5894, 1577]]),
        np.array([[5854, 1485], [6150, 1333]]),
        np.array([[5758, 1309], [5814, 1417]]),
        np.array([[5770, 1337], [6066, 1181]]),
        np.array([[5682, 1169], [5734, 1261]]),
        np.array([[5492, 1841], [5316, 1497]]),
        np.array([[5236, 1345], [5320, 1497]]),
        np.array([[5064, 1701], [5184, 1641]]),
        np.array([[5384, 2041], [5184, 1641]]),
        np.array([[4960, 1485], [5236, 1345]]),
        np.array([[3959, 1801], [4143, 1797]]),
        np.array([[3499, 2801], [3503, 2993]]),
        np.array([[3499, 2737], [3643, 2733]]),
        np.array([[2466, 2525], [2470, 2645]]),
        np.array([[2470, 2445], [2798, 2445]]),
        np.array([[2918, 1321], [2914, 1637]]),
        np.array([[2914, 1637], [3130, 1637]]),
        np.array([[3130, 1633], [3134, 1457]]),
        np.array([[3270, 1321], [3270, 1641]]),
        np.array([[3270, 1641], [3942, 1637]]),
        np.array([[3942, 1633], [3934, 1609]]),
        np.array([[3938, 1553], [3934, 1513]]),
        np.array([[3934, 1513], [3686, 1337]]),
        np.array([[3686, 1337], [3666, 1373]]),
        np.array([[3666, 1373], [3670, 1637]]),
        np.array([[3530, 1377], [3670, 1373]]),
        np.array([[3450, 1325], [3458, 1633]]),
        np.array([[3458, 1381], [3478, 1377]]),
        np.array([[3346, 1317], [3450, 1325]]),
        np.array([[4200, 1421], [4216, 1577]]),
        np.array([[4220, 1573], [4484, 1545]]),
        np.array([[4548, 1449], [4560, 1433]]),
        np.array([[4560, 1433], [4548, 1377]]),
        np.array([[4548, 1377], [4440, 1393]]),
        np.array([[4368, 1401], [4200, 1417]]),
        np.array([[4368, 1393], [4360, 1281]]),
        np.array([[4360, 1281], [4476, 1261]]),
        np.array([[4476, 1261], [4500, 1385]]),
        np.array([[4428, 869], [4468, 1261]]),
        np.array([[4428, 865], [4164, 681]]),
        np.array([[4164, 685], [3932, 1025]]),
        np.array([[3948, 1033], [4140, 1169]]),
        np.array([[4140, 1169], [4104, 1221]]),
        np.array([[4304, 1297], [4360, 1229]]),
        np.array([[4360, 1229], [4372, 1241]]),
        np.array([[4372, 1249], [4376, 1277]]),
        np.array([[4252, 1289], [4256, 1277]]),
        np.array([[4260, 1277], [4304, 1301]]),
        np.array([[4076, 1329], [3824, 1153]]),
        np.array([[3828, 1145], [3932, 1021]]),
        np.array([[3944, 1509], [3980, 1465]]),
        np.array([[4016, 1413], [4080, 1329]]),
        np.array([[2849, 1637], [2757, 1637]]),
        np.array([[2753, 1609], [2729, 1385]]),
        np.array([[2717, 1321], [2913, 1321]]),
        np.array([[2697, 1237], [2721, 1317]]),
        np.array([[2457, 1281], [2385, 1017]]),
        np.array([[2385, 1017], [2473, 929]]),
        np.array([[2473, 933], [2585, 885]]),
        np.array([[2585, 885], [2757, 853]]),
        np.array([[2757, 853], [2905, 877]]),
        np.array([[2905, 881], [3001, 957]]),
        np.array([[3005, 961], [3045, 1049]]),
        np.array([[3045, 1057], [3049, 1101]]),
        np.array([[3049, 1101], [3077, 1105]]),
        np.array([[2669, 1145], [2701, 1237]]),
        np.array([[2461, 1285], [2693, 1241]]),
        np.array([[2433, 1141], [2641, 1069]]),
        np.array([[2637, 1045], [2653, 1093]]),
        np.array([[2581, 889], [2621, 997]]),
        np.array([[3077, 1105], [3157, 969]]),
        np.array([[3153, 977], [3229, 901]]),
        np.array([[3229, 897], [3361, 817]]),
        np.array([[3361, 817], [3489, 797]]),
        np.array([[3493, 797], [3597, 809]]),
        np.array([[3597, 809], [3529, 1033]]),
        np.array([[3529, 1033], [3561, 1057]]),
        np.array([[3605, 1085], [3717, 1137]]),
        np.array([[3717, 1137], [3813, 977]]),
        np.array([[3813, 961], [3845, 849]]),
        np.array([[3845, 849], [3601, 813]]),
        np.array([[3721, 1133], [3665, 1209]]),
        np.array([[3665, 1209], [3765, 1193]]),
        np.array([[3765, 1193], [3821, 1149]]),
        np.array([[3669, 1317], [3689, 1333]]),
        np.array([[3761, 1189], [3669, 1313]]),
        np.array([[1577, 2145], [1585, 2185]]),
        np.array([[1581, 2045], [1577, 2017]]),
        np.array([[1577, 2017], [1453, 2037]]),
        np.array([[1453, 2029], [1421, 1897]]),
        np.array([[1425, 1897], [1621, 1853]]),
        np.array([[1621, 1849], [1605, 1781]]),
        np.array([[1605, 1781], [1585, 1685]]),
        np.array([[1573, 1629], [1565, 1593]]),
        np.array([[1557, 1537], [1533, 1421]]),
        np.array([[1525, 1369], [1501, 1257]]),
        np.array([[1489, 1201], [1485, 1181]]),
        np.array([[1485, 1181], [1517, 1177]]),
        np.array([[1517, 1177], [1501, 1101]]),
        np.array([[1501, 1101], [2065, 989]]),
        np.array([[2065, 989], [2121, 1293]]),
        np.array([[2129, 1345], [2145, 1413]]),
        np.array([[2145, 1413], [2193, 1401]]),
        np.array([[2065, 997], [2217, 965]]),
        np.array([[2213, 969], [2293, 1349]]),
        np.array([[2293, 1349], [2137, 1377]]),
        np.array([[2165, 1517], [2213, 1741]]),
        np.array([[2073, 1693], [2089, 1757]]),
        np.array([[2089, 1757], [1745, 1825]]),
        np.array([[1745, 1825], [1721, 1757]]),
        np.array([[2629, 1569], [2653, 1661]]),
        np.array([[2649, 1661], [2501, 1689]]),
        np.array([[2497, 1681], [2473, 1609]]),
        np.array([[2461, 1609], [2197, 1661]]),
        np.array([[2329, 1645], [2341, 1717]]),
        np.array([[2341, 1717], [2381, 1709]]),
        np.array([[2469, 1609], [2433, 1369]]),
        np.array([[2433, 1369], [2589, 1345]]),
        np.array([[2593, 1349], [2613, 1417]]),
        np.array([[2621, 1417], [2729, 1385]]),
        np.array([[1497, 1101], [1173, 1169]]),
        np.array([[1173, 1173], [1325, 1925]]),
        np.array([[1333, 1921], [1421, 1901]]),
        np.array([[1301, 1825], [1601, 1781]]),
        np.array([[1281, 1665], [1569, 1609]]),
        np.array([[1245, 1501], [1541, 1441]]),
        np.array([[1205, 1333], [1505, 1273]]),
        np.array([[2033, 2465], [2013, 2541]]),
        np.array([[1993, 2637], [1961, 2705]]),
        np.array([[1961, 2705], [1725, 2633]]),
        np.array([[1725, 2625], [1797, 2405]]),
        np.array([[1801, 2409], [2033, 2465]]),
        np.array([[1677, 2369], [1609, 2597]]),
        np.array([[1609, 2597], [1509, 2581]]),
        np.array([[1649, 2365], [1697, 2377]]),
        np.array([[1777, 2397], [1797, 2405]]),
        np.array([[5536, 1929], [5556, 1965]]),
        np.array([[5552, 1965], [5392, 2041]]),
        np.array([[5412, 2097], [5420, 2121]]),
        np.array([[1493, 2121], [1497, 2309]]),
        np.array([[1329, 2077], [1457, 2041]]),
        np.array([[1365, 2149], [1493, 2121]]),
    ]
    n_lines = len(lines)
    # (n_lines, n_points, 2)
    lines = np.stack(lines, axis=0)
    assert lines.shape == (n_lines, 2, 2)
    return lines


def get_rects():
    """Get lines, but bloated to become rectangles."""
    # (n_lines, n_points, 2)
    lines = get_lines()

    # Extend both perp and tan directions.
    thick_perp = 5
    thick_tan = 8

    # 1: Unit vector of the line.
    tangent = lines[:, 1] - lines[:, 0]
    # (n_lines, 2)
    tangent = tangent / np.linalg.norm(tangent, axis=-1, keepdims=True)
    # (n_lines, 2)
    perp = np.stack([-tangent[:, 1], tangent[:, 0]], axis=1)

    # Get four corners of the rectangle in clockwise order.
    p0 = lines[:, 0] + thick_perp * perp - thick_tan * tangent
    p1 = lines[:, 1] + thick_perp * perp + thick_tan * tangent
    p2 = lines[:, 1] - thick_perp * perp + thick_tan * tangent
    p3 = lines[:, 0] - thick_perp * perp - thick_tan * tangent

    # (n_lines, 4, 2)
    rects = np.stack([p0, p1, p2, p3], axis=1)
    return rects


def get_seed_points():
    seed_points = [
        [1996, 2851],
        [2192, 2391],
        [1872, 2551],
        [1500, 2467],
        [2080, 2139],
        [2352, 1943],
        [2684, 1915],
        [2656, 2135],
        [3124, 2127],
        [2192, 1811],
        [1824, 1471],
        [1404, 1699],
        [1388, 1539],
        [1436, 1371],
        [1340, 1227],
        [2188, 1183],
        [3456, 2271],
        [3340, 2787],
        [4284, 2163],
        [4072, 1611],
        [4456, 1899],
        [5532, 1427],
        [3544, 1683],
        [3024, 1467],
        [3368, 1175],
        [2840, 1063],
        [3368, 1471],
        [3572, 1487],
        [3788, 1515],
        [4208, 1107],
        [4676, 1515],
        [3840, 1899],
        [3644, 1907],
        [3412, 1895],
        [2972, 2515],
        [2596, 2543],
        [1604, 1939],
        [2556, 1191],
        [2520, 1007],
        [2692, 1703],
        [5189, 1035],
        [5405, 971],
        [5837, 1167],
        [5949, 1319],
        [6013, 1479],
        [6117, 1647],
        [6177, 1835],
        [5917, 1783],
        [5693, 2147],
        [5709, 1907],
        [4921, 1751],
        [4848, 1999],
        [4624, 2107],
        [4202, 1883],
        [1766, 2293],
        [1650, 2721],
        [1710, 2497],
        [1508, 1220],
        [1536, 1400],
        [1564, 1556],
        [1584, 1656],
        [1668, 1788],
        [1640, 2089],
        [1616, 2346],
        [2032, 2590],
        [2348, 2169],
        [2496, 2185],
        [2424, 2049],
        [1924, 1861],
        [2128, 1701],
        [2448, 1749],
        [2884, 1685],
        [2656, 1120],
        [2624, 1024],
        [3192, 1480],
        [3316, 1324],
        [3512, 1384],
        [3592, 1060],
        [3928, 1584],
        [4112, 1400],
        [4092, 1276],
        [4180, 1264],
        [5232, 1228],
        [5396, 1156],
        [5748, 1284],
        [5832, 1440],
        [5908, 1596],
        [5980, 1744],
        [6028, 1832],
        [5960, 1924],
        [5728, 2008],
        [5512, 1820],
        [5204, 1304],
        [4916, 1528],
        [4988, 1400],
        [4520, 1700],
        [4376, 1648],
        [4788, 1900],
        [3948, 2096],
        [3708, 2096],
        [3736, 2168],
        [3772, 2036],
        [3536, 2028],
        [3444, 2036],
        [3260, 2240],
        [3544, 2666],
        [3224, 2366],
        [2832, 2366],
        [2792, 2294],
        [2788, 1789],
        [2470, 2485],
        [2206, 2709],
        [1642, 2193],
        [1554, 2093],
        [2570, 1516],
        [2678, 1644],
        [2122, 1316],
        [2158, 1464],
        [4783, 2414],
        [5059, 2378],
    ]
    seed_points = np.array(seed_points)
    n_seeds = len(seed_points)
    assert seed_points.shape == (n_seeds, 2)
    return seed_points


def get_seed_points2():
    seed_points = np.array(
        [
            [3.489958, 2.697444],
            [3.881697, 1.682553],
            [3.356850, 1.679358],
            [3.697652, 1.694607],
            [2.326985, 1.771184],
            [2.572353, 1.724167],
            [2.798620, 1.688904],
            [3.646388, 2.097361],
            [5.443304, 1.236370],
            [3.575495, 1.081113],
            [3.503869, 1.318649],
        ]
    )
    seed_points = seed_points * 1e3
    n_seeds = len(seed_points)
    assert seed_points.shape == (n_seeds, 2)
    return seed_points


def get_sources():
    srcs = np.array(
        [
            [1524, 2096],
            [4932, 1768],
            [4628, 1432],
        ]
    )
    assert srcs.shape == (len(srcs), 2)
    return srcs


def get_dests():
    dests = np.array(
        [
            [1388, 1560],
            [6200, 1856],
            [4404, 1952],
            [3344, 2840],
            [2480, 1004],
            [3352, 1481],
            [3768, 1525],
            [3604, 1905],
            [3376, 1889],
            [3376, 1889],
        ]
    )
    assert dests.shape == (len(dests), 2)
    return dests


def get_floorplan_image() -> Image.Image:
    image_path = pathlib.Path("32_2.jpg")
    im = Image.open(image_path)
    im = im.convert("RGB")
    return im
