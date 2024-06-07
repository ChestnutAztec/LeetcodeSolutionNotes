#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time
from typing import List
from util import generate_random_list


class SeparateBlackAndWhiteBalls(object):
    """docstring for SeparateBlackAndWhiteBalls"""
    def __init__(self):
        pass

    def minimumSteps(self, s: str) -> int:
        """TODO: Docstring for separate.
        :returns: TODO
        """
        ans = 0
        n = len(s)
        m = 0
        j = n - 1
        while j >= 0:
            first_zero_index = n - 1 - m
            if s[j] == '1':
                ans += first_zero_index - j
                m += 1
            j -= 1
        return ans


def main():
    """TODO: Docstring for main.
    :returns: TODO
    """
    nums = generate_random_list(10, 0, 1)
    s = ''.join([f'{item}' for item in nums])
    #s = '101'
    #s = '0111'
    #s = '100'
    print(s)
    ans = SeparateBlackAndWhiteBalls().minimumSteps(s)
    print(ans)


if __name__ == "__main__":
    main()
