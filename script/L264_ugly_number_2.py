#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time
import numpy as np

"""
UglyNumberII:
# 定义: 如果一个 num, 因子只有 2, 3, 4 则 num 为一个 ugly num
# 问题: 给定一个 n, 求第 n 个 ugly num. n=1 时为 1 (2**0 *3**0 * 5**0)

# 思路:
假定前 k-1 个 ugly num 构成 ans, len(ans) = k-1
第 k 个 ugly_num ans[k] = min(ans[i] * 2, ans[j] * 3, ans[l] * 5)
    if i, j, l < k & ans[i] * 2 > ans[k-1] & ans[j] * 3 > ans[k-1] & ans[l] * 5 > ans[k-1]
可以二分去找这样的 i, j, l
对所有的 prime in [2, 3, 5]
找第一个 index, 满足对所有的 i <= index, ans[i] * prime <= T; 所有的 i > index, ans[i] * prime > T
则 ans[index] * prime 是下一个 ugly_num 的候选

# 上述思路很容易直接写成每次都对所有的 ans 二分查找
实际上, 对于 prime = 3
上一轮找到的 index, 一定是下一轮二分查找的 left 位置.
index 之前的一定不可能再满足 ans[index] * prime > T

实验中, 加上这个优化后, 相比直接二分要再快10倍
"""

class UglyNumberII:

    def is_ugly_number(self, num):
        """TODO: Docstring for is_ugly_number.
        :num: TODO
        :returns: TODO
        """
        if num == 1:
            return True
        for prime in [2, 3, 5]:
            if num % prime == 0 and self.is_ugly_number(num // prime):
                return True
        return False

    def binary_search(self, nums, T, prime):
        """TODO: Docstring for binary_search.
        找到第一个 index, 满足对所有的 i < index, nums[i] * prime <= T
        对 i >= index, nums[i] * prime > T
        :nums: TODO
        :left: TODO
        :right: TODO
        :T: TODO
        :returns: TODO
        """
        left = 0
        right = len(nums)
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] * prime <= T:
                left += 1
            else:
                right = mid
        return left

    def nthUglyNumber_v1(self, n):
        """TODO: Docstring for nthUglyNumber_v1.
        :n: TODO
        :returns: TODO
        """
        ret_list = []
        for i in range(1, 5**n):
            if self.is_ugly_number(i):
                ret_list.append(i)
                if len(ret_list) == n:
                    break
        return ret_list[-1]

    def nthUglyNumber(self, n: int) -> int:
        """
        二分查找: 优化每轮查找位置
        """
        ret = 0
        data_list = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30]
        if n <= len(data_list):
            return data_list[n - 1]
        else:
            last_index_dict = {5: 0, 3: 0, 2: 0}
            while len(data_list) < n:
                T = data_list[-1]
                nxt = None
                tl = []
                for prime, last_index in last_index_dict.items():
                    index = self.binary_search(data_list[last_index:], T, prime)
                    index = last_index + index
                    nxt = prime * data_list[index] if nxt is None else min(nxt, prime * data_list[index])
                    tl.append([prime * data_list[index],  prime,  data_list[index], T])
                    last_index_dict[prime] = index
                data_list.append(nxt)
        return data_list[-1]

    def nthUglyNumber_v2(self, n: int) -> int:
        """
        二分查找: 第一次优化
        """
        ret = 0
        data_list = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30]
        if n <= len(data_list):
            return data_list[n - 1]
        else:
            while len(data_list) < n:
                T = data_list[-1]
                nxt = None
                for prime in [2, 3, 5]:
                    index = self.binary_search(data_list, T, prime)
                    nxt = prime * data_list[index] if nxt is None else min(nxt, prime * data_list[index])
                data_list.append(nxt)
        return data_list[-1]


def main():
    """TODO: Docstring for main.
    :returns: TODO
    """
    ts1_list = []
    ts2_list = []
    ts3_list = []
    for n in range(400, 600):
        #s_time = time.time()
        #r1 = UglyNumberII().nthUglyNumber_v1(n)
        #ts1 = time.time() - s_time

        s_time = time.time()
        r2 = UglyNumberII().nthUglyNumber_v2(n)
        ts2 = time.time() - s_time

        s_time = time.time()
        r3 = UglyNumberII().nthUglyNumber(n)
        ts3 = time.time() - s_time

        #print(n, r1, r2, r3, f'time_cost: {ts1:.6f} v {ts2:.6f} v {ts3:.6f}')
        print(n, r2, r3, f'time_cost: {ts2:.6f} v {ts3:.6f} [{ts3 / ts2:.1%}]')
        #ts1_list.append(ts1)
        ts2_list.append(ts2)
        ts3_list.append(ts3)
        #assert(r1 == r2 and r2 == r3)
        assert(r2 == r3)
    #ts1, ts2, ts3 = np.mean(ts1_list), np.mean(ts2_list), np.mean(ts3_list)
    #print(ts1, ts2, ts3, f'{ts2 / ts1:.1%}', f'{ts3 / ts2:.1%}')
    ts2, ts3 = np.mean(ts2_list), np.mean(ts3_list)
    print(ts2, ts3, f'{ts3 / ts2:.1%}')


if __name__ == "__main__":
    main()
