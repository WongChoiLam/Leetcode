class Solution:
    def balancedStringSplit(self, s: str) -> int:
        L = 1 if s[0] == 'L' else 0
        R = 1 - L
        ans = 0
        for i in range(1, len(s)):
            if s[i] == 'L':
                L += 1
            else:
                R += 1
            if L==R:
                ans += 1
        return ans