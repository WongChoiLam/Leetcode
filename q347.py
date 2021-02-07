class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if not n in count:
                count[n] = 0
            count[n] += 1
        ans = sorted(list(count.items()), key=lambda x:x[1], reverse=True)[:k]
        return [x[0] for x in ans]