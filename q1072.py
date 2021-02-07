class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        def solution(row : List[int]) -> List[bool]:
            if sum(row) == 0 or sum(row) == len(row):
                return tuple([False] * len(row))
            k = row[0]
            return tuple([i==k for i in row])
        count = {}
        for row in matrix:
            s = solution(row)
            if not s in count:
                count[s] = 0
            count[s] += 1
        return sorted(list(count.items()), key=lambda x:x[1], reverse=True)[0][1]