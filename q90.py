from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        stack = [[]]
        while len(stack) > 0:
            seq = stack.pop()
            if len(seq) == len(nums):
                ans.add(tuple(sorted([nums[i] for i,v in enumerate(seq) if v])))
                continue
            s1 = seq.copy()
            s1.append(True)
            stack.append(s1)
            s2 = seq.copy()
            s2.append(False)
            stack.append(s2)
        return ans