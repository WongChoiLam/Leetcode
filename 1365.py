class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        ans = {}
        index = 0
        while index < len(sorted_nums):
            ans[sorted_nums[index]] = index
            index += 1
            while index < len(sorted_nums) and sorted_nums[index] == sorted_nums[index-1]:index += 1
        return [ans[i] for i in nums]