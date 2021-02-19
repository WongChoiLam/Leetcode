from typing import List
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        low_len = len(str(low))
        if low_len > 9: return ans
        to_next = lambda x : [chr(ord(c) + 1) for c in x]
        character_list = [str(i + 1) for i in range(low_len)]
        length = low_len
        num = int("".join(character_list))
        while num <= high:
            if num >= low: ans.append(num)
            if character_list[-1] != '9':
                character_list = to_next(character_list)
            else:
                length += 1
                character_list = [str(i + 1) for i in range(length)]
            num = int("".join(character_list))
        return ans
print(Solution().sequentialDigits(100, 300))