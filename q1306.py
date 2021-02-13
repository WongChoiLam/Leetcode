from typing import List
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        visited.add(start)
        stack = [start]
        
        in_arr = lambda x : 0<=x and x<len(arr)
        
        while len(stack) > 0:
            i = stack.pop()
            if arr[i] == 0: return True
            a = i + arr[i]
            b = i - arr[i]
            if in_arr(a) and (not a in visited):
                stack.append(a)
                visited.add(a)
            if in_arr(b) and (not b in visited):
                stack.append(b)
                visited.add(b)
        return False