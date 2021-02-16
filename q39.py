from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def bt(c : List[int]):
            if sum(c) == target: ans.append(c)
            if sum(c) > target: return
            for num in candidates:
                if(len(c) == 0 or num >= c[-1]): bt(c + [num])
        bt([])
        return ans