#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 11:37 上午
# @Author  : CHAO
# @Email   : Glen_CHAO@163.com
# @File    : 81. 搜索旋转排序数组 II.py


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        flag = False
        for num in nums:
            if num == target:
                flag = True
                break
        return flag


if __name__ == '__main__':
    s = Solution()
    nums = [2,5,6,0,0,1,2]
    target = 0
    print(s.search(nums, target))



