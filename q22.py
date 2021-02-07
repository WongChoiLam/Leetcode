class Solution:
    def generate(self, n:int, acc:str, index:int, opened:int, ans: List[str]) -> List[str]:
        if index == (n*2): return [] if opened != 0 else [acc]
        if opened != 0:
            ans = ans + self.generate(n, acc + ')', index + 1, opened - 1, [])
        ans = ans + self.generate(n, acc + '(', index + 1, opened + 1, [])
        return ans
    def generateParenthesis(self, n: int) -> List[str]:
        return self.generate(n, "", 0, 0, [])