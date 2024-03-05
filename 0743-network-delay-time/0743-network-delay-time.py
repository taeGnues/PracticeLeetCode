class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    
        graph = {i : [] for i in range(1,n+1)} # 인접리스트 생성

        for i in times :
            graph[i[0]].append((i[2], i[1]))  # 인접 리스트에 삽입하기! (cost, vertex)


        costs = {}
        pq = []
        heapq.heappush(pq, (0, k)) # (cost, st)

        while pq :
            cur_cost, cur_v = heapq.heappop(pq)
            if cur_v not in costs:
                costs[cur_v] = cur_cost
                for cost, next_v in graph[cur_v]:
                    next_cost = cost + cur_cost
                    heapq.heappush(pq, (next_cost, next_v)) # 넣기만해도, 항상 pop하면 최소값만 나오게됨!!!

        if len(costs)!=n : return -1

        return max(costs.values())