from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def bt(c : List[int]):
            if len(c) == k:
                if sum(c) == n: ans.append(c)
                return
            lo = c[-1] if len(c) > 0 else 0
            for num in range(lo + 1, 10):
                bt(c + [num])
        bt([])
        return ans