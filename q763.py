from typing import List
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        alphabet = OrderedDict()
        for i in range(len(S)):
            if not S[i] in alphabet:
                alphabet[S[i]] = [i, i]
            else:
                alphabet[S[i]][1] = i
        ans = []
        last = -1
        k, v = alphabet.popitem(last=False)
        lo, hi = v
        while len(alphabet) > 0:
            k, v = alphabet.popitem(last=False)
            nl, nh = v
            if nl > hi:
                ans.append(hi - last)
                last = hi
                lo, hi = nl, nh
            else:
                hi = max(nh, hi)
        ans.append(len(S) - 1 - last)
        return ans