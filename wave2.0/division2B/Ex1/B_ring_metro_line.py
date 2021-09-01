#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28730/problems/B/"""


def solve(stations: int,
          istation: int,
          jstation: int) -> int:
    # let's make sure bad input won't be a hindrance 
    if (isinstance(stations, int) and stations > 0) and \
        (isinstance(istation, int) and 1 <= istation <= stations) and \
        (isinstance(jstation, int) and 1 <= jstation <= stations):
            istation -= 1  # station values become indices
            jstation -= 1  # for the reason of modular arithmetics
            left, right = istation, istation
            step = 0
            while (left != jstation) and (right != jstation):
                left = (left - 1) % stations
                right = (right + 1) % stations
                step += 1
            return max(0, step - 1)


if __name__ == '__main__':
    sts, ist, jst = (int(var) for var in input().split())
    print(solve(sts, ist, jst))
