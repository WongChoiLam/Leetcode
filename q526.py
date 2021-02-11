class Solution:
    def countArrangement(self, n: int) -> int:
        def options(x:int):
            ans = []
            for i in range(1,x + 1):
                if x % i == 0: ans.append(i)
            for i in range(x+1, n+1):
                if i % x == 0: ans.append(i)
            return ans
        stack = [[]]
        ans = 0
        while len(stack) > 0:
            arr = stack.pop()
            if len(arr) == n:
                ans+=1
                continue
            next_number = len(arr) + 1
            for option in options(next_number):
                if option in arr: continue
                stack.append(arr + [option])
        return ans

print(Solution().countArrangement(2))