from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def bt(c):
            if c[-1] == (len(graph) - 1): ans.append(c)
            for n in graph[c[-1]]:
                if not n in c:
                    bt(c + [n])
        bt([0])
        return ans