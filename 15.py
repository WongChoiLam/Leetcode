from typing import List
class Solution:
    def twoSum(self, target : int, nums: List[int]) -> List[List[int]]:
        ans = []
        small, big = 0, len(nums) - 1
        while big > small:
            candidate = [nums[small], nums[big]]
            candidate_sum = sum(candidate)
            if candidate_sum == target:
                ans.append(candidate)
                small += 1
                big -= 1
                while nums[small] == nums[small - 1] and big > small: small += 1
                while nums[big] == nums[big + 1] and big > small: big -= 1
            elif candidate_sum < target:
                small += 1
                while nums[small] == nums[small - 1] and big > small: small += 1
            elif candidate_sum > target:
                big -= 1
                while nums[big] == nums[big + 1] and big > small: big -= 1
        return ans
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        ans = []
        index = 0
        while index < N - 2:
            fix = nums[index]
            ans = ans + [[fix] + two for two in self.twoSum(-fix, nums[index + 1:N])]
            index += 1
            while index < N and nums[index] == nums[index-1]: index += 1
        return ans