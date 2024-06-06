#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random


def generate_random_list(num, min_val=0, max_val=100, allow_dup=True):
    """TODO: Docstring for generate_random_list.
    :num: TODO
    :min_val: TODO
    :max_val: TODO
    :allow_dup: TODO
    :returns: TODO
    """
    nums = []
    while num:
        if allow_dup:
            nums.append(random.randint(min_val, max_val))
        num -= 1
    return nums
