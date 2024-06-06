#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
二叉索引树: 通过 O(logN) 和 O(logN) 的时间分别完成前缀和的计算和更新

# 对于数组 nums, 计算任何 index \in [i, j) 的和
sum(i, j) = sum_i^j nums[index]

# 前缀和的计算方式
1. 暴力计算: 计算复杂度 O(N), 更新复杂度 O(1)
2. 前缀和数组: 计算复杂度 sum(i, j) = pre_sum[j] - pre_sum[i]. 计算复杂度 O(1), 更新复杂度 O(N)

# 二叉索引树: 上述2中方式中找到平衡
核心逻辑
1. 类似前缀数组, c[i] 表示 i 结尾的前面 n 个元素的和
2. 不同于前缀数组, n = i + 1; 二叉索引树的 n 和 i 相关
3. 实际计算的时候, n = lowBit(i) i 的二进制表示下, 最低位的 1 及后面的0构成的数值
   或者理解成, 对于所有的 k, 满足 i % 2^k == 0 的最大的 k
   1) i 为2的幂: 这是等于平凡的前缀和
   2) i 不为2的幂, 等于 (i-2^k, i] 的区间和
   每个 C[index] 覆盖 lowBit 个 nums 的和
4. 这样构造的树状结构的父子坐标关系
   1) index 直接覆盖的子节点
      index - lowBit(index)
   2) index 的直接父节点
      index + lowBit(index)
5. 计算过程: 给定一个 index.
   逐层去找 index 的子节点 ans + 子节点
   while index > 0:
       ans += C[index]
       index = index - lowBit(index)
6. 更新过程: 更新 index 处的 nums[index] 值. 需要更新线断数组 C 的对应值
   需要更新的index:
   1) index 本身
   2) 所有的 i, 满足 i - lowBit(i) < index <= i 时, 都需要更新
   3) 实际上, 是逐个去找 index 对应的父节点.
7. 更高效的计算 lowBit 方式: lowBit(index) = index & (-1 * index)
   -index 的二进制是 index 的二进制取反 + 1
   比如 index = 6 -> 00000110
   -6 -> 11111001 + 1 -》 11111010
   index & -index 即可得到 index 的 lowBit
"""

import time
import random
import math


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


class PreSum(object):
    """docstring for PreSum"""
    def __init__(self, nums):
        N = len(nums)
        self.pre_sum = [0 for i in range(N + 1)]
        for i in range(0, N):
            self.pre_sum[i + 1] += self.pre_sum[i] + nums[i]

    def get(self, index):
        """TODO: Docstring for get.
        :index: TODO
        :returns: TODO
        """
        return self.pre_sum[index]

    def update(self, index, delta_val):
        """TODO: Docstring for update.
        :index:
        :delta_val: 更新值的 delta_val = new_nums[index] - old_nums[index]
        :returns: TODO
        """
        for i in range(index, len(self.pre_sum)):
            self.pre_sum[i] += delta_val


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


def main():
    """TODO: Docstring for main.
    :returns: TODO
    """
    T = 1
    for i in range(T):
        ts_1_list = []
        ts_2_list = []
        up_ts_1_list = []
        up_ts_2_list = []
        n = random.randint(1, 1000)
        nums = generate_random_list(n, min_val=0, max_val=max(n-100, 100))
        #nums = [1, 2, 3, 4, 5]
        #print(nums)
        p_sum = PreSum(nums)
        bit = BinaryIndexTree(nums)
        for i in range(len(nums)):
            delta_val = random.randint(1, 10)
            # update
            s_time = time.time()
            p_sum.update(i+1, delta_val)
            up_ts_1 = time.time() - s_time
            s_time = time.time()
            bit.update(i+1, delta_val)
            up_ts_2 = time.time() - s_time
            up_ts_1_list.append(up_ts_1)
            up_ts_2_list.append(up_ts_2)

            # search
            s_time = time.time()
            val_1 = p_sum.get(i + 1)
            ts_1 = time.time() - s_time
            s_time = time.time()
            val_2 = bit.get(i + 1)
            ts_2 = time.time() - s_time
            #print(ts_1, ts_2)
            ts_1_list.append(ts_1)
            ts_2_list.append(ts_2)
            #print(i, val_1, val_2)
            assert(val_1 == val_2)
        ts_1 = sum(ts_1_list) / len(ts_1_list) * 1e8
        ts_2 = sum(ts_2_list) / len(ts_2_list) * 1e8
        up_ts_1 = sum(up_ts_1_list) / len(up_ts_1_list) * 1e8
        up_ts_2 = sum(up_ts_2_list) / len(up_ts_2_list) * 1e8
        print(n, ts_1, ts_2, up_ts_1, up_ts_2)


if __name__ == "__main__":
    main()
