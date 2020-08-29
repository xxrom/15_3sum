from typing import List

class Solution:
  def getKey(self, keys: List[int]):
    return ''.join(str(sorted(keys)))

  def findAns(self, path: List[int], others: List[int], curSum: int):
    # print(path)
    if len(path) == 3:
      if curSum == 0:
        keys = self.getKey(path)
        if keys not in self.ans:
          self.ans[keys] = path
          # print('FOUND!')

    if len(path) <= 2:
      twoPath = self.getKey(path)

      if len(path) == 2 and twoPath in self.memo:
        return

      self.memo[twoPath] = True

      for index, num in enumerate(others):
        if len(path) == 2 and num > -1 * curSum:
          # print('EXIT')
          break

        self.findAns(path + [num], others[:index] + others[index + 1:], curSum + num)

  def threeSum(self, nums: List[int]) -> List[List[int]]:
    sortedNums = sorted(nums)

    # print(sortedNums)

    self.ans = {}
    self.memo = {}
    for index, num in enumerate(sortedNums):
      self.findAns([num], sortedNums[:index] + sortedNums[index + 1:], num)
    # print(self.ans)

    return list(self.ans.values())

my = Solution()
n = [-1, 0, 1, 2, -1, -4]

trueAns=[
  [-1, 0, 1],
  [-1, -1, 2]
]

ans = my.threeSum(n)
print("ans", ans, ans == trueAns)
