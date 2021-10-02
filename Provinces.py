from collections import deque
class Solution:
    def bfs(self, isConnected, visited, city):
        if visited[city]:
            return
        que = deque()
        visited[city] = True
        que.append(city)
        while que:
            cty = que.popleft()
            for adcity, ispath in enumerate(isConnected[cty]):
                if visited[adcity] or ispath == 0:
                    continue
                visited[adcity] = True
                que.append(adcity)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        prov = 0
        visited = [False for _ in range(len(isConnected))]
        for city in range(len(isConnected)):
            if visited[city] == True:
                continue
            self.bfs(isConnected, visited, city)
            prov += 1
        return prov
