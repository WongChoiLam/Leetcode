from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(0, int(n / 2)):
            first = i
            last = -1 - i
            s[first], s[last] = s[last], s[first]