class Solution:
    def combination(self,groups):
        if len(groups) == 1:
            return list(groups[0])
        next_combination = self.combination(groups[1:])
        ret = []
        for c in groups[0]:
            ret.extend([c + e for e in next_combination])
        return ret
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return ""
        mapping = ["" for _ in range(10)]
        mapping[2] = 'abc'
        mapping[3] = 'def'
        mapping[4] = 'ghi'
        mapping[5] = 'jkl'
        mapping[6] = 'mno'
        mapping[7] = 'pqrs'
        mapping[8] = 'tuv'
        mapping[9] = 'wxyz'
        groups = [mapping[int(d)] for d in digits]
        return self.combination(groups)