class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ' '.join([word for word in s.strip().split(' ')[::-1] if word!=''])
        return ans