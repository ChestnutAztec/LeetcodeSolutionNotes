#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from util import generate_random_list

class TrappingRainWater(object):
    """docstring for TrappingRainWater"""
    def __init__(self):
        pass

    def find_next(self, height_list, cur, direction=1):
        """TODO: Docstring for find_next.
        双指针的算法, 进入 find_next 时, 可以保证, 从 cur 向 direction 方向找的时候
        height_list 中必定存在一个 i 满足 height_list[i] >= height_list[cur]
        所以不需要额外判断越界
        :cur: TODO
        :dir: TODO
        :returns: TODO
        """
        ans = 0
        nxt = cur + direction
        while 0 <= nxt < len(height_list) and height_list[nxt] < height_list[cur]:
            ans += height_list[cur] - height_list[nxt]
            nxt = nxt + direction
        # 循环退出时, 一定是找到了这样的 i
        return nxt, ans

    def trap(self, height_list):
        """TODO: Docstring for trap.
        :height: TODO
        :returns: TODO
        """
        ret = 0
        left = 0
        right = len(height_list) - 1
        while left < right:
            if height_list[left] < height_list[right]:
                # 向右寻找第一个 i, height_list[i] >= height_list[left]
                nxt, ans = self.find_next(height_list, left, direction=1)
                ret += ans
                left = nxt
            else:
                # 向左寻找第一个 j, height_list[j] >= height_list[right]
                nxt, ans = self.find_next(height_list, right, direction=-1)
                ret += ans
                right = nxt
        return ret


def main():
    """TODO: Docstring for main.
    :returns: TODO
    """
    #height_list = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    #height_list = [4, 2, 0, 3, 2, 5]
    #height_list = [1,  1, 3]
    #height_list = generate_random_list(10, 0, 20)
    for i in range(100):
        n = random.randint(0, 20)
        height_list = generate_random_list(n, 0, 20)
        print(height_list)
        # ret = TrappingRainWater().trap(height_list)
        # print(ret)


if __name__ == "__main__":
    main()
