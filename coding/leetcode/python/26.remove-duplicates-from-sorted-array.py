#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return len(nums)
        i = 0
        while(i != len(nums)-1):
            first = nums.pop(i)
            if nums[i] == first:
                continue
            else:
                nums.insert(i, first)
                i += 1
        return i+1


# @lc code=end
