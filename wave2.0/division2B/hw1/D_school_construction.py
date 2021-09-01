#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28730/problems/D/"""


# pylint: disable=invalid-name


from math import ceil


if __name__ == "__main__":
    total = int(input())
    coords = [int(coord) for i, coord in zip(range(total), input().split())]
    if total:
        middle = total // 2
        if total % 2:
            print(coords[middle])
        else:
            print(ceil((coords[middle] + coords[middle]) / 2))
