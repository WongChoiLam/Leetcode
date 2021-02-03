from typing import List
class Solution:
    def flip(self, num):
        first = 1
        while not first * 2 > num: 
            first *= 2
        return first * 2 - 1 - (num - first)
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = [label]
        while label != 1:
            label = self.flip(int(label / 2))
            ans.insert(0, label)
        return ans
        
s = Solution()
print(s.pathInZigZagTree(26))