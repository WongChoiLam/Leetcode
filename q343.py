class Solution:
    def integerBreak(self, n: int) -> int:
        ans = [0 for _ in range(n + 1)]
        ans[1] = 1
        for i in range(2, len(ans)):
            max_break = 0
            for j in range(1, i):
                print(i,j, ans[j] * ans[i - j])
                max_break = max(ans[j] * ans[i - j], max_break)
                max_break = max(j * ans[i-j], max_break)
                max_break = max(j * (i - j), max_break)
            ans[i] = max_break
        print(ans)
        return ans[n]