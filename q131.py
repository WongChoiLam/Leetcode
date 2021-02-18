from typing import *
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            for i in range(int(len(s) / 2)):
                if s[i] != s[-1 - i]: return False
            return True
        def condition(partition : List[int]):
            num = 0
            for i in partition:
                substring = s[num:num + i]
                # print('\t', substring)
                if not isPalindrome(substring): return False
                num += i
            return True
        stack = [[1]]
        ans = []
        while len(stack) > 0:
            partition = stack.pop()
            if sum(partition) == len(s):
                if condition(partition):
                    ans.append(partition)
                continue
            p1 = partition.copy()
            p1[-1] += 1
            stack.append(p1)
            p2 = partition.copy()
            p2.append(1)
            stack.append(p2)
        ret = []
        for partition in ans:
            ret.append([])
            num = 0
            for i in partition:
                substring = s[num:num + i]
                ret[-1].append(substring)
                num += i
        return ret

print(Solution().partition("aab"))