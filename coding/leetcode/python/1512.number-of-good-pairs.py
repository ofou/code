#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0
        for i, j in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    counter += 1
        return counter

# @lc code=end
