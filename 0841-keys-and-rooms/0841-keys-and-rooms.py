class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool: 
        # 1. 인접리스트 생성
        
        dic = {}
        
        for i in range(len(rooms)) :
            dic[i] = rooms[i]

        # 2. 인접리스트 순회. (room 0부터 시작함.)
        
        visited = [0]
        q = deque([0])
        
        while q :
            cur_v = q.popleft()
            
            for v in dic[cur_v] :
                if v not in visited:
                    visited.append(v)
                    q.append(v)
                    
        
        
        return True if len(visited) == len(rooms) else False