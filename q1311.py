from typing import List
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue = deque([(0, id)])
        visited = set()
        visited.add(id)
        ans_dict = {}
        while len(queue) > 0:
            nlevel, nid = queue.popleft()
            if nlevel ==level:
                for videoName in watchedVideos[nid]:
                    if not videoName in ans_dict:
                        ans_dict[videoName] = 1
                    else:
                        ans_dict[videoName] += 1
            elif nlevel < level:
                for friend_id in friends[nid]:
                    if not friend_id in visited:
                        queue.append((nlevel+1, friend_id))
                        visited.add(friend_id)
        ans_list = list(ans_dict.items())
        ans_list.sort(key=lambda x:(x[1],x[0]))
        return [x[0] for x in ans_list]
                    