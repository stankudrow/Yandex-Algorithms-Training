#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28730/problems/E/"""


# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name


from typing import Tuple


def sqdist(point1: Tuple[int, int], point2: Tuple[int, int]) -> int:
    """
    Return the squared distance between two 2D points.

    Parameters
    ----------
    point1: Tuple[int, int]
    point2: Tuple[int, int]

    Returns
    -------
    int

    """
    xc1, yc1 = point1
    xc2, yc2 = point2
    return ((xc2 - xc1) ** 2 + (yc2 - yc1) ** 2)


def solve(xcoord: int, ycoord: int, leg: int) -> int:
    """
    Return the code of a relation between a point and a right triangle.

    Parameters
    ----------
    xcoord: int
        -1000 <= xcoord <= 1000.
    ycoord: int
        -1000 <= ycoord <= 1000.
    leg: int
        1 <= leg <= 1000.

    Returns
    -------
    int
        0 if the point belongs to the right triangle:
        otherwise:
            1 if the point is the closest to the point A(0, 0)
            2 if the point is the closest to the point B(leg, 0)
            3 if the point is the closest to the point C(0, leg)

    """
    if (0 <= xcoord <= leg) and (0 <= ycoord <= leg) and (ycoord <= -xcoord + leg):
        return 0
    point = (xcoord, ycoord)
    distances = [
        (sqdist(point, (0, 0)), 1),
        (sqdist(point, (leg, 0)), 2),
        (sqdist(point, (0, leg)), 3),
    ]
    return min(distances)[1]


if __name__ == "__main__":
    leg = int(input())  # of a right triangle
    xcoord, ycoord = map(int, input().split())
    print(solve(xcoord, ycoord, leg))
