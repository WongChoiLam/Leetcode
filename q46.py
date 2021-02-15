from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: return [[nums[0]]]
        ans = []
        for i in range(len(nums)):
            n = self.permute(nums[:i] + nums[i+1:])
            k = [[nums[i]] + p for p in n]
            ans = ans + k
        return ans
            