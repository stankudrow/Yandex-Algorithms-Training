#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28730/problems/D/"""


# pylint: disable=invalid-name


# 0 < total < 100001
# abs(coord) <= 2e9
if __name__ == "__main__":
    total = int(input())
    coords = [int(coord) for coord in input().split()]
    print(coords[total // 2])
