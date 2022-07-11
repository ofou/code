#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for index, number in enumerate(nums):
            temp = [y for y in [x for i, x in enumerate(
                nums) if i != index] if y < number]
            result.append(len(temp))
        return result
# @lc code=end
