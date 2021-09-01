#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28730/problems/B/"""


# pylint: disable=invalid-name
# pylint: disable=too-many-boolean-expressions


from typing import Optional


def solve(stations: int, in_station: int, out_station: int) -> Optional[int]:
    """
    Return the number of stations between in- and out-stations.

    Parameters
    ----------
    stations : int
        total natural number of stations.
    in_station : int
        the number of station to get in.
    out_station : int
        the number of station to get out.

    Returns
    -------
    int

    """
    # let's make sure bad input won't be a hindrance
    if (
        (isinstance(stations, int) and stations > 0)
        and (isinstance(in_station, int) and 1 <= in_station <= stations)
        and (isinstance(out_station, int) and 1 <= out_station <= stations)
    ):
        in_station -= 1  # station values become indices
        out_station -= 1  # for the reason of modular arithmetics
        left, right = in_station, in_station
        step = 0
        while out_station not in (left, right):
            left = (left - 1) % stations
            right = (right + 1) % stations
            step += 1
        return max(0, step - 1)
    return None  # explicit


if __name__ == "__main__":
    sts, ist, jst = (int(var) for var in input().split())
    print(solve(sts, ist, jst))
