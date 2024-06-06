#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time
from typing import List
from data_structure import BinaryIndexTree
from util import generate_random_list


class BinaryIndexTree(object):
    """docstring for BinaryIndexTree
    """
    def __init__(self, nums):
        N = len(nums)
        self.sum_arr = [0] * (N + 1)
        for i in range(N):
            self.update(i+1, nums[i])

    def get(self, index):
        """TODO: Docstring for get.
        :index: TODO
        :returns: TODO
        """
        ans = 0
        while index > 0:
            ans += self.sum_arr[index]
            index -= index & -index
        return ans

    def update(self, index, delta_val):
        """TODO: Docstring for update.
        :index:
        :delta_val: 更新值的 delta_val = new_nums[index] - old_nums[index]
        :returns: TODO
        """
        while index < len(self.sum_arr):
            self.sum_arr[index] += delta_val
            index += index & -index


class DistributeElementsIntoTwoArrays(object):
    """docstring for DistributeElementsIntoTwoArrays"""
    def __init__(self):
        pass

    def resultArray(self, nums: List[int]) -> List[int]:
        """TODO: Docstring for distribute.
        :nums: TODO
        :returns: TODO
        """
        if len(nums) < 2:
            return nums
        array_1 = []
        array_2 = []

        sorted_nums = sorted(nums)
        index_map = {}
        index = 1
        for num in sorted_nums:
            if not num in index_map:
                index_map[num] = index
                index += 1
        N = len(index_map)
        bit_1 = BinaryIndexTree([0] * N)
        bit_2 = BinaryIndexTree([0] * N)

        array_1.append(nums[0])
        array_2.append(nums[1])
        bit_1.update(index_map[nums[0]], 1)
        bit_2.update(index_map[nums[1]], 1)
        for i in range(2, len(nums)):
            index = index_map[nums[i]]
            n1 = bit_1.get(N) - bit_1.get(index)
            n2 = bit_2.get(N) - bit_2.get(index)
            if n1 > n2:
                array_1.append(nums[i])
                bit_1.update(index, 1)
            elif n1 < n2:
                array_2.append(nums[i])
                bit_2.update(index, 1)
            else:
                if len(array_1) > len(array_2):
                    array_2.append(nums[i])
                    bit_2.update(index, 1)
                else:
                    array_1.append(nums[i])
                    bit_1.update(index, 1)
        ret = array_1 + array_2
        return ret

    def distribute_v2(self, nums):
        """TODO: Docstring for distribute_v2.
        :returns: TODO
        """
        if len(nums) < 2:
            return nums
        array_1 = []
        array_2 = []
        array_1.append(nums[0])
        array_2.append(nums[1])
        for i in range(2, len(nums)):
            n1 = sum([int(val > nums[i]) for val in array_1])
            n2 = sum([int(val > nums[i]) for val in array_2])
            if n1 > n2:
                array_1.append(nums[i])
            elif n1 < n2:
                array_2.append(nums[i])
            else:
                if len(array_1) > len(array_2):
                    array_2.append(nums[i])
                else:
                    array_1.append(nums[i])
        #print(array_1)
        #print(array_2)
        ret = array_1 + array_2
        return ret



def main():
    """TODO: Docstring for main.
    :returns: TODO
    """
    # nums = [2, 1, 3, 3]
    # nums = [5, 14, 3, 1, 2]
    # nums = [3, 3, 3, 3]
    for i in range(1000,10000,100):
        nums = generate_random_list(i, 1, max(100, i - 200))
        # nums = [14, 20, 20, 14, 11, 15, 10, 7, 11, 17]

        s_time = time.time()
        ret_1 = DistributeElementsIntoTwoArrays().resultArray(nums)
        ts_1 = (time.time() - s_time) * 1e1
        s_time = time.time()
        ret_2 = DistributeElementsIntoTwoArrays().distribute_v2(nums)
        ts_2 = (time.time() - s_time) * 1e1
        print(len(nums), ts_1, ts_2)
        assert(ret_1 == ret_2)
        # break


if __name__ == "__main__":
    main()
