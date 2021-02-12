class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda X : X[0] ** 2 + X[1] ** 2)[:K]