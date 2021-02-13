from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        visited = set()
        visited.add(0)
        while len(stack) > 0:
            room_index = stack.pop()
            for key in rooms[room_index]:
                if not key in visited:
                    stack.append(key)
                    visited.add(key)
        if len(visited) == len(rooms):
            return True
        return False