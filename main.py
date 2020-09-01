# URL: explanation and solution
# https://leetcode.com/problems/3sum/discuss/7498/Python-solution-with-detailed-explanationzzu
from typing import List

class Solution:
  def getKey(self, keys: List[int]):
    return ''.join(str(keys))

  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()

    size = len(nums)

    self.ans = {}
    for i in range(size - 2): # -2 - because of left and right need place to be
      # Imagine we are at index i and we have invoked the 2SUM problem from index i+1
      # to end of the array. Now once the 2SUM terminates, we will have a list of all
      # triplets which include nums[i]. To avoid duplicates, we must skip all nums[i]
      # where nums[i] == nums[i-1].
      if i > 0 and nums[i] == nums[i - 1]:
        continue

      l = i + 1
      r = size - 1

      while l < r:
        if nums[l] + nums[r] < -nums[i]:
          l = l + 1
        elif nums[l] + nums[r] > -nums[i]:
          r = r - 1
        else:
          # print([l, i, r])
          keys = [nums[l], nums[i], nums[r]]
          keys.sort()
          self.ans[self.getKey(keys)] = keys

          # Say index s and e are forming a solution in a sorted array. Now givens nums[s],
          # there is a unique nums[e] such that nums[s]+nums[e]=Target. Therefore, if nums[s+1]
          # is the same as nums[s], then searching in range s+1 to e will give us a duplicate
          # solution. Thus we must move s till nums[s] != nums[s-1] to avoid getting duplicates.
          while l < r and nums[l] == nums[l+1]:
            l = l + 1
          while l < r and nums[r] == nums[r - 1]:
            r = r - 1

          l = l + 1
          r = r - 1

    return list(self.ans.values())


my = Solution()
# n = [-1, 0, 1, 2, -1, -4]
n = [0, 0, 0]
trueAns=[
  [-1, 0, 1],
  [-1, -1, 2]
]

ans = my.threeSum(n)
print("ans", ans, ans == trueAns)

# a + b + c = 0
# a + c = -b

# a + c < -b => increment a + c sum => a index ++
# a + c > -b => decrement a + c sum => c index --

# Runtime: 1064 ms, faster than 60.28% of Python3 online submissions for 3Sum.
# Memory Usage: 17.9 MB, less than 16.22% of Python3 online submissions for 3Sum.