#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
from functools import reduce


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = []
        for i, n in enumerate(nums, start=1):
            suma = reduce(lambda a, b: a+b, nums[0:i], 0)
            temp.append(suma)
        return temp

# @lc code=end
