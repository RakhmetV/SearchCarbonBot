from math import fabs


def calculation_one(variant, a, b):
    result = {
        0: fabs((a * 270 - b * 378) / 1000),
        1: fabs((a * b * 52 * 192 - a * b * 66) / 1000),
        2: fabs((a * 12 * 33 - 51.25) / 1000),
        3: fabs(a / b),
        4: fabs(a * 52 * 3 / (3.75 * 1000000 * 1000)),
        5: fabs((a * 52 * 150 - a * 52 * 80) / 1000),
        6: fabs((a * 12 * 180.09 - 2 * 403.2) / 1000),
        7: fabs((a * b * 12 * 3000 - 1 * 12 * 66) / 1000),  # тут переменная с вместо 1
        8: fabs((a * 52 * 26 - (a - 1) * 52 * 2) / 1000),
        9: fabs((b * 200 - a * 41) / 1000)
    }
    return result[variant]


def calculation_two(variant, a, b):
    result = {
        0: fabs((a * b * 52 * 7 * 22.75 - a * b * 5.7 * 52 * 7) / 1000),
        1: fabs((a * 52 * 66 - a * 52 * 17) / 1000),
        2: fabs((a * 52 * 12 - 78) / 1000),
        3: fabs((a * 52 * 23 - a * 52 * 18.25) / 1000),
        4: fabs((a * b * 52 * 66 - a * b * 52 * 35) / 1000),
        5: fabs((a * b * 52 * 5.5 - a * 36.55) / 1000),
        6: fabs((a * b * 52 * 7 * 22.75 - a * b * 26 * 7 * 22.75) / 1000),
        7: fabs((b * 8000 - a * 15000) / 1000),
        8: fabs((a * b * 52 * 32.5 - a * b * 52 * 4.875) / 1000),
        9: fabs((a * b * 12 - 645.12) / 1000),
    }
    return result[variant]
