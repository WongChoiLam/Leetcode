from typing import List
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        occ = {}
        for i in arr:
            if not i in occ:
                occ[i] = 0
            occ[i] += 1
        half = len(arr) - int(len(arr) / 2)
        occ_list = sorted(list(occ.values()), reverse=True)
        
        sum_occ = 0
        ans = 0
        for i in occ_list:
            sum_occ += i
            ans += 1
            if sum_occ >= half:
                return ans
                
        