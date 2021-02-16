from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def bt(c : List[int]):
            if(len(c) == k): ans.append(c)
            l = 0 if len(c) == 0 else c[-1]
            for i in range(l + 1, n + 1):
                bt(c + [i])
        bt([])
        return ans