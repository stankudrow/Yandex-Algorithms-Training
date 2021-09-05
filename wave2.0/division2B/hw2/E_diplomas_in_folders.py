#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28738/problems/E/"""


# pylint: disable=invalid-name


if __name__ == "__main__":
    folders_total = int(input())
    folders = tuple(map(int, input().split()))
    print(sum(sorted(folders)[:-1]))
