#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28724/problems/A/"""

# pylint: disable=invalid-name

if __name__ == "__main__":
    a, b, c, d = (int(input()) for _ in range(4))
    # if both a and b are equal to zero
    if not (a or b):
        print("INF")
    # otherwise if only a = 0 or the fraction is a proportion
    elif (a == 0) or (b * c == a * d):
        print("NO")
    elif b % a == 0:
        print(-b // a)
    else:
        print("NO")
