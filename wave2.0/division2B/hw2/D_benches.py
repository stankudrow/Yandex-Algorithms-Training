#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28738/problems/D/"""


# pylint: disable=invalid-name


# this solutions is not so algorithmic
if __name__ == "__main__":
    bench_len, blocks_num = map(int, input().split())
    centre, is_odd = divmod(bench_len, 2)
    dists = {pos: pos - centre for pos in (int(i) for i in input().split())}
    if is_odd and dists.get(centre) == 0:
        print(centre)
    else:
        # this logics fails on invalid zeros only data which is normal
        negdists = {p: d for p, d in dists.items() if d < 0}
        posdists = {p: d for p, d in dists.items() if d >= 0}
        min1 = max(negdists, key=negdists.get)
        min2 = min(posdists, key=posdists.get)
        print(f'{min1} {min2}')
