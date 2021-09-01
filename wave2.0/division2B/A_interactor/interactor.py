#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://contest.yandex.ru/contest/28730/problems/"""


def solve(return_code: int,
           interactor_code: int,
           checker_code: int) -> int:
    """
    Return the final decision.

    Parameters
    ----------
    return_code : int
        -128 <= r <= 127.
    interactor_code : int
        0 <= i <= 7.
    checker_code : int
        0 <= c <= 7.

    Returns
    -------
    int

    """
    if (-128 <= return_code <= 127) and \
        (0 <= interactor_code <= 7) and \
        (0 <= checker_code <= 7):
            if interactor_code == 0:
                if return_code:
                    return 3
                return checker_code
            if interactor_code == 1:
                return checker_code
            if interactor_code == 4:
                if return_code:
                    return 3
                return 4
            if interactor_code == 6:
                return 0
            if interactor_code == 7:
                return 1
            return interactor_code
                


if __name__ == '__main__':
    ret, inter, check = (int(input()) for _ in range(3))
    print(f'\nans = {solve(ret, inter, check)}')
