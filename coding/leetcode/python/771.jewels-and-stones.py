#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return len([s for s in S if s in J])

# @lc code=end
