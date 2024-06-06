#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:

    def gcd(self, a, b):
        """TODO: Docstring for gcd.
        :a: TODO
        :b: TODO
        :returns: TODO
        """
        while b > 0:
            t = a % b
            a = b
            b = t
        return a

    def lcm(self, a, b):
        """TODO: Docstring for lcm.
        :a: TODO
        :b: TODO
        :returns: TODO
        """
        return a * b // self.gcd(a, b)

    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = self.lcm(a, b)
        bc = self.lcm(b, c)
        ac = self.lcm(a, c)
        abc = self.lcm(self.lcm(a, b), c)
        min_val = min([a,b,c])
        left = min_val
        right = min_val * (n + 1)
        while left < right:
            mid = (right - left) // 2 + left
            ugly_num = mid // a + mid // b + mid // c - mid // ab - mid // ac - mid // bc + mid // abc
            if ugly_num < n:
                left = mid + 1
            else:
                right = mid
        return left


def main():
    """TODO: Docstring for main.
    :returns: TODO
    """
    n, a, b, c = [3, 2, 3, 5]
    #n, a, b, c = [4, 2, 3, 4]
    #n, a, b, c = [5, 2, 11, 13]

    #n, a, b, c = [1000000000, 2, 217983653, 336916467]
    ret = Solution().nthUglyNumber(n, a, b, c)
    print(ret)
    #print(Solution().lcm(2*3*5, 2*5*7))


if __name__ == "__main__":
    main()
