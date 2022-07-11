#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [('FizzBuzz' if i % 3 == 0 and i % 5 == 0 else
                 ('Fizz' if i % 3 == 0 else
                  ('Buzz' if i % 5 == 0 else str(i))))
                for i in range(1, n+1)]

# @lc code=end
