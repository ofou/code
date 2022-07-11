#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start

from itertools import combinations
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, j in combinations(range(len(nums)), 2):
            if nums[i] + nums[j] == target:
                return [i, j]

# @lc code=end
