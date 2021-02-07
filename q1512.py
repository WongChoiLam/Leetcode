from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if not num in count.keys(): count[num] = 0
            count[num] += 1
        pair = 0
        for num in count.keys():
            pair += count[num] * (count[num] - 1) / 2
        return int(pair)