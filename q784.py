from typing import List
class Solution:
    def is_digit(self,x):
        return 47 < ord(x) and ord(x) < 58
    def letterCasePermutation(self, S: str) -> List[str]:
        if len(S) == 1:
            if self.is_digit(S):
                return [S]
            [S.lower(), S.upper()]
        ans = []
        for i in range(len(S)):
            if self.is_digit(S[i]): continue
            pre = S[:i+1]
            next_p = self.letterCasePermutation(S[i+1:])
            ans += [pre.lower() + p for p in next_p]
            ans += [pre.upper() + p for p in next_p]
            return ans
        return [S]