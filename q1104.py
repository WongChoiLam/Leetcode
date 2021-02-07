class Solution:
    def flip(self, num, first):
        return first * 2 - 1 - (num - first)
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = [label]
        first = 1
        while not first * 2 > label: 
            first *= 2
        while label != 1:
            first = int(first / 2)
            label = self.flip(int(label / 2), first)
            ans.insert(0, label)
        return ans