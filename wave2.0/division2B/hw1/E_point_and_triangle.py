#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28730/problems/E/"""


# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name


from typing import Tuple


def dist(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
    """
    Return the distance between two 2D points.

    Parameters
    ----------
    point1: Tuple[int, int]
    point2: Tuple[int, int]

    Returns
    -------
    float

    """
    xc1, yc1 = point1
    xc2, yc2 = point2
    return ((xc2 - xc1) ** 2 + (yc2 - yc1) ** 2) ** 0.5


def solve(point: Tuple[int, int], leg: int) -> int:  # type: ignore
    """
    Return the code of a relation between a point and a right triangle.

    Parameters
    ----------
    point: Tuple[int, int]
        2d point with -1000 <= coord <= 1000 each.
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
    xcoord, ycoord = point
    if (0 <= xcoord <= leg) and (0 <= ycoord <= leg) and (ycoord <= -xcoord + leg):
        return 0
    # the dictionary may not meet the constraints of the task
    distances = [
        (dist(point, (0, 0)), 1),
        (dist(point, (leg, 0)), 2),
        (dist(point, (0, leg)), 3),
    ]
    return min(distances)[1]


if __name__ == "__main__":
    leg = int(input())  # of a right triangle
    xpoint = tuple(map(int, input().split()))[:2]  # an attempt to silence mypy
    print(solve(xpoint, leg))
