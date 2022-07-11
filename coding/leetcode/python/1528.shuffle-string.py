#
# @lc app=leetcode id=1528 lang=python3
#
# [1528] Shuffle String
#

# @lc code=start
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [None] * len(indices)

        for index, position in enumerate(indices):
            result[position] = s[index]

        return ''.join(result)

# @lc code=end
