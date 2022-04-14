#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28724/problems/C/"""

# pylint: disable=invalid-name

from collections import Counter
from typing import List

def sanitize_input() -> List[List[int]]:
    inlines = [list(map(int, input().split())) for _ in range(3)]
    board = []
    for row in inlines:
        if len(row) != 3 or not (set(row) <= {0, 1, 2}):
            raise ValueError(f'{row} is an invalid row.')
        board.append(row)
    return board

if __name__ == "__main__":
    moves = sanitize_input()
    print(moves)